# CODE_EXAMPLES — implémentations reconstruites

Tout le code ici est **reconstruit** à partir de l'analyse (aucun code original n'était disponible). Statut de test :

| Dossier | Contenu | Testé | Commande |
|---|---|---|---|
| `web_threejs/` | rig R6 + visages canvas, cycles/gestes/clignements, directeur de caméra par plans, kit de ville instancié, post (bloom, grade, vignette, grain), **flou de mouvement par sous-échantillonnage**, export headless image par image | **oui** (Chromium headless SwiftShader) | `cd web_threejs && npm install && node render.mjs out` · flou : `MB=6 node render.mjs out` · aperçu : `npx serve .` puis ouvrir `index.html` |
| `pipeline/shot_planner.py` | mots horodatés → liste de plans | **oui** (comparé aux coupes réelles) | `python3 shot_planner.py words.json shots.json` |
| `pipeline/captions_ass.py` | mots horodatés → sous-titres « pop » ASS | **oui** | `python3 captions_ass.py words.json out.ass --style yellow` |
| `pipeline/mix_and_master.sh` | voix + musique (ducking) + loudnorm −14 LUFS + sous-titres incrustés + H.264/AAC | **oui** (−14,0 LUFS mesuré) | `bash mix_and_master.sh silent.mp4 vo.wav music.wav captions.ass final.mp4` |
| `blender/r6_story_scene.py` | rig R6 en primitives, visage à clés CONSTANT, marche, geste, caméra ease, **flou de mouvement**, **ombre sans propriétaire**, **reflet sélectif** | **oui** (bpy 4.2, Cycles CPU) | `python r6_story_scene.py --out /tmp/r6 --frames 1,20,36,40` (Python 3.11 + `pip install bpy==4.2.0`) ou `blender -b -P r6_story_scene.py -- --out /tmp/r6` |
| `roblox/CinematicDirector.luau` | lecteur de liste de plans à horloge fixe, push-in, presets d'éclairage | **non** (pas de Roblox Studio) | LocalScript, Play Solo, capture OBS |
| `roblox/FaceAndActing.luau` | swaps de visage, clignements, « talk », lecture d'animations, marche | **non** | idem |

Preuves de test : `_test_outputs/`
* `threejs_render_strip.jpg` — 12 images du rendu (marche → arrêt → geste + visage choc → gros plan, clignement, sourire)
* `threejs_with_pop_captions_strip.jpg` — même rendu avec sous-titres pop incrustés
* `threejs_motionblur_off_vs_MB8_frames76_78.jpg` — sans flou / avec 8 sous-images (netteté −50 % sur bras en mouvement)
* `threejs_demo_final.mp4` — démo 6 s mixée (signal de test, pas de vraie voix)
* `blender_frames_1_20_36_40.jpg`, `blender_f0040_shadow_reflection_motionblur.jpg` — rendu Blender

Dépendances : Node ≥ 18, `three@0.169.0` (npm), Playwright + Chromium ; Python 3 + FFmpeg avec libass ; optionnel `faster-whisper` ; Blender 4.2 ou `bpy==4.2.0` (Python 3.11).
