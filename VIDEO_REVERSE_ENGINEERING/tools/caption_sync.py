#!/usr/bin/env python3
"""Caption/voice sync without OCR: detect caption-change onsets at full 30 fps from the binary
caption-glyph mask (bright fill adjacent to dark outline, in the caption band), then measure the
offset of each onset to the nearest Whisper word start.
Usage: caption_sync.py video alias datadir band_center_y"""
import sys, json, cv2, numpy as np
src, alias, dd, yc = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS)
prev = None; on = []; i = 0; areas = []
while True:
    ok, f = cap.read()
    if not ok: break
    crop = f[max(0, yc - 48):yc + 48, 40:536]
    g = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV); v, s, h = g[..., 2], g[..., 1], g[..., 0]
    fill = (v > 200) & ((s < 60) | ((h > 20) & (h < 40)))
    near_dark = cv2.dilate((v < 60).astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
    m = cv2.resize((fill & near_dark).astype(np.uint8) * 255, (124, 24), interpolation=cv2.INTER_AREA) > 60
    areas.append(int(m.sum()))
    if prev is not None:
        union = (m | prev).sum()
        if union > 15 and (m ^ prev).sum() / union > 0.5: on.append(i / fps)
    prev = m; i += 1
on = np.array(on)
# merge onsets closer than 3 frames (pop animation scales the word over ~3 frames)
merged = [] 
for t in on:
    if not merged or t - merged[-1] > 0.1: merged.append(t)
on = np.array(merged)
tr = json.load(open(f'{dd}/{alias}_transcript.json'))
ws = np.array([w['s'] for s in tr['segments'] for w in s['words']])
d = np.array([on_ - ws[np.argmin(np.abs(ws - on_))] for on_ in on])
good = d[np.abs(d) < 0.25]
res = dict(alias=alias, caption_onsets=int(len(on)), whisper_words=int(len(ws)),
           onsets_matched_within_250ms=int(len(good)), match_pct=round(100 * len(good) / max(1, len(on)), 1),
           caption_minus_voice_ms_median=round(float(np.median(good)) * 1000) if len(good) else None,
           caption_minus_voice_ms_p25_p75=[round(float(np.percentile(good, 25)) * 1000), round(float(np.percentile(good, 75)) * 1000)] if len(good) else None,
           words_covered_pct=round(100 * np.mean([np.min(np.abs(on - w)) < 0.25 for w in ws]), 1) if len(on) else 0)
json.dump(res, open(f'{dd}/{alias}_caption_sync.json', 'w'), indent=1); print(res)
