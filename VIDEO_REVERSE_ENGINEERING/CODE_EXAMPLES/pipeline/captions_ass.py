#!/usr/bin/env python3
"""
captions_ass.py — RECONSTRUCTED word-by-word "pop" captions (the caption style of all 7 videos).

Observed (frame-by-frame strips, KEYFRAMES/, ANALYSIS_DATA/*_captions.json):
  * exactly ONE word on screen at a time, centred, at 58–76 % of frame height (varies by channel)
  * fill: yellow (#F2F21A-ish: V1, V2, V5) or white (V3, V4, V6) or white UPPERCASE with
    per-keyword colour (red/blue/yellow gradient words: V7); thick black outline + soft shadow
  * "pop" entrance: the word appears small and scales up past 100 % then settles in ~3 frames
    (V1 'supposed', V5 "he's"/'forty-one', V7 'OPENED')
  * word boundaries come from the voice-over word timestamps (caption leads/lags voice by tens of ms)

Input : Whisper-style JSON {"segments":[{"words":[{"w","s","e"}]}]} (see ANALYSIS_DATA/*_transcript.json)
Output: .ass subtitle file to burn with:  ffmpeg -i in.mp4 -vf "ass=captions.ass" out.mp4

Usage: captions_ass.py words.json out.ass [--style yellow|white|upper] [--y 0.66] [--lead-ms 0]
"""
import argparse, json

STYLES = {
    #            primary (&HAABBGGRR)  outline     font                bold upper
    'yellow': dict(primary='&H0019F2F2', outline='&H00000000', font='Liberation Sans', upper=False),
    'white':  dict(primary='&H00FFFFFF', outline='&H00000000', font='Liberation Sans', upper=False),
    'upper':  dict(primary='&H00FFFFFF', outline='&H00101010', font='Liberation Sans', upper=True),
}
# words that get an accent colour in the "upper" style (V7 colours nouns/verbs of the hook)
ACCENT = {'red': '&H003A3AFF', 'blue': '&H00FFB04A', 'yellow': '&H0010D8FF'}


def ts(t: float) -> str:
    t = max(0.0, t)
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def build(words, style='yellow', y=0.66, W=576, H=1024, lead_ms=0, pop_ms=100, accents=None, min_dur=0.12):
    st = STYLES[style]
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Pop,{st['font']},{int(H * 0.058)},{st['primary']},&H000000FF,{st['outline']},&H96000000,-1,0,0,0,100,100,0,0,1,{max(3, int(H * 0.006))},{max(1, int(H * 0.003))},5,20,20,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    x, yy = W // 2, int(H * y)
    for i, w in enumerate(words):
        start = w['s'] - lead_ms / 1000
        # each word stays until the next one starts (no gaps -> no flicker), min 4 frames
        end = max(words[i + 1]['s'] - lead_ms / 1000 if i + 1 < len(words) else w['e'] + 0.3, start + min_dur)
        text = w['w'].strip()
        if st['upper']: text = text.upper()
        colour = ''
        if accents and w['w'].lower().strip('.,!?') in accents:
            colour = r'\1c' + ACCENT[accents[w['w'].lower().strip('.,!?')]]
        # pop: 70% -> 112% in pop_ms, then 112% -> 100% in the next pop_ms (overshoot + settle)
        p = pop_ms
        anim = (rf"{{\an5\pos({x},{yy})\fscx70\fscy70{colour}"
                rf"\t(0,{p},\fscx112\fscy112)\t({p},{2 * p},\fscx100\fscy100)}}")
        lines.append(f"Dialogue: 0,{ts(start)},{ts(end)},Pop,,0,0,0,,{anim}{text}")
    return head + "\n".join(lines) + "\n"


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('words_json'); ap.add_argument('out_ass')
    ap.add_argument('--style', default='yellow', choices=STYLES); ap.add_argument('--y', type=float, default=0.66)
    ap.add_argument('--lead-ms', type=float, default=0); ap.add_argument('--w', type=int, default=576); ap.add_argument('--h', type=int, default=1024)
    a = ap.parse_args()
    d = json.load(open(a.words_json))
    words = [w for s in d['segments'] for w in s['words']]
    open(a.out_ass, 'w').write(build(words, a.style, a.y, a.w, a.h, a.lead_ms))
    print(f"{len(words)} words -> {a.out_ass}")
