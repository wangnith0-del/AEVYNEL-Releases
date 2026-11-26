#!/usr/bin/env python3
"""Audio analysis: envelope, silences, stereo width, spectral profile, voice-vs-bed estimate,
and cut/word synchronisation. Usage: audio_analysis.py <stereo44k.wav> <alias> <datadir>"""
import sys, json, wave
import numpy as np
from scipy import signal
wav, alias, dd = sys.argv[1:4]
w = wave.open(wav); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32).reshape(-1, 2) / 32768
L, R = x[:, 0], x[:, 1]; M = (L + R) / 2; Sd = (L - R) / 2
hop = sr // 100  # 10 ms
def rms(v): n = len(v) // hop; return np.sqrt((v[:n * hop].reshape(n, hop) ** 2).mean(1) + 1e-12)
env = 20 * np.log10(rms(M)); envS = 20 * np.log10(rms(Sd))
# band energies: voice band 300-3400 vs low (<150) vs high (>6k)
f, t, Z = signal.stft(M, sr, nperseg=2048, noverlap=2048 - 441)
P = np.abs(Z) ** 2
def band(a, b): return 10 * np.log10(P[(f >= a) & (f < b)].sum(0) + 1e-12)
low, voice, high = band(20, 150), band(300, 3400), band(6000, 16000)
tr = json.load(open(f'{dd}/{alias}_transcript.json'))
words = [w_ for s in tr['segments'] for w_ in s['words']]
ws = np.array([w_['s'] for w_ in words]); we = np.array([w_['e'] for w_ in words])
speech_mask = np.zeros(len(env), bool)
for s_, e_ in zip(ws, we): speech_mask[int(s_ * 100):int(e_ * 100) + 1] = True
speech_mask = speech_mask[:len(env)]
gap_floor = env[~speech_mask & (env > -90)]
# pauses between words
gaps = ws[1:] - we[:-1]
shots = json.load(open(f'{dd}/{alias}_shots.json'))['shots']
cuts = np.array([s['start'] for s in shots[1:]])
def nearest(a, ref): return np.array([ref[np.argmin(np.abs(ref - v))] - v for v in a])
d_word = nearest(cuts, ws)
seg_starts = np.array([s['start'] for s in tr['segments']])
d_seg = nearest(cuts, seg_starts)
speech_end = float(we.max())
out = dict(alias=alias,
    duration=round(len(M) / sr, 2),
    integrated_rms_dbfs=round(float(20 * np.log10(np.sqrt((M ** 2).mean()))), 2),
    peak_dbfs=round(float(20 * np.log10(np.abs(x).max() + 1e-9)), 2),
    stereo_side_minus_mid_db=round(float(np.median(envS - env)), 1),
    lr_correlation=round(float(np.corrcoef(L, R)[0, 1]), 4),
    speech_level_median_db=round(float(np.median(env[speech_mask])), 1),
    non_speech_level_median_db=round(float(np.median(gap_floor)) if len(gap_floor) else None, 1),
    frames_below_m60db_pct=round(float((env < -60).mean() * 100), 2),
    words=len(words), words_per_min=round(len(words) / (speech_end / 60), 1),
    speech_end_s=round(speech_end, 2),
    median_word_gap_s=round(float(np.median(gaps)), 3),
    pauses_over_300ms=int((gaps > 0.3).sum()), longest_pause_s=round(float(gaps.max()), 2),
    low_band_minus_voice_db=round(float(np.median(low - voice)), 1),
    high_band_minus_voice_db=round(float(np.median(high - voice)), 1),
    cuts=len(cuts),
    cut_to_nearest_word_start_ms_median=round(float(np.median(np.abs(d_word)) * 1000), 0),
    cuts_within_100ms_of_word_start_pct=round(float((np.abs(d_word) < 0.1).mean() * 100), 1),
    cuts_within_150ms_of_sentence_start_pct=round(float((np.abs(d_seg) < 0.15).mean() * 100), 1),
    cut_minus_word_signed_ms_median=round(float(np.median(-d_word)) * 1000, 0),
    avg_shot_s=round(float(np.mean([s['dur'] for s in shots])), 2),
    words_per_shot=round(len(words) / len(shots), 2))
json.dump(out, open(f'{dd}/{alias}_audio.json', 'w'), indent=1)
np.savez_compressed(f'{dd}/{alias}_envelope.npz', env_db=env.astype(np.float16), side_db=envS.astype(np.float16), low=low.astype(np.float16), voice=voice.astype(np.float16), high=high.astype(np.float16))
print(json.dumps(out))
