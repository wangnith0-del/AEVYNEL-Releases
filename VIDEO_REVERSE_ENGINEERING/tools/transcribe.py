#!/usr/bin/env python3
"""Local word-level transcription (faster-whisper small.en, CPU int8). Usage: transcribe.py <wav> <alias> <outdir>"""
import sys, json, wave
import numpy as np
from faster_whisper import WhisperModel
wav, alias, out = sys.argv[1:4]
m = WhisperModel('small.en', device='cpu', compute_type='int8', cpu_threads=1)
w_=wave.open(wav); audio=np.frombuffer(w_.readframes(w_.getnframes()),np.int16).astype(np.float32)/32768
segs, info = m.transcribe(audio, word_timestamps=True, vad_filter=False, beam_size=5)
res = []
for s in segs:
    res.append(dict(start=round(s.start, 2), end=round(s.end, 2), text=s.text.strip(),
                    words=[dict(w=w.word.strip(), s=round(w.start, 2), e=round(w.end, 2), p=round(w.probability, 2)) for w in s.words]))
json.dump(dict(alias=alias, segments=res), open(f'{out}/{alias}_transcript.json', 'w'), indent=1)
with open(f'{out}/{alias}_transcript.txt', 'w') as f:
    for s in res: f.write(f"[{s['start']:7.2f}-{s['end']:7.2f}] {s['text']}\n")
print(alias, len(res), 'segments')
