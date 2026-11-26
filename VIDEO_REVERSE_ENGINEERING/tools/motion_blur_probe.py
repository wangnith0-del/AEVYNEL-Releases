#!/usr/bin/env python3
"""Motion-blur probe. Real render motion blur => local sharpness drops where local motion is high.
For frame pairs, compute per-block (16x16 @288x512) optical-flow magnitude and Laplacian variance;
report Spearman correlation between block motion and block sharpness (normalised by the same block
in the shot's least-moving frame is too costly; we use within-frame ranking instead), plus the median
sharpness ratio of fast-moving blocks (>3 px/frame) vs static blocks with similar texture.
Usage: motion_blur_probe.py video alias datadir"""
import sys, json, cv2, numpy as np
from scipy.stats import spearmanr
src, alias, dd = sys.argv[1:4]
cap = cv2.VideoCapture(src); prev = None; i = 0; ratios = []; rhos = []
while True:
    ok, f = cap.read()
    if not ok: break
    i += 1
    if i % 3: prev = None if i % 3 == 1 else prev; 
    g = cv2.cvtColor(cv2.resize(f, (288, 512)), cv2.COLOR_BGR2GRAY)
    if i % 3 == 2: prev = g; continue
    if i % 3 != 0 or prev is None: continue
    flow = cv2.calcOpticalFlowFarneback(prev, g, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag = np.linalg.norm(flow, axis=2)
    lap = cv2.Laplacian(g, cv2.CV_32F)
    gx = cv2.Sobel(g, cv2.CV_32F, 1, 0); gy = cv2.Sobel(g, cv2.CV_32F, 0, 1)
    B = 16; m = []; s = []; e = []
    for y in range(0, 512 - B, B):
        if 190 <= y <= 340: continue  # skip caption band
        for x in range(0, 288 - B, B):
            m.append(mag[y:y + B, x:x + B].mean()); s.append(lap[y:y + B, x:x + B].var())
            e.append(np.abs(gx[y:y + B, x:x + B]).mean() + np.abs(gy[y:y + B, x:x + B]).mean())
    m, s, e = map(np.array, (m, s, e))
    # sharpness relative to edge energy (blur lowers high-freq Laplacian more than 1st-order gradient)
    rel = s / (e ** 2 + 1)
    fast, slow = (m > 3) & (e > 8), (m < 0.5) & (e > 8)
    if fast.sum() >= 5 and slow.sum() >= 5:
        ratios.append(np.median(rel[fast]) / np.median(rel[slow]))
        r, _ = spearmanr(m[e > 8], rel[e > 8]); rhos.append(r)
res = dict(alias=alias, frames_used=len(ratios),
           fast_vs_static_sharpness_ratio_median=round(float(np.median(ratios)), 3) if ratios else None,
           spearman_motion_vs_sharpness_median=round(float(np.nanmedian(rhos)), 3) if rhos else None)
json.dump(res, open(f'{dd}/{alias}_motionblur.json', 'w'), indent=1); print(res)
