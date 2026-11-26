# 00 — Rapport maître : rétro-ingénierie de 7 vidéos « In this town… »

**Corpus** : 7 MP4 (V1–V7, alias dans `ANALYSIS_DATA/aliases.txt`), 898 s au total, 26 945 images, 5 comptes TikTok. **Aucun fichier source fourni** : toutes les conclusions viennent de l'analyse des images, du son et des métadonnées, et le code fourni est **reconstruit**. Légende : **[CONFIRMÉ]** vérifié/mesuré · **[FORTEMENT PROBABLE]** · **[HYPOTHÈSE]** · **[INDÉTERMINABLE]**.

## 1. En une page

* **Ce que sont ces vidéos** : des récits courts (71–162 s de contenu), en 9:16, de personnages Roblox R6, narrés à la 1re personne, qui ouvrent tous à 0,00 s par « In this town, <règle surnaturelle> » **[CONFIRMÉ 7/7]**.
* **Comment elles sont faites** : deux familles de rendu sous une seule grammaire de montage.
  * **A — capture temps réel Roblox** (V1, V4, V5, V7) : aucun flou de mouvement même sur actions rapides, décalques basse résolution, éclairage direct **[FORTEMENT PROBABLE]**.
  * **B — rendu offline type Blender** (V2, V3, V6) : flou de mouvement par membre (bras flous, torse net), DOF, AO, **reflet sélectif** (V6) **[FORTEMENT PROBABLE]** ; alternative (capture + flou optique en post + astuces) **[HYPOTHÈSE moins probable]**.
  * **Montage commun** : coupe sur le mot (image 20–30 ms avant, 80–85 % des coupes sur V1/V5/V7), plans médians de 1,3–2,5 s, sous-titres « pop » un mot à la fois synchronisés sur la voix (92–100 % des mots, décalage médian −53…+40 ms), voix très rapide (172–234 mots/min), bed musical qui bascule aux pivots du récit **[CONFIRMÉ par mesure]**.
