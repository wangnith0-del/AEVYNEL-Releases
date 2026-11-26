#!/usr/bin/env python3
"""Colour-grade / post-process fingerprint, sampled at 3 fps over the full video (end card excluded).
 - vignette: median ratio corner-luma / centre-luma (constant <0.85 across varied content => applied vignette)
 - warmth: median (R-B) ; saturation ; contrast (luma std) ; black/white clipping %
 - sharpening halo index: ratio of high-pass energy (3x3) to mid-pass energy (9x9 DoG)
 - grain: residual noise std in flat regions after 5x5 median
Usage: grade_analysis.py video alias datadir end_card_seconds"""
import sys, json, cv2, numpy as np
src, alias, dd, ec = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4])
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS); n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
last = n - int(ec * fps); V = []; W = []; S = []; C = []; CL = []; WH = []; SH = []; GR = []
for i in range(0, last, int(fps // 3)):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i); ok, f = cap.read()
    if not ok: break
    f = cv2.resize(f, (288, 512)); g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32)
    h, w = g.shape; cy, cx = h // 2, w // 2
    centre = g[cy - 60:cy + 60, cx - 40:cx + 40].mean()
    corners = np.mean([g[:50, :40].mean(), g[:50, -40:].mean(), g[-50:, :40].mean(), g[-50:, -40:].mean()])
    V.append(corners / (centre + 1)); b_, g_, r_ = [f[..., k].astype(float).mean() for k in range(3)]
    W.append(r_ - b_); S.append(cv2.cvtColor(f, cv2.COLOR_BGR2HSV)[..., 1].mean()); C.append(g.std())
    CL.append((g < 8).mean() * 100); WH.append((g > 247).mean() * 100)
    hp = np.abs(g - cv2.GaussianBlur(g, (3, 3), 0)).mean(); mp = np.abs(cv2.GaussianBlur(g, (3, 3), 0) - cv2.GaussianBlur(g, (9, 9), 0)).mean()
    SH.append(hp / (mp + 1e-3))
    med = cv2.medianBlur(g.astype(np.uint8), 5).astype(np.float32); res = g - med
    flat = cv2.Laplacian(med, cv2.CV_32F); m = np.abs(flat) < 2
    if m.mean() > 0.05: GR.append(res[m].std())
q = lambda a: [round(float(np.percentile(a, p)), 3) for p in (10, 50, 90)]
out = dict(alias=alias, samples=len(V), vignette_corner_over_centre_p10_50_90=q(V), warmth_R_minus_B=q(W),
           saturation=q(S), contrast_luma_std=q(C), pct_crushed_blacks=q(CL), pct_clipped_whites=q(WH),
           sharpen_index=q(SH), grain_std_flat=q(GR) if GR else None)
json.dump(out, open(f'{dd}/{alias}_grade.json', 'w'), indent=1); print(json.dumps(out))
