# 02 — Rétro-ingénierie du « code source » et de l'architecture

## 0. Statut des sources

**Aucun code source original n'a été fourni ni n'est récupérable depuis un MP4** **[CONFIRMÉ]**. Tout le code de ce dossier est **reconstruit** à partir des observations ; aucune ligne n'est présentée comme originale. Chaque mécanisme reconstruit renvoie à la mesure qui le justifie.

Ce qui a été réellement exécuté et testé dans cet environnement :

| Code | Langage | Testé ? | Preuve |
|---|---|---|---|
| `CODE_EXAMPLES/web_threejs/` | JavaScript / Three.js r169 / GLSL | **Oui** — 180 images rendues headless (Playwright + SwiftShader), encodées en H.264 | `_test_outputs/threejs_render_strip.jpg`, `threejs_demo_final.mp4` |
| `CODE_EXAMPLES/pipeline/captions_ass.py` | Python + libass | **Oui** — sous-titres « pop » incrustés | `_test_outputs/threejs_with_pop_captions_strip.jpg` |
| `CODE_EXAMPLES/pipeline/mix_and_master.sh` | FFmpeg filtergraph | **Oui** — sortie mesurée −14,0 LUFS | `16_VALIDATION_REPORT.md` |
| `CODE_EXAMPLES/pipeline/shot_planner.py` | Python | **Oui** — confronté aux coupes réelles (rappel 51–72 % à ±150 ms) | `ANALYSIS_DATA/shot_planner_validation.txt` |
| `CODE_EXAMPLES/blender/r6_story_scene.py` | Python / bpy 4.2 | **Oui** — rendu Cycles CPU : flou de mouvement, ombre sans propriétaire, reflet sélectif | `_test_outputs/blender_f0040_*.jpg` |
| `CODE_EXAMPLES/roblox/*.luau` | Luau | **Non** (pas de Roblox Studio ici) | écrit contre l'API publique Roblox |

## 1. Deux pipelines de création distincts sous une même grammaire de montage

L'analyse image par image sépare les 7 vidéos en deux familles de *rendu*, mais elles partagent la même *post-production* (voix → sous-titres mot-à-mot → montage serré → export vertical).

```
                     ┌──────────────── PIPELINE A : capture temps réel Roblox ────────────────┐
 Script ─► Voix ─►   │ Roblox Studio (place + rigs R6) ─► caméra scriptée/Moon Animator ─►     │
 (texte)   (TTS ou   │ Play Solo / Studio ─► capture écran (OBS, ≥30 fps) ─► rushes par plan   │ ─┐
           voix)     └────────────────────────────────── V1, V4, V5, V7 ───────────────────────┘  │
                     ┌──────────────── PIPELINE B : rendu offline (type Blender) ──────────────┐  ├─► Montage mobile/desktop
                     │ Avatars R6 (importés de Roblox ou recréés) ─► scène 3D ─► animation      │  │   (CapCut-like) : coupes
                     │ clé ─► caméra animée ─► rendu Eevee/Cycles avec flou de mouvement ─►     │ ─┘   sur la voix, sous-titres
                     │ séquences d'images / MP4                         V2, V3, V6              │      pop, musique, SFX,
                     └─────────────────────────────────────────────────────────────────────────┘      filtres ─► export 1080×1920
                                                                                                        ─► TikTok (576×1024 DL)
```

Justification des familles : voir `00_MASTER_REPORT.md §3` (tableau par vidéo) et `14_COMPARATIVE_ANALYSIS.md`.

## 2. Architecture reconstruite d'un projet de production (vue modules)

L'architecture ci-dessous est l'organisation **minimale cohérente** avec tout ce qui est observable. Elle est implémentée (en version réduite mais fonctionnelle) dans `CODE_EXAMPLES/web_threejs/`.

