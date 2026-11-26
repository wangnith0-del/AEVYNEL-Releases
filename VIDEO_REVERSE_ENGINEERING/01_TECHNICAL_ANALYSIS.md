# 01 — Analyse technique des fichiers vidéo

Légende de confiance utilisée dans tout le dossier : **[CONFIRMÉ]** vérifié dans les fichiers ou par mesure · **[FORTEMENT PROBABLE]** plusieurs indices concordants · **[HYPOTHÈSE]** plausible, invérifiable · **[INDÉTERMINABLE]** données insuffisantes.

## 1. Inventaire et alias

| Alias | Fichier fourni | SHA-256 (début) | Taille | Compte (filigrane TikTok visible) |
|---|---|---|---|---|
| V1 | `856391f0-v26044gc0000dc3vmpfog65mstlrss6g.mp4` | e190cd26… | 17,7 Mo | @jexario |
| V2 | `5bbdae42-v15044gf0000dc25vm7og65linhp7ks0.mp4` | b4896029… | 8,2 Mo | @pawranoid.pets |
| V3 | `6fbc8ec7-v26044gc0000dc1l1b7og65us58g66u0.mp4` | 1dd1cca9… | 17,6 Mo | @whatifstoriess_ |
| V4 | `ffad1ac0-v15044gf0000dc3d877og65umu2pe8vg.mp4` | 5e9fdc3c… | 27,0 Mo | @xxvideo.25 |
| V5 | `0863af51-v26044gc0000dc3kj67og65i4pmu3dkg.mp4` | 5dee0df4… | 29,4 Mo | @goopie.yt |
| V6 | `2f32ac23-v26044gc0000dbrq2fvog65vje5kn6j0.mp4` | 956137a5… | 13,3 Mo | @whatifstoriess_ |
| V7 | `47e73f86-v12025gd0000dc1k507og65j9la4m0a0.mp4` | 93bd32a1… | 15,6 Mo | @elii.rbl |

Aucun fichier source (projet, script, asset, configuration) n'a été fourni : seuls les 7 MP4 sont disponibles **[CONFIRMÉ]**. Les fichiers originaux n'ont jamais été modifiés (lecture seule ; toutes les extractions vont vers `KEYFRAMES/`, `ANALYSIS_DATA/` ou le scratchpad).

## 2. Caractéristiques des flux (ffprobe) **[CONFIRMÉ]**

| | V1 | V2 | V3 | V4 | V5 | V6 | V7 |
|---|---|---|---|---|---|---|---|
| Durée (s) | 143,000 | 74,867 | 138,801 | 130,520 | 119,767 | 124,100 | 167,207 |
| Images | 4290 | 2246 | 4163 | 3915 | 3592 | 3723 | 5016 |
| Résolution | 576×1024 | idem | idem | idem | idem | idem | idem |
| SAR / DAR | 1:1 / 9:16 | idem | idem | idem | idem | idem | idem |
| fps (r/avg) | 30/30 | 30/30 | 30/30 | 30/30 | 30/30 | 30/30 | 30/30 |
| Codec vidéo | H.264 High L3.1 | idem | idem | idem | idem | idem | idem |
| Débit vidéo (kb/s) | 853 | 737 | 876 | 1520 | 1829 | 721 | 610 |
| Pixel format | yuv420p | idem | idem | idem | idem | idem | idem |
| Couleur tagguée | BT.709 tv | non tagguée | non tagguée | BT.709 tv | BT.709 tv | non tagguée | non tagguée |
| Audio | AAC-LC 44,1 kHz stéréo 128 kb/s (toutes) |||||||
| Loudness intégrée (EBU R128) | −19,1 LUFS | −14,4 | −14,2 | −13,7 | −19,6 | −14,7 | −13,7 |
| LRA | 3,2 LU | 2,7 | 9,6 | 1,5 | 3,0 | 3,6 | 2,1 |
| Crête | 0,0 dBFS (toutes, limiteur/normalisation plateforme) |||||||

* **Framerate constant** : l'écart entre timestamps successifs est exactement 1/30 s sur 100 % des images des 7 fichiers (`ANALYSIS_DATA/*_gop.json`, champ `frame_dt_unique`) **[CONFIRMÉ]**.
* **Images dupliquées** (diff. max ≤ 2 niveaux) : 0,4–1,8 % seulement → la source a été produite/captée à ≥ 30 fps ; pas de rendu à 15/24 fps « étiré » **[CONFIRMÉ]**. Les rares doublons coïncident avec des plans fixes sur décor immobile.

## 3. Structure de compression **[CONFIRMÉ]**

| | I | P | B | GOP médian / max (s) | Coupes portant un I-frame |
|---|---|---|---|---|---|
| V1 | 50 | 1131 | 3109 | 2,53 / 6,23 | 91,5 % |
| V2 | 21 | 647 | 1578 | 3,13 / 6,77 | 47,6 % |
| V3 | 79 | 1118 | 2966 | 1,77 / 5,00 | 79,5 % |
| V4 | 54 | 1046 | 2815 | 2,27 / 4,93 | 52,2 % |
| V5 | 56 | 997 | 2539 | 1,88 / 6,80 | 77,8 % |
| V6 | 69 | 1053 | 2601 | 1,67 / 5,77 | 75,9 % |
| V7 | 56 | 1326 | 3634 | 2,77 / 6,50 | 49,0 % |

