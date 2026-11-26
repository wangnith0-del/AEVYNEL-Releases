# 07 — Caméra et réalisation

Données : `ANALYSIS_DATA/*_camera.json` (classement de chaque plan à partir du flux optique de **toutes** les images), `*_zoom_forensics.json` (test 2D/3D), bandes image par image.

## 1. Mesures globales

| | V1 | V2 | V3 | V4 | V5 | V6 | V7 |
|---|---|---|---|---|---|---|---|
| Plans (hors carte de fin) | 47 | 42 | 83 | 92 | 54 | 83 | 102 |
| Durée médiane (s) | 2,50 | 1,58 | 1,43 | 1,43 | 1,80 | 1,33 | 1,52 |
| Push-in | 6 | 26 | 25 | 53 | 32 | 34 | 52 |
| Pull-out | 0 | 2 | 4 | 1 | 4 | 1 | 4 |
| Pan/track | 1 | 2 | 7 | 6 | 3 | 12 | 1 |
| Tilt/grue | 0 | 2 | 0 | 2 | 5 | 1 | 0 |
| Dérive lente | 24 | 5 | 24 | 23 | 8 | 18 | 27 |
| Statique | 17 | 2 | 16 | 1 | 2 | 9 | 6 |
| Mouvement de sujet/orbite | 0 | 4 | 7 | 7 | 1 | 9 | 11 |
| Jitter médian (px/image natif) | 0,004 | 0,073 | 0,024 | 0,061 | 0,093 | 0,029 | 0,009 |

Seuils de classement (sur image 144×256, flux ×4 = px natifs) : statique si flux moyen < 0,6 px ; push/pull si composante radiale > 0,48 px et dominante ; pan/tilt si translation médiane > 1 px. Le classement est **automatique** : « dérive lente » regroupe des mouvements faibles ou mixtes.

## 2. Résultat clé : les mouvements sont de vraies caméras 3D **[CONFIRMÉ par test calibré]**

Test : suivi de ≥25 points (masque sur sous-titres et filigranes), ajustement d'une similitude (échelle+rotation+translation) par RANSAC entre deux images distantes de 8.
* **Contrôle** : zoom 2D synthétique (zoompan FFmpeg sur une image de V3, réencodé H.264) → **100 % d'inliers, résidu médian 0,06 px**.
* **Vidéos** : inliers médians 29–43 %, résidus 1,1–3,1 px → mouvement **non explicable par un zoom 2D** : parallaxe (profondeur) → caméra déplacée dans la scène 3D.
* 307 plans testés (push/pull/dérive ≥ 0,8 s) : **299 « 3D »**, 5 « 2D » (cas isolés : sujet plan face caméra), 3 « quasi statiques ».

Conséquence : les push-in ne sont pas des « Ken Burns » ajoutés dans l'éditeur ; ils sont animés dans le moteur (Roblox : CFrame interpolé, p.ex. Moon Animator ; Blender : caméra à clés) **[FORTEMENT PROBABLE quant à l'outil, CONFIRMÉ quant au caractère 3D]**.

## 3. Profils de vitesse (easing) mesurés

| | ease-in-out | ease-in (accélère) | ease-out (décélère) | constant |
|---|---|---|---|---|
| V1 | 12 | 11 | 6 | 2 |
| V2 | 16 | 11 | 10 | 4 |
| V3 | 39 | 12 | 13 | 3 |
| V4 | 11 | 14 | 23 | 39 |
| V5 | 23 | 13 | 12 | 4 |
| V6 | 32 | 16 | 20 | 6 |
| V7 | 23 | 32 | 21 | 18 |

Lecture : V3/V6 (@whatifstoriess_) privilégient l'**ease-in-out** (mouvement « cinéma », doux) ; V4 beaucoup de **constant/ease-out** (poussées linéaires : interpolation par défaut ou caméra de jeu) ; V7 beaucoup d'**ease-in** (accélération vers le visage = tension). Méthode : vitesse lissée sur 5 images, comparaison des tiers du plan (seuil ×1,25–1,3). Les plans très courts rendent la classification approximative **[HYPOTHÈSE pour un plan donné, tendance FORTEMENT PROBABLE]**.

## 4. Grammaire de plans observée

