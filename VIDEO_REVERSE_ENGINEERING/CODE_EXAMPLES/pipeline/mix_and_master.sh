#!/usr/bin/env bash
# =====================================================================================
# mix_and_master.sh — RECONSTRUCTED audio assembly + final encode.
# Measured targets (ANALYSIS_DATA/*_audio.json, ebur128):
#   integrated loudness -13.7 … -14.7 LUFS for 5 of 7 videos (V1, V5 ≈ -19 LUFS), LRA 1.5–3.6 LU
#   (V3 9.6 LU), voice centred (L/R correlation 0.84–0.99), music bed 3–11 dB under the voice,
#   bed switches at the story's turning point (V6 +27 dB low-band at 60.9 s, V7 a cappella
#   lullaby 115–124 s then a fuller bed), AAC-LC 44.1 kHz stereo 128 kb/s.
# Usage: mix_and_master.sh video_silent.mp4 voice.wav music.wav captions.ass out.mp4
# =====================================================================================
set -euo pipefail
V="$1"; VOICE="$2"; MUSIC="$3"; ASS="$4"; OUT="$5"
ffmpeg -v error -y -i "$V" -i "$VOICE" -i "$MUSIC" -filter_complex "
  [1:a]aresample=44100,highpass=f=80,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,asplit=2[vo][sc];
  [2:a]aresample=44100,volume=-6dB[mus];
  [mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[ducked];
  [vo][ducked]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=4[aout];
  [0:v]ass='${ASS}'[vout]" \
  -map "[vout]" -map "[aout]" -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
  -c:a aac -b:a 128k -ar 44100 -ac 2 -movflags +faststart "$OUT"
echo "wrote $OUT"