* **Découverte clé sur la caméra** : les push-in dominants (jusqu'à 57 % des plans) sont de **vrais mouvements 3D** dans le moteur, pas des zooms de montage : test calibré par RANSAC, 299 plans sur 307 montrent de la parallaxe, alors qu'un zoom 2D synthétique de contrôle donne 100 % d'inliers et 0,06 px de résidu **[CONFIRMÉ]**.
* **Ce qui les rend efficaces** (conception, pas audience mesurée) : concept montré à l'image 0, setup/payoff vérifiable par le spectateur (V5 : l'aiguille dans le chignon dès l'image 0, puis « Did you see it before I did? »), twists de relecture (V3, V6 : le narrateur est mort), lumière narrative (coucher de soleil = fin de la « visite »), son diégétique au moment clé (berceuse V7).

## 2. Livrables

| Fichier | Contenu |
|---|---|
| `01_TECHNICAL_ANALYSIS.md` | flux, GOP, loudness, signatures TikTok, outils d'analyse |
| `02_SOURCE_CODE_ANALYSIS.md` | architecture reconstruite, modules, données, temps, synchro |
| `03_COMPLETE_TIMELINE.md` | temps forts annotés + **510 plans** mesurés avec images clés |
| `04_CHARACTER_SYSTEMS.md` | rig R6, fiches personnages par vidéo, cohérence |
| `05_ANIMATION_SYSTEMS.md` | analyses image par image, 12 principes, anti-« mannequin » |
| `06_ENVIRONMENT_SYSTEMS.md` | décors, kits modulaires, instancing |
| `07_CAMERA_SYSTEMS.md` | mouvements mesurés, test 2D/3D, easing, grammaire de plans |
| `08_LIGHTING_AND_SHADERS.md` | empreinte colorimétrique, schémas d'éclairage, matériaux |
| `09_VISUAL_EFFECTS.md` | sous-titres pop, flou, ombre sans propriétaire, reflet sélectif, particules, grade |
| `10_AUDIO_SYSTEMS.md` | loudness, débit, bed musical, synchro A/V |
| `11_STORYTELLING_ANALYSIS.md` | structure en 7 actes, setups/payoffs, gabarit de script |
| `12_PRODUCTION_PIPELINE.md` | 19 étapes, outils, automatisation, QC |
| `13_PERFORMANCE_OPTIMIZATION.md` | mesures, leviers, 3 configurations |
| `14_COMPARATIVE_ANALYSIS.md` | comparaison, forces/faiblesses, meilleures techniques |
| `15_RECONSTRUCTION_BLUEPRINT.md` | architecture de production recommandée |
| `16_VALIDATION_REPORT.md` | confirmé / hypothèses / tests / limites |
| `CODE_EXAMPLES/` | Three.js (testé), pipeline Python/FFmpeg (testé), Blender bpy (testé), Roblox Luau (non testé) |
| `KEYFRAMES/` | 510 images clés (1 par plan) |
| `ANALYSIS_DATA/` | CSV image par image, JSON plans, caméra, audio, transcriptions, spectrogrammes, grade, synchro |
| `tools/` | scripts d'analyse réutilisables |

## 3. Identification du moteur, vidéo par vidéo

| Vidéo | Verdict | Indices pour | Indices contre / limites |
|---|---|---|---|
| V1 | **Roblox Studio, capture** [FORTEMENT PROBABLE] | avatars R6/accessoires catalogue, physique rigide sans flou (effondrement), ciel/éclairage type Roblox Future, aucun flou de mouvement | ombre sans propriétaire faisable aussi dans Blender ; faisceaux de la grotte (néon/Beam ?) |
| V2 | **Rendu offline (Blender probable)** [FORTEMENT PROBABLE] | flou de mouvement par membre (sauts), visages dessinés sur mesure, arêtes adoucies, éclairage doux | flou optique en post possible [HYPOTHÈSE] |
| V3 | **Rendu offline (Blender probable)** [FORTEMENT PROBABLE] | bras flous / torse net (f2119–2123), AO, intérieurs à GI douce, même univers que V6 | idem |
| V4 | **Roblox, capture + filtre d'éditeur** [FORTEMENT PROBABLE] | avatars/visages de catalogue, maisons type RP, eau/pluie Roblox, pas de flou, filtre sur-saturé + stickers | jeu exact [INDÉTERMINABLE] ; origine du contenu [HYPOTHÈSE : remontage] |
| V5 | **Roblox Studio, capture** [FORTEMENT PROBABLE] | ciel nuageux cartoon type Roblox, avatars R6, pas de flou (plongeon), modèles sur mesure (vache) | instancing de paille massif faisable ailleurs |
| V6 | **Rendu offline (Blender probable)** [FORTEMENT PROBABLE] | **reflet sélectif** dans la glace, flou sur la course, DOF, matériaux spéculaires | reflet imitable par un double inversé [HYPOTHÈSE] |
| V7 | **Roblox, capture** [FORTEMENT PROBABLE] | décalques de visage pixelisés en gros plan, carte/bus de type Brookhaven, éclairage plat, swaps de visage | — |

Technologies **non retenues** : Three.js/Babylon/WebGL/WebGPU, Unity, Unreal, Godot, Manim, Remotion, Canvas/SVG, Pygame comme moteur de création. Aucun indice positif ; ils **peuvent** reproduire le résultat (démontré ici avec Three.js) mais rien ne montre qu'ils ont été utilisés. After Effects / CapCut / Premiere : un éditeur avec sous-titres automatiques animés est **[FORTEMENT PROBABLE]**, le produit exact **[INDÉTERMINABLE]**. Les métadonnées (`Lavf58.76.100`, `vid:`, `aigc_info`) ne décrivent que la plateforme de diffusion.

## 4. Les 10 techniques à réutiliser en priorité

1. Concept visible à l'image 0 et phrase-règle à 0,00 s.
2. 1 proposition = 1 plan ; coupe 20–30 ms avant le mot.
3. Push-in 3D lent par défaut ; ease-in pour la tension, ease-out pour le choc ; reveal en recul rapide pour l'ouverture.
4. Sous-titres pop (70→112→100 % en ~3 images), un mot à la fois.
5. Rig R6 + bibliothèque de visages ; swaps instantanés déclenchés par les mots.
6. Flou de mouvement sur les plans d'action (rendu ou sous-échantillonnage).
7. Lumière narrative (doré = miracle, coucher = fin, nuit d'orage = crise).
8. Setup/payoff visuel vérifiable + défi au spectateur.
9. Bed musical qui bascule ~2 s avant le pivot ; un moment de son diégétique seul.
10. Master −14 LUFS, voix dominante, ducking.

## 5. Reprise

L'analyse est complète. Scripts et données permettent de rejouer chaque mesure (`tools/`, Python `-I`, en lecture seule sur les originaux). Prochaine étape possible, **sur votre autorisation uniquement** : produire un épisode pilote avec le blueprint (`15`).