```
project/
├─ episode.json              # données : script, timings voix, liste de plans, événements
├─ assets/                   # avatars, visages (décalques), kits de décor, musique, SFX
├─ src/
│  ├─ main.js                # point d'entrée : charge l'épisode, expose renderFrame(i)
│  ├─ character.js           # CharacterFactory : rig R6 + visage interchangeable
│  ├─ animation.js           # cycles procéduraux, pistes de clés, easing, ressorts
│  ├─ camera.js              # CameraDirector : liste de plans → caméra à l'instant t
│  ├─ world.js               # kits modulaires instanciés + éclairage + brouillard
│  └─ post.js                # bloom → grade → vignette → grain
├─ pipeline/
│  ├─ shot_planner.py        # timings voix → coupes
│  ├─ captions_ass.py        # timings voix → sous-titres pop
│  └─ mix_and_master.sh      # voix + musique (ducking) + loudnorm + encodage
└─ render.mjs                # export image par image (headless) → ffmpeg
```

### 2.1 Point d'entrée et gestion du temps

* **Temps absolu, pas de delta-time.** Tout est une fonction pure de `t = frame / 30`. C'est la seule façon d'obtenir un rendu reproductible synchronisé à une voix préenregistrée (les vidéos ne montrent aucune dérive : coupes à ~20–30 ms des mots sur V1/V5/V7). Dans un moteur temps réel (pipeline A), l'équivalent est une horloge à pas fixe (`CinematicDirector.luau`, `t += 1/fps`).
* `window.renderFrame(i)` (Three.js) : pose les personnages, évalue la caméra, rend, renvoie. Pas de `requestAnimationFrame` en mode capture.

### 2.2 Structures de données (format `episode.json` recommandé)

```json
{
  "fps": 30,
  "voice": { "file": "vo.wav", "words": [{"w":"In","s":0.00,"e":0.12}, "..."] },
  "shots": [
    {"start":0.00,"end":3.30,"size":"wide","move":"push_in","ease":"outCubic",
     "from":{"pos":[1.2,1.6,6],"look":[-0.3,1,-3],"fov":50},
     "to":  {"pos":[0.9,1.5,3.8],"look":[-0.4,1.1,-3],"fov":50}}
  ],
  "events": [
    {"t":2.45,"type":"gesture","char":"hero","name":"alarm"},
    {"t":2.45,"type":"face","char":"hero","expr":"shock"},
    {"t":2.60,"type":"face","char":"sister","expr":"shock"},
    {"t":10.13,"type":"vfx","name":"golden_flash","dur":0.8},
    {"t":60.9,"type":"music","cue":"turning_point"}
  ]
}
```

### 2.3 Systèmes et communication

| Système | Entrées | Sorties | Communique avec |
|---|---|---|---|
| ShotPlanner | mots horodatés, phrases | `shots[]` | CameraDirector, éditeur |
| CharacterFactory | palette, visage, cheveux | `{root, joints, setExpression}` | Animation, Events |
| Animation | `t`, état d'action | rotations des pivots | Character |
| EventScheduler | `events[]` triés, `t` | appels `setExpression`, `gesture`, VFX, cues audio | tous |
| CameraDirector | `shots[]`, `t` | position/visée/FOV caméra | Renderer |
| World | preset (day/sunset/night) | scène, lumières | Renderer |
| Post | uniforms | image finale | Renderer |
| Captions/Mix | mots, pistes audio | `.ass`, mix −14 LUFS | encodeur |

### 2.4 Hiérarchie et transformations

Rig R6 = 6 maillages rigides, **pivots aux articulations** (épaules, hanches, cou). Le maillage est décalé sous le pivot (`mesh.position.y = -longueur/2`) pour que la rotation locale du pivot produise un balancier anatomique. La racine porte la translation dans le monde ; le bassin (`hips`) porte le rebond vertical et le roulis. Ce découpage local/global est ce qui permet de superposer marche + geste + idle sans conflit (chaque couche écrit des canaux distincts ou est remise à zéro à chaque image — voir `heroPose()` dans `main.js`).

Coordonnées : Y vers le haut (Three.js, Roblox) ; Z vers le haut dans Blender — le script bpy en tient compte.

