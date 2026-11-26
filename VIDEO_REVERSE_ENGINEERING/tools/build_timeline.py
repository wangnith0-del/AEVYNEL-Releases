#!/usr/bin/env python3
"""Generate the per-shot timeline tables (03_COMPLETE_TIMELINE.md body) from measured data.
Usage: build_timeline.py <datadir> > timeline_tables.md"""
import sys, json, glob, os
dd = sys.argv[1]
def fmt(t): m, s = divmod(t, 60); return f"{int(m):02d}:{s:05.2f}"
for a in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']:
    sh = json.load(open(f'{dd}/{a}_shots.json')); cam = {c['shot']: c for c in json.load(open(f'{dd}/{a}_camera.json'))['shots']}
    zf = {z['shot']: z for z in json.load(open(f'{dd}/{a}_zoom_forensics.json'))['shots']}
    tr = json.load(open(f'{dd}/{a}_transcript.json')); words = [w for s in tr['segments'] for w in s['words']]
    kf = sorted(glob.glob(f'KEYFRAMES/{a}/*.jpg'))
    print(f"\n### {a} — `{sh['src']}` — {sh['frames']} frames, {len(sh['shots'])} shots\n")
    print("| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for n, s in enumerate(sh['shots']):
        ws = ' '.join(w['w'] for w in words if s['start'] - 0.05 <= w['s'] < s['end'] - 0.05)
        if len(ws) > 90: ws = ws[:87] + '…'
        c = cam.get(n, {}); z = zf.get(n)
        zv = '' if not z else ('3D' if z['verdict'].startswith('parallax') else '2D' if z['verdict'].startswith('planar') else '≈static')
        k = next((os.path.basename(x) for x in kf if f'_shot{n:03d}_' in x), '')
        if not ws and n == len(sh['shots']) - 1: ws = '*(TikTok end card)*'
        print(f"| {n} | {fmt(s['start'])} | {fmt(s['end'])} | {s['dur']:.2f} | {ws.replace('|', '/')} | {c.get('move', '')} | {c.get('ease', '')} | {zv} | {s['luma']:.0f} | {s['sat']:.0f} | [img](KEYFRAMES/{a}/{k}) |")