| Type | Usage narratif | Exemples |
|---|---|---|
| Plan aérien / plongée d'établissement | « In this town… » : poser le monde | V2 0–3 s (survol descendant), V3 0–2,6 s, V6 0–0,5 s, V1 26–29 s (coupe de la ville au-dessus du vide) |
| **Recul aérien ultra-rapide** (reveal) | accroche + indice caché | V5 0,0–1,1 s : gros plan Grand-mère (éclat sur le chignon) → panorama de la meule, flux 4→20 px/image, sans coupe |
| Plan moyen frontal en poussée lente | exposition, personnage qui parle | majorité des plans |
| Gros plan visage | émotion, révélation | V6 « memorize », V7 « year », V2 « glass » (dernier plan) |
| Insert objet | élément de règle/indice | calendrier (V6), réveil 6:59 / montre 11:59:58 (V4), bocal de plumes (V3), aiguille (V5) |
| POV | point de vue subjectif | V2 47–54 s : vignette « jumelles » (masque noir à deux lobes) |
| Contre-plongée | personnage dominant | Papa V2 « tall » ; maire V5 « lifted » |
| Angle hollandais | instabilité | V1 effondrement (~20°) |
| Travelling d'accompagnement | course/poursuite | V6 66–68 s, V3 75–78 s |

**Hauteur/focale estimées** **[HYPOTHÈSE]** : caméra à hauteur de poitrine–tête d'un R6 pour les plans moyens ; champ vertical ≈ 40–60° (équivalent ≈ 24–35 mm plein format en vertical) pour les plans larges, ≈ 25–35° pour les gros plans (fond peu déformé, flou d'arrière-plan sur V6). Estimation visuelle par la déformation perspective des verticales ; non mesurable précisément sans métadonnées.

**Profondeur de champ** : nette séparation sujet/fond sur V6 (gros plans au coucher) et V3 (intérieurs) — DOF de rendu ; quasi absente sur V4/V7 (tout net) **[CONFIRMÉ visuellement]**.

## 5. Programmation des mouvements

Modèle « liste de plans » (implémenté dans `web_threejs/src/camera.js`, `roblox/CinematicDirector.luau`, `blender/r6_story_scene.py`) :

```js
// un plan = deux poses caméra + une courbe ; coupe franche entre plans
{ start: 2.0, end: 4.0, ease: 'outCubic',
  from: { pos: [0.6,1.4,1.5], look: [-0.4,1.4,-2.0], fov: 45 },
  to:   { pos: [0.1,1.45,0.2], look: [-0.5,1.5,-2.0], fov: 45 } }
// évaluation (camera.js)
const u = Ease[s.ease]((t - s.start) / (s.end - s.start));
camera.position.lerpVectors(from.pos, to.pos, u); camera.lookAt(from.look.lerp(to.look, u));
```

* Push-in « émotion » : `outCubic` sur 1,5–2 s, distance divisée par ~1,5–2.
* Push-in « tension » : `inCubic` (accélère vers le visage), à couper juste avant la révélation.
* Recul-révélation (V5) : interpolation exponentielle de la distance (`d(t) = d0 · (d1/d0)^u`) — la vitesse apparente reste constante malgré l'éloignement ; combiner avec une montée en hauteur.
* Splines : pour un trajet courbe (survol V2), interpoler la position sur une `CatmullRomCurve3` et la visée sur un second chemin ; paramétrer par abscisse curviligne pour une vitesse constante.
* « Respiration » de caméra : somme de sinus incommensurables d'amplitude ≤ 1 cm (`shake` dans `camera.js`) — le corpus montre un jitter quasi nul, donc à utiliser avec parcimonie.

## 6. Transitions

* **Coupes franches** : quasi exclusives. Détection confirmée par le détecteur de scènes FFmpeg (81–100 % de concordance).
* **Flashs/fondus au blanc** : V3 6,2 s / 10,1–10,9 s / 72,6–74,1 s (« lumière dorée », luma > 215) ; V7 44,3–45,5 s (« RANDOM KID AGAIN » : passage au gris/blanc). Ce sont des **effets narratifs**, pas des transitions de confort.
* **Fondu depuis le blanc** : V3 74,9–75,4 s — la « lumière dorée aveuglante » se résorbe sur le plan suivant (passage-de-relais pendant le blanc) **[CONFIRMÉ image par image]**.
* **Séquence de montage rapide** : V5 79,5–81,3 s (« We dug for three days ») ≈ 10 plans de 4–6 images sur la foule qui creuse, puis **rétrécissement animé de la meule** (81,4–81,8 s, « the mountain became a hill ») — compression du temps sans fondu **[CONFIRMÉ image par image]**. Le détecteur automatique fusionne ces micro-plans (seuil adaptatif) : le nombre de plans de V5 est donc **sous-estimé d'environ 10**.
* Les autres « fondus candidats » détectés automatiquement correspondent à des mouvements rapides de caméra ou de particules (paille, neige) : **pas de fondu enchaîné classique dans le corpus** **[CONFIRMÉ sur les passages vérifiés]**.