~72 % de B-frames, GOP variable avec insertion d'I-frames aux changements de scène (« scenecut ») : profil typique d'un transcodage serveur x264-like. Aucune chaîne SEI d'encodeur (`x264 - core …`) n'est présente : elle a été supprimée ou l'encodeur est propriétaire **[CONFIRMÉ : absence]**.

## 4. Signatures du pipeline de distribution

| Indice | Valeur | Interprétation |
|---|---|---|
| `comment` | `vid:v26044gc0000…` / `v15044…` / `v12025…` | Identifiant vidéo TikTok **[CONFIRMÉ]** |
| `vid_md5` | présent | Empreinte ajoutée par la plateforme **[CONFIRMÉ]** |
| `aigc_info` | `{"aigc_label_type":0}` (absent sur V7) | Champ « contenu généré par IA » de TikTok ; 0 = **non déclaré** comme IA. Ne prouve **pas** l'absence d'IA **[CONFIRMÉ (valeur) / INDÉTERMINABLE (portée)]** |
| `encoder` | `Lavf58.76.100` | Muxeur FFmpeg 4.4 côté serveur (pas l'outil du créateur) **[FORTEMENT PROBABLE]** |
| 576×1024 | toutes | Rendition « download » de TikTok, pas la résolution de production (probablement 1080×1920) **[FORTEMENT PROBABLE]** |
| Fin de vidéo | 4,0–4,5 s d'écran noir « TikTok @compte » + jingle (−23 dB, identique sur les 7) | Carte de fin ajoutée au téléchargement ; **n'appartient pas à la production** **[CONFIRMÉ]** |
| Filigrane | logo TikTok + @compte, position changeante (haut-gauche → bas-droite vers 2–3 s) | Filigrane dynamique ajouté au téléchargement **[CONFIRMÉ visuellement]** |

**Conséquence méthodologique** : toutes les métadonnées décrivent la *distribution*, pas la *création*. Les conclusions sur le moteur de création (section 05 du master) reposent uniquement sur l'analyse d'image et de son.

## 5. Indices de post-production lisibles dans l'image

| Indice | Vidéos | Méthode de mesure | Statut |
|---|---|---|---|
| Sous-titres incrustés mot-à-mot avec animation « pop » | 7/7 | lecture image par image (`tools/frame_strip.py`), OCR | **[CONFIRMÉ]** |
| Second filigrane de créateur au centre (`@elii.rbl`, semi-transparent) | V7 | visuel | **[CONFIRMÉ]** |
| Stickers persistants (photo de personne réelle en bas-droite, bonhomme de neige en bas-gauche) | V4 | visuel | **[CONFIRMÉ]** |
| Vignettage constant | V3 (ratio coin/centre médian 0,695) | `tools/grade_analysis.py` | **[CONFIRMÉ]** |
| Accentuation + saturation forte (« filtre HDR/clarity ») | V4 (sat. médiane 153, %noirs écrasés p90 12,7 %) | idem + visuel | **[FORTEMENT PROBABLE]** |
| Grain / bruit dans les aplats | V5 (5,6), V4 (4,9), V1 (4,4) vs V7 (2,5) | idem ; inclut le bruit de compression | **[HYPOTHÈSE]** (grain volontaire vs artefacts) |

## 6. Outils et scripts utilisés pour cette analyse

Tous dans `tools/` (lancés en lecture seule sur les originaux, Python `-I`) :

| Script | Rôle | Sortie |
|---|---|---|
| `analyze_video.py` | 100 % des images : luma, saturation, histogramme HSV, flux optique Farnebäck, détection de plans adaptative | `*_frames.csv`, `*_shots.json` |
| `contact_sheet.py` | image clé au milieu de chaque plan + planches-contact | `KEYFRAMES/Vx/` |
| `transcribe.py` | transcription locale mot-à-mot (faster-whisper small.en, CPU) | `*_transcript.json/.txt` |
| `audio_analysis.py` | enveloppes, bandes spectrales, stéréo, pauses, synchro coupes↔mots | `*_audio.json`, `*_envelope.npz` |
| `camera_motion.py` | classement des mouvements caméra, easing, jitter, flashs, fondus | `*_camera.json` |
| `zoom_forensics.py` | test 2D (zoom numérique) vs 3D (parallaxe), **calibré** sur un zoom synthétique | `*_zoom_forensics.json` |
| `motion_blur_probe.py` | tentative de mesure automatique du flou de bouger (non concluante, voir 16) | `*_motionblur.json` |
| `grade_analysis.py` | vignettage, température, saturation, contraste, accentuation, grain | `*_grade.json` |
| `caption_ocr.py` | OCR des sous-titres incrustés + alignement sur la voix | `*_captions.json` |
| `frame_strip.py` | bandes image-par-image des passages complexes | (scratchpad) |
| `build_timeline.py` | génération des tableaux de `03_COMPLETE_TIMELINE.md` | — |
