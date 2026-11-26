# 10 — Audio et sound design

Données : `ANALYSIS_DATA/*_audio.json`, `*_transcript.json` (397–631 mots par vidéo, horodatés au mot), `*_spectrogram.png`, `music_bed_changes.json`, `voice_pitch_probe.json`, mesures EBU R128 (FFmpeg `ebur128`).

## 1. Mesures

| | V1 | V2 | V3 | V4 | V5 | V6 | V7 |
|---|---|---|---|---|---|---|---|
| Loudness intégrée | −19,1 LUFS | −14,4 | −14,2 | −13,7 | −19,6 | −14,7 | −13,7 |
| LRA | 3,2 LU | 2,7 | **9,6** | 1,5 | 3,0 | 3,6 | 2,1 |
| Débit de parole | 172 mots/min | 208 | 220 | **234** | 208 | 214 | **233** |
| Voix commence à | 0,00 s (toutes) |||||||
| Fin de la voix → fin du fichier | 4,4 s | 4,0 | 7,2 | 4,1 | 4,7 | 7,9 | 4,9 |
| Pauses > 300 ms | 45 | 23 | 68 | 11 | 26 | 58 | 41 |
| Pause la plus longue | 0,92 s | **3,10 s** | 0,98 | 0,58 | 0,64 | 0,70 | 0,90 |
| Niveau hors-parole vs parole | −8,9 dB | −6,4 | −11,8 | −8,6 | −10,2 | **−3,1** | −8,4 |
| Corrélation L/R | 0,96 | 0,88 | 0,99 | 0,99 | 0,98 | **0,84** | 0,98 |
| Coupes à < 100 ms d'un début de mot | 81 % | 29 % | 54 % | 61 % | 85 % | 11 % | 80 % |
| Décalage médian coupe − mot | −27 ms | −130 | −20 | −80 | −27 | −160 | −20 |

Notes : la narration conversationnelle « normale » est à 150–160 mots/min ; ici 172–234 → **débit très rapide** (voix accélérée ou écrite/jouée pour être rapide) **[CONFIRMÉ : débit ; HYPOTHÈSE : accélération en post]**. Les 4–8 s de fin incluent la carte de fin TikTok (jingle identique à −23 dB sur les 7 fichiers).

## 2. Structure des pistes

1. **Voix off** (narrateur à la 1re personne, centrée, compressée, dominante) — présente de la première à la dernière image de contenu.
2. **Répliques de personnages** : dites dans le flux de narration (« Eli, I'm so tired », « Sure, sweetheart », « Wake up! »). Hauteur médiane plus élevée pour les enfants (V7 Ava 261 Hz vs narrateur 192 Hz) → voix différente ou même voix transposée **[INDÉTERMINABLE : la mesure F0 est contaminée par la musique, voir 16]**.
3. **Bed musical** continu sous la voix, 3–12 dB en dessous ; **change aux pivots du récit** :
   * V6 : saut de +27 dB dans les graves à **60,9 s** (bed calme → nappe grave soutenue jusqu'à la fin) — juste avant « At four o'clock, Lily let go of my hand and ran » : la musique annonce la bascule ~2 s avant la phrase **[CONFIRMÉ : mesure + spectrogramme]**.
   * V7 : **115,6–124,2 s** la musique s'efface au profit d'une **berceuse chantée** (F0 médiane ≈ 557 Hz, 88 % voisé) — « la voix qui endort » est donnée à entendre ; puis bed plus plein (+29 dB graves à 124 s) pour la résolution **[CONFIRMÉ]**.
   * V3 : densification progressive des graves à partir de ~80 s (−52 → −38 dB), c.-à-d. à partir de la révélation (« But she wasn't looking at me »), d'où la LRA élevée (9,6 LU) **[CONFIRMÉ : mesure]**.
4. **SFX / gags vocaux** : V2 « huss huss » (3,1–4,6 s, puis la pause de 3,1 s à 60,4–63,5 s laissée au gag sonore, sous-titré « huss ») **[CONFIRMÉ : transcription + sous-titres]**. Les autres SFX (impacts, whoosh) sont faibles ou absents dans la mesure spectrale ; un inventaire SFX exhaustif n'est pas possible sans séparation de sources **[INDÉTERMINABLE au-delà des gags identifiés]**.
5. **Stéréo** : voix au centre ; V6 et V2 ont le bed le plus large (corrélation 0,84–0,88) → musique stéréo plus présente.

## 3. Synchronisation audio-visuelle

* **La voix est la piste maître** : les coupes tombent sur les débuts de mots (V1/V5/V7 : 80–85 % à < 100 ms) avec l'image **en avance de ~20–30 ms** (montage « image d'abord »). V2/V6 coupent plus librement, en moyenne 130–160 ms avant le mot (coupe sur l'inspiration / J-cut visuel).
* **Les sous-titres suivent chaque mot** : 92,5–100 % des mots prononcés ont une apparition de sous-titre à ±250 ms ; décalage médian sous-titre − voix : V1 +40, V2 +7, V3 0, V4 −40, V5 +20, V6 −53, V7 +27 ms (`ANALYSIS_DATA/*_caption_sync.json`, mesure à 30 fps sur toute la durée) → texte généré depuis les timestamps de mots **[CONFIRMÉ]**.
* **Les expressions suivent les mots-clés** (V7 « mouth » → bouche ouverte la même image).
* **La musique suit les actes** (changements de bed aux pivots).

## 4. Rôle perceptif du son

| Mécanisme | Effet |
|---|---|
| Débit 210–234 mots/min, pauses courtes (médiane ≈ 0 ms entre mots) | aucune « respiration » où décrocher ; densité d'information |
| Pause longue unique (V2 3,1 s) | gag/silence = ponctuation forte |
| Bascule de bed avant la phrase-pivot | le spectateur *sent* le tournant avant de le comprendre |
| Retrait de la musique (V7 berceuse) | focalisation totale sur un son diégétique clé |
| Loudness −14 LUFS, LRA faible | intelligible sur haut-parleur de téléphone, pas de variations à corriger |

## 5. Architecture de synchronisation réutilisable

```
script.txt ──TTS/enregistrement──► vo.wav ──Whisper (word_timestamps)──► words.json  (SOURCE DE VÉRITÉ)
                                                                           │
          ┌──────────────────────────┬────────────────────────────┬────────┴──────────────┐
          ▼                          ▼                            ▼                       ▼
 shot_planner.py (coupes)   captions_ass.py (texte)   events (visages, gestes)   cues musique (pivots)
          └──────────────────────────┴───────────── rendu (Three.js / Roblox / Blender) ───┘
                                                                           ▼
                        mix_and_master.sh : voix compressée + musique avec ducking sidechain
                        → loudnorm I=−14, TP=−1, LRA=4 → AAC 128 kb/s 44,1 kHz
```

Testé : `mix_and_master.sh` produit −14,0 LUFS mesuré (voir 16).

Paramètres de ducking recommandés (estimés pour obtenir les écarts mesurés de 3–12 dB) : `sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350`, bed à −6 dB avant compression.
