#!/usr/bin/env python3
"""Second pass on <alias>_frames.csv + shots.json:
 - per-shot camera move classification from optical flow (static / pan / tilt / push-in / pull-out / handheld)
 - easing profile of the move (linear vs ease-in-out vs ease-out) from the speed curve
 - jitter (high-frequency component of global flow -> shake / handheld noise)
 - flash frames (luma spikes) and dissolves (cuts spread over >1 frame)
Usage: camera_motion.py <datadir> <alias>"""
import sys, json, csv
import numpy as np
dd, alias = sys.argv[1:3]
rows = list(csv.DictReader(open(f'{dd}/{alias}_frames.csv')))
F = {k: np.array([float(r[k]) for r in rows]) for k in rows[0]}
shots = json.load(open(f'{dd}/{alias}_shots.json'))['shots']
res = []
for n, s in enumerate(shots):
    a, b = s['start_f'] + 1, s['end_f'] + 1
    if b - a < 6:
        res.append(dict(shot=n, move='too_short')); continue
    dx, dy, dv, mg = F['flow_dx'][a:b], F['flow_dy'][a:b], F['flow_div'][a:b], F['flow_mag'][a:b]
    # global speed (px/frame at 144x256) ; scale x4 for native
    gl = np.sqrt(dx ** 2 + dy ** 2)
    k = 5
    smooth_dx = np.convolve(dx, np.ones(k) / k, 'same'); smooth_dy = np.convolve(dy, np.ones(k) / k, 'same')
    jitter = float(np.sqrt(((dx - smooth_dx)[k:-k] ** 2 + (dy - smooth_dy)[k:-k] ** 2).mean())) if len(dx) > 2 * k else 0
    mdx, mdy, mdv, mmg = dx.mean(), dy.mean(), dv.mean(), mg.mean()
    if mmg < 0.15: move = 'static'
    elif abs(mdv) > 0.12 and abs(mdv) > 0.6 * max(abs(mdx), abs(mdy)): move = 'push_in' if mdv > 0 else 'pull_out'
    elif abs(mdx) > 0.25 and abs(mdx) >= abs(mdy): move = 'pan_or_track_' + ('left' if mdx > 0 else 'right')  # content moves right => camera moves left
    elif abs(mdy) > 0.25: move = 'tilt_or_crane_' + ('up' if mdy > 0 else 'down')
    elif mmg > 0.6 and abs(mdx) < 0.25 and abs(mdy) < 0.25 and abs(mdv) < 0.12: move = 'subject_motion_or_orbit'
    else: move = 'slow_drift'
    # easing: speed curve of the dominant component
    sp = np.abs(np.convolve(dv if move.startswith(('push', 'pull')) else gl, np.ones(5) / 5, 'valid'))
    ease = 'n/a'
    if move not in ('static',) and len(sp) >= 9:
        t3 = len(sp) // 3
        first, mid, last = sp[:t3].mean(), sp[t3:2 * t3].mean(), sp[2 * t3:].mean()
        if mid > 1.25 * first and mid > 1.25 * last: ease = 'ease_in_out'
        elif first > 1.3 * last: ease = 'ease_out (fast start, decelerating)'
        elif last > 1.3 * first: ease = 'ease_in (accelerating)'
        else: ease = 'linear/constant'
    res.append(dict(shot=n, start=s['start'], dur=s['dur'], move=move, ease=ease,
                    mean_dx=round(float(mdx) * 4, 2), mean_dy=round(float(mdy) * 4, 2),
                    zoom_rate=round(float(mdv) * 4, 3), mean_flow=round(float(mmg) * 4, 2),
                    jitter_px=round(jitter * 4, 3)))
# flashes: luma spike frames
lum = F['luma']; flashes = [round(F['t'][i], 2) for i in range(1, len(lum) - 1) if lum[i] > 215 and lum[i] - min(lum[i - 1], lum[i + 1]) > 0 or (lum[i] - np.median(lum[max(0, i - 15):i + 15]) > 60)]
# dissolve detection: frames with moderate hist distance on several consecutive frames
hd = F['hist_d']; diss = []
i = 1
while i < len(hd) - 4:
    if all(0.12 < hd[j] < 0.5 for j in range(i, i + 4)) and F['absdiff'][i:i + 4].mean() > 4:
        diss.append(round(F['t'][i], 2)); i += 10
    else: i += 1
moves = {}
for r in res: moves[r['move'].split('_')[0] if r['move'].startswith('pan') or r['move'].startswith('tilt') else r['move']] = moves.get(r['move'].split('_')[0] if r['move'].startswith(('pan', 'tilt')) else r['move'], 0) + 1
eases = {}
for r in res:
    if r.get('ease', 'n/a') != 'n/a': eases[r['ease']] = eases.get(r['ease'], 0) + 1
summary = dict(alias=alias, move_counts=moves, ease_counts=eases,
               median_jitter_px=round(float(np.median([r['jitter_px'] for r in res if 'jitter_px' in r])), 3),
               flash_times=sorted(set(flashes))[:60], dissolve_candidates=diss[:40])
json.dump(dict(summary=summary, shots=res), open(f'{dd}/{alias}_camera.json', 'w'), indent=1)
print(json.dumps(summary))
