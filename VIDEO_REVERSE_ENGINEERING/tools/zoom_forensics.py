#!/usr/bin/env python3
"""Distinguish 2D digital zoom (editor keyframe / Ken Burns) from 3D camera dolly.
For each shot classified push_in/pull_out/slow_drift (>=0.8 s), track corners between two frames
8 frames apart (caption band + corners masked), fit a similarity transform with RANSAC.
 - 2D zoom: every point obeys one scale+translation -> high inlier ratio, tiny residual, no parallax
 - 3D dolly/orbit: depth-dependent motion -> lower inlier ratio, larger residual
Usage: zoom_forensics.py <video> <datadir> <alias>"""
import sys, json, cv2, numpy as np
src, dd, alias = sys.argv[1:4]
cam = json.load(open(f'{dd}/{alias}_camera.json'))['shots']
shots = json.load(open(f'{dd}/{alias}_shots.json'))['shots']
cap = cv2.VideoCapture(src)
def grab(i):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i); ok, f = cap.read()
    return cv2.cvtColor(cv2.resize(f, (288, 512)), cv2.COLOR_BGR2GRAY) if ok else None
mask = np.full((512, 288), 255, np.uint8)
mask[200:330, :] = 0            # caption band (varies by channel, covers 40-64% height)
mask[400:, 180:] = 0; mask[:80, :120] = 0; mask[230:290, :110] = 0  # TikTok watermark zones
mask[440:, :] = 0
out = []
for c in cam:
    if c.get('move') not in ('push_in', 'pull_out', 'slow_drift') or c.get('dur', 0) < 0.8: continue
    s = shots[c['shot']]; mid = (s['start_f'] + s['end_f']) // 2
    a, b = grab(mid - 4), grab(mid + 4)
    if a is None or b is None: continue
    p0 = cv2.goodFeaturesToTrack(a, 300, 0.01, 6, mask=mask)
    if p0 is None or len(p0) < 25: continue
    p1, st, _ = cv2.calcOpticalFlowPyrLK(a, b, p0, None)
    g0, g1 = p0[st == 1], p1[st == 1]
    if len(g0) < 25: continue
    M, inl = cv2.estimateAffinePartial2D(g0, g1, method=cv2.RANSAC, ransacReprojThreshold=0.6)
    if M is None: continue
    scale = float(np.sqrt(M[0, 0] ** 2 + M[1, 0] ** 2)); rot = float(np.degrees(np.arctan2(M[1, 0], M[0, 0])))
    pred = (g0 @ M[:, :2].T) + M[:, 2]
    resid = np.linalg.norm(pred - g1, axis=1)
    motion = np.linalg.norm(g1 - g0, axis=1)
    out.append(dict(shot=c['shot'], start=s['start'], move=c['move'], n=int(len(g0)),
                    inlier_ratio=round(float(inl.mean()), 3), scale_per_8f=round(scale, 4),
                    rot_deg=round(rot, 3), median_resid_px=round(float(np.median(resid)), 3),
                    median_motion_px=round(float(np.median(motion)), 3)))
def verdict(o):
    if abs(o['scale_per_8f'] - 1) < 0.002 and o['median_motion_px'] < 0.4: return 'near_static'
    if o['inlier_ratio'] > 0.85 and o['median_resid_px'] < 0.25: return 'planar_2D_transform (digital zoom/pan likely)'
    return 'parallax_3D (camera move in engine likely)'
for o in out: o['verdict'] = verdict(o)
cnt = {}
for o in out: cnt[o['verdict']] = cnt.get(o['verdict'], 0) + 1
json.dump(dict(alias=alias, counts=cnt, shots=out), open(f'{dd}/{alias}_zoom_forensics.json', 'w'), indent=1)
print(alias, cnt)
