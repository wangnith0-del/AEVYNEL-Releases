#!/usr/bin/env python3
"""OCR the burned-in word-by-word captions (every 2nd frame = 15 Hz) and align them to the
Whisper word timestamps to measure caption/voice synchronisation.
Usage: caption_ocr.py <video> <alias> <datadir> <band_center_y_px_of_1024> [max_seconds]"""
import sys, json, re, difflib, subprocess
import cv2, numpy as np
src, alias, dd, yc = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
max_s = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9   # optional: only the first max_s seconds
cap = cv2.VideoCapture(src); fps = cap.get(cv2.CAP_PROP_FPS)
import pytesseract
seq = []; i = 0; prev_small = None
while True:
    ok, f = cap.read()
    if not ok or i / fps > max_s: break
    if i % 2 == 0:
        crop = f[max(0, yc - 48):yc + 48, 40:536]
        g = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        # caption glyphs are bright (white or yellow fill): V high, inside a dark outline
        v = g[..., 2]; s = g[..., 1]
        fill = ((v > 200) & ((s < 60) | ((g[..., 0] > 20) & (g[..., 0] < 40)))).astype(np.uint8) * 255
        dark = (v < 60).astype(np.uint8)
        near_dark = cv2.dilate(dark, np.ones((7, 7), np.uint8)) > 0
        txt_mask = cv2.bitwise_and(fill, fill, mask=near_dark.astype(np.uint8))
        txt_mask = cv2.morphologyEx(txt_mask, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
        # only OCR when the caption mask changed (a word stays ~5 samples): ~5x fewer tesseract calls
        small = cv2.resize(txt_mask, (124, 24), interpolation=cv2.INTER_AREA) > 60
        if txt_mask.sum() < 255 * 40: seq.append((round(i / fps, 3), '')); prev_small = small; i += 1; continue
        if prev_small is not None and (small ^ prev_small).mean() < 0.04 and seq:
            seq.append((round(i / fps, 3), seq[-1][1])); prev_small = small; i += 1; continue
        prev_small = small
        img = 255 - cv2.resize(txt_mask, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
        t = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$').strip()
        seq.append((round(i / fps, 3), re.sub(r'[^a-z0-9$]', '', t.lower())))
    i += 1
# collapse into caption events
events = []
for t, w in seq:
    if not w or len(w) < 1: 
        if events and events[-1]['w'] is not None: events.append(dict(t=t, w=None))
        continue
    if events and events[-1]['w'] == w: continue
    events.append(dict(t=t, w=w))
caps = [e for e in events if e['w']]
tr = json.load(open(f'{dd}/{alias}_transcript.json'))
words = [dict(w=re.sub(r'[^a-z0-9$]', '', x['w'].lower()), s=x['s']) for s in tr['segments'] for x in s['words'] if x['s'] <= max_s]
A = [c['w'] for c in caps]; B = [w['w'] for w in words]
sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
offs = []
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        offs.append(caps[blk.a + k]['t'] - words[blk.b + k]['s'])
offs = np.array(offs)
res = dict(alias=alias, ocr_samples=len(seq), caption_events=len(caps), matched_words=int(len(offs)),
           whisper_words=len(words),
           match_rate_pct=round(100 * len(offs) / max(1, len(words)), 1),
           caption_minus_voice_ms_median=round(float(np.median(offs)) * 1000) if len(offs) else None,
           caption_minus_voice_ms_p10_p90=[round(float(np.percentile(offs, 10)) * 1000), round(float(np.percentile(offs, 90)) * 1000)] if len(offs) else None,
           multiword_caption_events=sum(1 for c in caps if len(c['w']) > 14),
           first_captions=[c for c in caps[:25]])
json.dump(res, open(f'{dd}/{alias}_captions.json', 'w'), indent=1)
print(alias, {k: v for k, v in res.items() if k != 'first_captions'})
