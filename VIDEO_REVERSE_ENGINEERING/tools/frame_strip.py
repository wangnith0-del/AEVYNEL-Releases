#!/usr/bin/env python3
"""Frame-by-frame strip: N consecutive frames (step s) from t0, labelled with frame index. Usage: frame_strip.py video t0 n step out.jpg"""
import sys, cv2, numpy as np
src, t0, n, step, out = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS); f0 = int(round(t0 * fps))
tiles = []
for k in range(n):
    cap.set(cv2.CAP_PROP_POS_FRAMES, f0 + k * step); ok, fr = cap.read()
    if not ok: break
    t = cv2.resize(fr, (216, 384)); cv2.putText(t, f"f{f0 + k * step} {(f0 + k * step) / fps:.2f}s", (4, 18), 0, 0.5, (0, 0, 255), 2)
    tiles.append(t)
cols = 6
while len(tiles) % cols: tiles.append(np.zeros_like(tiles[0]))
cv2.imwrite(out, np.vstack([np.hstack(tiles[i:i + cols]) for i in range(0, len(tiles), cols)]), [cv2.IMWRITE_JPEG_QUALITY, 85])
