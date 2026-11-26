#!/usr/bin/env python3
"""Extract first/mid frame of every shot -> KEYFRAMES/<alias>/ and build labelled contact sheets."""
import sys, json, os, cv2, numpy as np
src, shots_json, outdir, sheetdir = sys.argv[1:5]
d = json.load(open(shots_json)); alias = d['alias']
os.makedirs(outdir, exist_ok=True); os.makedirs(sheetdir, exist_ok=True)
cap = cv2.VideoCapture(src)
tiles = []
for n, s in enumerate(d['shots']):
    mid = (s['start_f'] + s['end_f']) // 2
    cap.set(cv2.CAP_PROP_POS_FRAMES, mid); ok, fr = cap.read()
    if not ok: continue
    cv2.imwrite(f"{outdir}/{alias}_shot{n:03d}_{s['start']:07.2f}s.jpg", cv2.resize(fr, (288, 512)), [cv2.IMWRITE_JPEG_QUALITY, 80])
    t = cv2.resize(fr, (180, 320))
    cv2.rectangle(t, (0, 0), (180, 22), (0, 0, 0), -1)
    cv2.putText(t, f"#{n} {s['start']:.1f}-{s['end']:.1f}", (3, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    tiles.append(t)
cols, per = 8, 24
for p in range(0, len(tiles), per):
    chunk = tiles[p:p + per]
    while len(chunk) % cols: chunk.append(np.zeros_like(tiles[0]))
    rows = [np.hstack(chunk[r:r + cols]) for r in range(0, len(chunk), cols)]
    cv2.imwrite(f"{sheetdir}/{alias}_sheet{p // per:02d}.jpg", np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 82])
