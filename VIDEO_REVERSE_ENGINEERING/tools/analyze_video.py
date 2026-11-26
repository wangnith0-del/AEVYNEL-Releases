#!/usr/bin/env python3
"""
Frame-by-frame analysis of a video file (read-only on the source).

For every frame (full 30 fps, no skipping) computes on a downscaled copy:
  - mean luma, saturation, RGB means
  - HSV-histogram distance to previous frame (shot-cut detector)
  - mean absolute pixel difference to previous frame
  - dense optical flow (Farneback) -> mean magnitude, median dx/dy
    (global camera-like translation), and "divergence" (zoom-like)
  - fraction of near-static pixels (to detect static backgrounds / held frames)
  - exact-duplicate frame flag (held frames / low-fps source / stills)
Writes CSV to ANALYSIS_DATA/<alias>_frames.csv and shot list JSON.

Usage: python3 -I analyze_video.py <video> <alias> <outdir>
"""
import sys, json, csv, os
import cv2
import numpy as np

src, alias, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
cap = cv2.VideoCapture(src)
fps = cap.get(cv2.CAP_PROP_FPS)
W, H = 144, 256  # 1/4 scale, keeps 9:16

rows = []
prev_small = prev_gray = prev_hist = None
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
cx, cy = (W - 1) / 2, (H - 1) / 2
rx, ry = xx - cx, yy - cy
rnorm = np.sqrt(rx ** 2 + ry ** 2) + 1e-6
i = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    small = cv2.resize(frame, (W, H), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, [16, 8, 8], [0, 180, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    b, g, r = [float(small[..., k].mean()) for k in range(3)]
    row = dict(frame=i, t=round(i / fps, 4), luma=float(gray.mean()),
               luma_std=float(gray.std()), sat=float(hsv[..., 1].mean()),
               r=r, g=g, b=b, hist_d=0.0, absdiff=0.0, flow_mag=0.0,
               flow_dx=0.0, flow_dy=0.0, flow_div=0.0, static_frac=1.0, dup=0)
    if prev_gray is not None:
        row['hist_d'] = float(cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA))
        d = cv2.absdiff(gray, prev_gray)
        row['absdiff'] = float(d.mean())
        row['static_frac'] = float((d < 3).mean())
        row['dup'] = int(d.max() <= 2)
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        fx, fy = flow[..., 0], flow[..., 1]
        mag = np.sqrt(fx ** 2 + fy ** 2)
        row['flow_mag'] = float(mag.mean())
        row['flow_dx'] = float(np.median(fx))
        row['flow_dy'] = float(np.median(fy))
        # radial component of flow: >0 = expansion (zoom in / dolly in)
        row['flow_div'] = float(((fx * rx + fy * ry) / rnorm).mean())
    rows.append(row)
    prev_gray, prev_hist = gray, hist
    i += 1
cap.release()

os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, f'{alias}_frames.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    for r_ in rows:
        w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r_.items()})

# ---- shot detection: adaptive threshold on histogram distance ----
hd = np.array([r_['hist_d'] for r_ in rows])
ad = np.array([r_['absdiff'] for r_ in rows])
cuts = [0]
win = 15
for k in range(1, len(rows)):
    lo, hi = max(1, k - win), min(len(rows), k + win + 1)
    neigh = np.concatenate([hd[lo:k], hd[k + 1:hi]])
    base = np.median(neigh) if len(neigh) else 0
    if hd[k] > max(0.30, base * 4 + 0.12) and ad[k] > 12 and k - cuts[-1] >= 6:
        cuts.append(k)
shots = []
for a, b in zip(cuts, cuts[1:] + [len(rows)]):
    seg = rows[a:b]
    mags = np.array([s['flow_mag'] for s in seg[1:]] or [0])
    dxs = np.array([s['flow_dx'] for s in seg[1:]] or [0])
    dys = np.array([s['flow_dy'] for s in seg[1:]] or [0])
    divs = np.array([s['flow_div'] for s in seg[1:]] or [0])
    dups = np.array([s['dup'] for s in seg[1:]] or [0])
    shots.append(dict(start_f=a, end_f=b - 1, start=round(a / fps, 3), end=round(b / fps, 3),
                      dur=round((b - a) / fps, 3), mean_flow=round(float(mags.mean()), 3),
                      cum_dx=round(float(dxs.sum()), 1), cum_dy=round(float(dys.sum()), 1),
                      mean_div=round(float(divs.mean()), 4), dup_frac=round(float(dups.mean()), 3),
                      luma=round(float(np.mean([s['luma'] for s in seg])), 1),
                      sat=round(float(np.mean([s['sat'] for s in seg])), 1),
                      cut_strength=round(float(hd[a]), 3)))
json.dump(dict(alias=alias, src=os.path.basename(src), fps=fps, frames=len(rows), shots=shots),
          open(os.path.join(outdir, f'{alias}_shots.json'), 'w'), indent=1)
print(alias, 'frames', len(rows), 'shots', len(shots),
      'median shot', round(float(np.median([s['dur'] for s in shots])), 2),
      'dup frac', round(float(np.mean([r_['dup'] for r_ in rows])), 3))
