#!/usr/bin/env python3
"""
shot_planner.py — RECONSTRUCTED editorial logic: voice-over word timings -> shot list.

Rules derived from the measurements (ANALYSIS_DATA/*_audio.json, *_shots.json):
  * V1/V5/V7: 80–85 % of cuts fall within 100 ms of a word onset; the cut lands ~20–30 ms
    BEFORE the word (median signed offset -20…-27 ms) => "cut on the word, image first".
  * 50–72 % of cuts are within 150 ms of a SENTENCE start => one sentence ≈ one or two shots.
  * Median shot length 1.35–2.5 s, ~5–8 spoken words per shot; long sentences are split
    at a word boundary once the shot exceeds MAX_SHOT.
  * The end of the narration is followed by a ~4 s outro (the TikTok end card in the downloads).

Output: JSON list of {start, end, words, sentence_idx, size, move} that a renderer (Three.js
CameraDirector, Roblox CinematicDirector, Blender script) consumes.
Usage: shot_planner.py words.json shots.json [--fps 30] [--max 2.6] [--lead-ms 25]
"""
import argparse, json, re

SIZES = ['wide', 'medium', 'close']          # rotation of shot sizes avoids jump cuts
MOVES = ['push_in', 'push_in', 'slow_drift', 'push_in', 'static', 'pull_out']  # weighted like the corpus


def plan(segments, fps=30, max_shot=2.6, min_shot=0.6, lead_ms=25):
    words = []
    for si, s in enumerate(segments):
        for w in s['words']:
            words.append(dict(w=w['w'], s=w['s'], e=w['e'], si=si))
    q = lambda t: round(round(t * fps) / fps, 4)      # snap to frame grid
    cuts = [0.0]
    last_si = 0
    for w in words[1:]:
        t = max(0.0, w['s'] - lead_ms / 1000)
        new_sentence = w['si'] != last_si
        too_long = t - cuts[-1] > max_shot
        # hard rule: new sentence => new shot; soft rule: split long shots on a word boundary
        if (new_sentence or too_long) and t - cuts[-1] >= min_shot:
            cuts.append(q(t))
        last_si = w['si']
    end = q(words[-1]['e'] + 0.25)
    shots = []
    for i, c in enumerate(cuts):
        e = cuts[i + 1] if i + 1 < len(cuts) else end
        ws = [w['w'] for w in words if c <= w['s'] - lead_ms / 1000 < e]
        # emphasis heuristics: numbers, exclamations and emotional words -> close-ups
        txt = ' '.join(ws).lower()
        size = 'close' if re.search(r"\d|!|cried|scream|terrified|gone|dead|why|whisper", txt) else SIZES[i % 3]
        shots.append(dict(start=c, end=e, dur=round(e - c, 3), words=ws, size=size, move=MOVES[i % len(MOVES)]))
    return shots


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('words_json'); ap.add_argument('out_json')
    ap.add_argument('--fps', type=int, default=30); ap.add_argument('--max', type=float, default=2.6)
    ap.add_argument('--lead-ms', type=float, default=25)
    a = ap.parse_args()
    segs = json.load(open(a.words_json))['segments']
    shots = plan(segs, a.fps, a.max, lead_ms=a.lead_ms)
    json.dump(shots, open(a.out_json, 'w'), indent=1)
    durs = sorted(s['dur'] for s in shots)
    print(f"{len(shots)} shots, median {durs[len(durs) // 2]:.2f}s")