### 2.5 Machine à états implicite

Les vidéos ne montrent pas d'IA de comportement : chaque action est **scriptée par le temps**. La « machine à états » se réduit à une séquence `idle → walk → stop(décélération) → gesture → idle` dont les transitions sont des fondus de poids (`weight` dans `locomotion()`) — équivalent du `track:Play(fadeTime)` Roblox ou des NLA strips Blender.

### 2.6 Synchronisation audio-visuelle

Source de vérité unique : **les timestamps de mots de la voix**. Tout en découle :
1. coupes (ShotPlanner, image avant le mot de ~25 ms),
2. sous-titres (un mot = un événement),
3. swaps de visage (« talk » = alternance bouche ouverte/fermée sur les mots, `FaceAndActing.luau`),
4. cues musique/SFX aux pivots narratifs.

### 2.7 Génération procédurale

Observée : répétition de modules de décor (maisons, arbres, lampadaires) et de foules (V1 place, V5 villageois) — **instancing** de kits. La foule V5 (≈50 personnages) varie couleurs/accessoires sur une poignée de modèles **[FORTEMENT PROBABLE]**. Implémentation : `world.js` (InstancedMesh + couleur par instance, PRNG à graine fixe pour un résultat reproductible).

### 2.8 Collisions / physique

* V1 112–118 s : maisons basculant dans le gouffre, trajectoires de chute non-scriptées, sans flou → **simulation de corps rigides** (Roblox : pièces désancrées ; Blender : Rigid Body World) **[FORTEMENT PROBABLE]**.
* Ailleurs, aucun contact physique crédible n'est requis : les pieds glissent rarement parce que la vitesse de translation est liée à la phase du cycle (voir 05).

### 2.9 Mémoire et ressources

Les scènes sont légères (primitives, textures basse résolution ; décalques de visage visiblement pixelisés en gros plan sur V7). Coûts dominants : ombres (shadow maps), post-traitement plein écran, et en pipeline B les échantillons de rendu. Détails et budgets : `13_PERFORMANCE_OPTIMIZATION.md`.

## 3. Paramètres qui contrôlent le résultat (et comment les modifier)

| Paramètre | Où | Valeur de départ | Effet |
|---|---|---|---|
| `WALK_SPEED`, `STRIDE` | `main.js` | 1,4 u/s ; 1,1 u/cycle | doivent rester liés (phase = distance/stride) sinon glissement des pieds |
| `legAmp/armAmp` | `animation.js` | 0,55/0,5 (marche), 0,95/1,05 (course) | énergie du personnage |
| `ease` d'un plan | `shots[]` | `inOutSine` (calme), `outCubic` (choc), `inCubic` (tension) | lecture émotionnelle du mouvement |
| `shake` | `shots[]` | 0–0,01 | « respiration » de caméra ; mesuré quasi nul dans le corpus |
| `uVignette` | `post.js` | 0,3 (V3 ≈ 0,35 équiv.) | focalisation centrale |
| `bloom` | `post.js` | 0,3 | halo des zones claires (V3 lumière dorée) |
| `--lead-ms` | `shot_planner.py`, `captions_ass.py` | 25 ms | avance image/texte sur la voix |
| `max_shot` | `shot_planner.py` | 2,6 s | rythme ; corpus médian 1,33–2,5 s |

## 4. Améliorer la qualité sans dégrader la stabilité

1. Garder le rendu **déterministe** (graines fixes, pas de `Math.random()` non seedé, pas d'horloge murale).
2. Monter la qualité par **paramètres de rendu** (taille shadow map, échantillons, résolution) plutôt qu'en ajoutant des systèmes.
3. Ajouter le flou de mouvement par **sous-échantillonnage temporel** (rendre 4–8 sous-images par image et les moyenner) : c'est la différence visuelle la plus nette entre pipeline A et B, et elle est triviale avec un rendu en fonction pure de `t`.
4. Versionner `episode.json` : une production = des données, le code reste stable.
