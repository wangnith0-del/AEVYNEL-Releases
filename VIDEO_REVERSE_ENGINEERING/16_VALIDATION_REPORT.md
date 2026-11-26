# 16 — Rapport de validation

## 1. Couverture réelle de l'analyse

| Élément | Couverture | Preuve |
|---|---|---|
| Métadonnées / flux | 7/7 fichiers, ffprobe complet + liste des images | `01`, `*_gop.json` |
| Analyse image | **100 % des 26 945 images** (luma, couleur, histogramme, flux optique) | `*_frames.csv` |
| Plans | 510 plans, 1 image clé chacun | `*_shots.json`, `KEYFRAMES/` |
| Inspection visuelle | toutes les images clés (planches-contact) + ~25 images pleine résolution + 14 bandes image par image | `03`, `05` |
| Audio | 100 % de la durée : loudness, spectre, enveloppe, transcription mot par mot | `*_audio.json`, `*_transcript.*`, `*_spectrogram.png` |
| Sous-titres | synchro mesurée à 30 fps sur 100 % de la durée ; OCR texte **non terminé** (arrêté faute de quota) | `*_caption_sync.json`, `*_captions.json` |
| Fichiers sources / projets | **aucun disponible** | — |

## 2. Conclusions CONFIRMÉES (mesure ou vérification directe)

* Spécifications des flux (576×1024, 30 fps CFR exact, H.264 High, AAC 44,1 kHz 128 kb/s), structure GOP, signatures TikTok, carte de fin ajoutée au téléchargement.
* Loudness : −13,7 à −14,7 LUFS (V2, V3, V4, V6, V7) ; −19,1/−19,6 LUFS (V1, V5).
* Voix dès 0,00 s, phrase d'ouverture « In this/my town » 7/7, débit 172–234 mots/min.
* Rig R6 rigide, visages 2D à swap instantané (V7 f4812→f4814).
* Mouvements de caméra 3D avec parallaxe (299/307 plans ; contrôle 2D calibré).
* Flou de mouvement présent sur V2, V3, V6 (image par image) ; absent sur les passages rapides vérifiés de V1, V5 (et non observé sur V4, V7).
* Reflet sélectif V6 81–85 s ; ombre sans propriétaire V1 ; indice ✦ à l'image 0 de V5 ; reveal sans coupe V5 0–1,1 s ; montage rapide V5 79,5–81,3 s ; fondu depuis le blanc V3 74,9–75,4 s.
* Vignettage constant V3 (coin/centre 0,695).
* Bascules du bed musical : V6 60,9 s, V7 115,6–124,2 s (chant), V3 ~80 s.
* Sous-titres un mot à la fois, synchronisés sur la voix : 92,5–100 % des mots couverts à ±250 ms ; décalage médian V1 +40, V2 +7, V3 0, V4 −40, V5 +20, V6 −53, V7 +27 ms.
* Coupes sur les mots : 80–85 % à < 100 ms (V1, V5, V7).
* Mêmes personnages et assets entre V3 et V6.

## 3. FORTEMENT PROBABLE

* Familles de rendu A (capture Roblox : V1, V4, V5, V7) et B (rendu offline type Blender : V2, V3, V6).
* Caméras animées dans le moteur (Moon Animator ou script pour Roblox ; clés pour Blender).
* Éditeur avec sous-titres automatiques animés (type CapCut) ; stickers et filtres d'éditeur (V4).
* Production à 1080×1920 puis réduction par TikTok.
* Physique de corps rigides (V1 effondrement).

## 4. HYPOTHÈSES

* Outils exacts (Moon Animator, OBS, CapCut, Blender vs autre moteur offline).
* Méthode de l'ombre V1 (LocalTransparencyModifier vs objet invisible à la caméra).
* Voix accélérée en post ; V4 contenu remonté ; V5 CTA commercial.
* Focales/hauteurs de caméra estimées ; paramètres d'éclairage et de grade proposés.

## 5. INDÉTERMINABLE

* Voix humaine ou TTS IA ; identité des voix des répliques (analyse F0 contaminée par la musique : p.ex. « Lily » V6 mesurée à 87 Hz = basse du bed).
* Jeu/carte Roblox exacts ; logiciel de montage exact.
* Inventaire exhaustif des SFX (pas de séparation de sources).
* Toute donnée d'audience (rétention, vues, partages) : **aucune n'est disponible, aucune n'est affirmée**.

## 6. Tests réalisés

| Test | Résultat |
|---|---|
| Détection de plans vs détecteur de scènes FFmpeg (`scene>0.25`) | 81–100 % de mes coupes confirmées ; ±10 % sur le nombre de plans |
| Calibrage du test 2D/3D sur un zoom synthétique | contrôle : 100 % d'inliers, résidu 0,06 px → séparation nette avec le corpus (29–43 %, 1–3 px) |
| Sonde automatique de flou de mouvement (Laplacien vs flux) | **non concluante** (ratios 0,8–1,4 sans tendance nette ; les blocs rapides sont aussi des bords contrastés). Conclusions de flou fondées sur l'inspection image par image uniquement |
| Pitch F0 (pYIN) narrateur vs répliques | indicatif seulement (contamination musicale) |
| OCR complet des sous-titres (tesseract à chaque changement) | abandonné pour lenteur (> 30 min sans terminer) ; remplacé par la détection d’apparitions à 30 fps (100 % de la durée) ; OCR partiel (30 s) également arrêté avant la fin |
| Planificateur de plans vs coupes réelles (±150 ms) | V1 59 %, V3 51 %, V5 72 %, V7 63 % de rappel → les monteurs coupent aussi sur des beats visuels hors débuts de phrase |
| Rendu Three.js headless | 180 images, 37,5 s, H.264 ; flou ×8 vérifié (netteté −50 % sur membres mobiles) |
| Sous-titres pop + mix | rendu vérifié visuellement ; loudness de sortie −14,0 LUFS |
| Blender bpy 4.2 Cycles | ombre sans propriétaire, reflet sélectif, flou de mouvement : les 3 visibles sur une même image |
| Luau Roblox | **non testé** (pas de Roblox Studio) |

## 7. Limites rencontrées

* Pas de GPU : pas de mesure de performances GPU ; Eevee non testé (Cycles CPU seulement).
* Vidéos téléchargées à 576×1024 recompressées : les détails fins (grain, textures) sont mêlés aux artefacts de compression.
* Transcription Whisper `small.en` : quelques erreurs ponctuelles (p.ex. V6 « On 12, my little sister » pour « I'm 12 » ; V7 paroles de la berceuse approximatives).
* Le classement automatique des mouvements de caméra est grossier sur les plans < 0,6 s.
* Erreurs détectées et corrigées pendant l'analyse : mesure du cycle de course V6 (corrigée à ≈ 28 images), décompte du test 2D/3D (307 plans), « fondus candidats » (vérifiés image par image : un vrai fondu depuis le blanc, une séquence de montage rapide).
