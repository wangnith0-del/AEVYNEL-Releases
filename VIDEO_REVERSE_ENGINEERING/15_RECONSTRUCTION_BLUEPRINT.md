# 15 — Blueprint de reconstruction (architecture recommandée)

Objectif : produire un épisode de 70–160 s du même format, **au moins au niveau de V2/V3/V6** (pipeline B), à partir de données, avec un code stable réutilisé d'épisode en épisode. **Aucune production n'a été lancée** : ce document décrit l'architecture ; la démonstration de 6 s dans `CODE_EXAMPLES/_test_outputs/` ne sert qu'à valider le code.

## 1. Choix du moteur (recommandation)

| Option | Qualité | Coût de production | Contrôle/automatisation | Recommandé pour |
|---|---|---|---|---|
| **Three.js offline (ce dossier)** | moyenne → bonne (ombres douces, bloom, grade, flou de mouvement par sous-échantillonnage) | faible | **total** (tout est code + JSON, rendu déterministe headless) | production en série automatisée |
| Blender (bpy) | **la meilleure** (GI, DOF, flou natif, reflets sélectifs) | moyen (temps de rendu) | élevé (bpy scriptable) | épisodes « premium », twists visuels |
| Roblox Studio + capture | bonne pour le style « Roblox authentique », assets gratuits | faible | moyen (capture temps réel, OBS) | si l'audience attend le look Roblox exact |

**Recommandation** : architecture **pilotée par données** commune, avec **deux back-ends** de rendu (Three.js pour le volume, Blender pour les épisodes clés). Les deux consomment le même `episode.json`.

## 2. Structure de projet

```
studio/
├─ episodes/E012_<slug>/
│  ├─ script.txt                # gabarit 11 §5
│  ├─ vo.wav                    # voix
│  ├─ words.json                # Whisper word timestamps (source de vérité)
│  ├─ shots.json                # généré puis retouché à la main
│  ├─ events.json               # visages, gestes, VFX, cues musique
│  └─ out/                      # frames/, silent.mp4, captions.ass, final.mp4
├─ library/
│  ├─ characters/*.json         # palette, accessoires, jeu de visages (casting récurrent)
│  ├─ faces/*.png               # ≥ 8 expressions par personnage-type
│  ├─ sets/*.json               # lieux héros + paramètres de kits
│  ├─ looks/*.json              # presets lumière+grade : day, golden, sunset, night_storm, cave
│  └─ music/, sfx/
├─ engine_three/                # = CODE_EXAMPLES/web_threejs (character, animation, camera, world, post, main, render)
├─ engine_blender/              # = CODE_EXAMPLES/blender/r6_story_scene.py étendu
└─ pipeline/                    # = CODE_EXAMPLES/pipeline (shot_planner, captions_ass, mix_and_master) + tools/ (QC)
```

## 3. Flux d'un épisode

1. `script.txt` (règle → exemples → moi → perturbation → crise → retournement → chute).
2. Voix → `vo.wav` ; `faster-whisper --word_timestamps` → `words.json`.
3. `shot_planner.py words.json shots.json` → coupes sur les phrases (image 25 ms avant le mot), max 2,6 s.
4. Retouche humaine de `shots.json` : taille de plan, lieu, mouvement (push-in par défaut ; ease-in pour la tension, out pour le choc), et des **plans-clés** de mise en scène (reveal type V5, insert d'indice).
5. `events.json` : swaps de visage sur mots-clés, gestes, VFX (flash doré, particules), cues musique au pivot.
6. Rendu : `MB=6 node render.mjs out 1080 1920` ou `python r6_story_scene.py`.
7. `captions_ass.py words.json captions.ass --style yellow|white|upper --y 0.66`.
8. `mix_and_master.sh silent.mp4 vo.wav music.wav captions.ass final.mp4` → −14 LUFS.
9. QC automatique (12 §QC).

## 4. Aller au-delà du corpus (améliorations ciblées)

| Faiblesse observée | Amélioration | Où |
|---|---|---|
| Visages pixelisés en gros plan (V7) | visages vectoriels/canvas haute résolution (`drawFace`) ou textures ≥ 1024² | `character.js` |
| Pas de flou en capture temps réel (V1, V4, V5, V7) | flou par sous-échantillonnage, uniquement sur plans d'action | `renderFrameMB` |
| Bouche « talk » par simple alternance | 3–4 visèmes (fermé, ouvert, « o », sourire) pilotés par l'énergie de la voix par mot | événement `talk` |
| Coupes non alignées (V2, V6) | règle « image 25 ms avant le mot » automatisée | `shot_planner.py` |
| Loudness trop basse (V1, V5 : −19 LUFS) | `loudnorm I=-14` | `mix_and_master.sh` |
| Sur-filtrage (V4) | grade doux en shader, pas de filtre d'éditeur empilé | `post.js` |
| Indice caché unique (V5) | systématiser 1 indice d'image 0 par épisode (revisionnage) | écriture + `shots.json` |

## 5. Critères d'acceptation (mesurables avec `tools/`)

* Durée médiane de plan 1,3–2,5 s ; ≥ 75 % des plans avec mouvement caméra.
* ≥ 75 % des coupes à < 100 ms d'un début de mot.
* Sous-titres : ≥ 95 % des mots couverts, décalage médian |x| < 50 ms.
* −14 ± 1 LUFS, crête ≤ −1 dBTP.
* 1080×1920, 30 fps CFR, H.264 High, AAC 128 kb/s 44,1 kHz.
