# 05 — Systèmes d'animation

Passages inspectés **image par image** (bandes de 12 images, pas de 2 ou 3 images) : V6 66,8–67,6 s (course), V1 59,3–60,0 s (marche), V2 36,7–37,5 s (sauts), V3 70,5–71,2 s (cri), V4 45,3–46,0 s (« Wake up! »), V5 12,2–13,3 s (dialogue), V5 62,2–62,5 s (plongeon), V5 0,0–1,1 s (ouverture), V7 159,8–160,5 s (bouche), V1 115,3–115,6 s (effondrement). Les durées sont mesurées en images à 30 fps.

## 1. Vocabulaire de mouvement d'un rig R6

Un R6 n'a que 5 rotations utiles (cou, 2 épaules, 2 hanches) + la translation/rotation de la racine. Tout le « jeu » passe donc par :

| Canal | Ce qui vend la vie | Mesure / observation |
|---|---|---|
| Opposition bras/jambes | lecture immédiate de la marche/course | V6 course : bras et jambes en opposition, amplitude jambes ≈ ±50°, bras ≈ ±60° ; cycle ≈ 28 images (≈ 0,93 s) **[mesuré sur bande, ±2 images]** |
| Inclinaison du torse | quantité d'effort | course V6 : torse penché vers l'avant ; marche V1 : quasi droit |
| Rebond vertical | poids | 2 creux par cycle (contacts) — visible sur V6, discret sur V1 |
| Tête | attention / émotion | rotation de cou vers l'interlocuteur ; inclinaison arrière sur le cri (V3) |
| Visage | émotion | swap instantané de décalque (0 image d'intermédiaire, V7 f4812→f4814) |
| Flou de mouvement | vitesse perçue + « film » | présent V2, V3, V6 (bras flous, torse net) ; absent V1, V4, V5, V7 |

## 2. Analyses détaillées

### 2.1 Course — V6 66,83–67,57 s (« I chased her »)
* Plan arrière ¾, caméra qui suit à vitesse ~constante (« tracking »), neige au premier plan.
* Cycle : écart maximal des jambes vers f2010, jambes jointes vers f2017, écart opposé vers f2024 → **demi-cycle ≈ 14 images, cycle ≈ 28 images ≈ 0,93 s** (±2 images ; échantillonnage toutes les 2 images). C'est lent pour une course : foulée ample et cadence réduite = course « dramatique », légèrement ralentie **[HYPOTHÈSE : ralenti volontaire ou animation lente]**.
* Bras quasi horizontaux en extension max (≈ 80–90°) → course « cartoon » exagérée (principe *exaggeration*).
* Flou de mouvement sur les bras aux extrêmes de vitesse (milieu de swing) et net aux extrêmes de position → cohérent avec un vrai flou de rendu (vitesse max au milieu de l'arc), pas avec un filtre uniforme.
* Pieds : empreintes laissées dans la neige (V6 « footprints ») → décalques/objets posés par script au contact **[HYPOTHÈSE technique]**.

### 2.2 Marche — V1 59,30–60,03 s (« I was supposed to go hiking »)
* Plan frontal fixe, personnage avançant vers la caméra ; marche R6 classique (bras pendulaires, jambes rigides).
* Le bras droit monte en geste (« lever la main ») **pendant** la marche : superposition d'une action secondaire sur le cycle (couche additive) — preuve d'un système à couches (animation de marche du Humanoid + animation de geste prioritaire **[FORTEMENT PROBABLE]**, typique du `Animator` Roblox avec priorités `Movement` < `Action`).
* Ombre portée nette sur l'herbe, synchrone → ombres temps réel.

### 2.3 Sauts — V2 36,73–37,47 s (trampoline, « The twins next door »)
* Deux personnages en saut sur trampoline, **phases décalées** (l'un monte quand l'autre descend) → évite l'effet « copier-coller ».
* Poses en l'air variées (bras écartés, genoux « pliés » simulés par rotation des jambes vers l'avant).
* Flou directionnel fort sur les corps en ascension → rendu avec flou de mouvement.
* Trajectoire parabolique (ralentissement au sommet, accélération en descente) — *slow in / slow out* naturel de la gravité **[FORTEMENT PROBABLE : simulation ou courbe de clés en parabole]**.

### 2.4 Cri / alarme — V3 70,50–71,23 s (« I screamed her name »)
| Phase | Images | Description |
|---|---|---|
| Neutre | f2115–f2117 | bras le long du corps, visage déjà en « choc + goutte de sueur » |
| Montée rapide | f2119–f2123 (≈ 4–5 images) | bras montent vers l'avant/haut, **fort flou** sur les bras |
| Dépassement | f2125 | bras légèrement au-delà de la pose finale |
| Tenue | f2127–f2137 | bras levés devant la poitrine, micro-mouvement |
Principes : anticipation minimale (visage avant le corps : *l'émotion précède le geste*), **ease-out** vif, *follow-through* par dépassement. Reconstruit dans `animation.js:gestureAlarm()` et `r6_story_scene.py:alarm_gesture()`.

### 2.5 « Wake up! » — V4 45,30–46,03 s
* Pia debout sur le lit penchée au-dessus du dormeur ; **alternance de deux décalques** (bouche ouverte / yeux plissés) au rythme des syllabes → « lip-flap » par swap, pas de synchro phonétique.
* Le dormeur reste immobile (yeux fermés) — contraste comique ; à 45,9 s changement d'angle (coupe sur le mot « right »).

### 2.6 Dialogue face caméra — V5 12,2–13,3 s (« He's forty-one »)
* Personnage quasi immobile ; tête légèrement tournée, barbe immobile ; caméra en légère poussée. Le « jeu » est porté par le cadrage et le sous-titre, pas par l'animation → économie de production assumée.

### 2.7 Plongeon — V5 62,20–62,53 s (« That's worse »)
* Corps rigide en rotation (salto avant) : le personnage pivote autour de la racine de ~90° en 6 images, bras tendus → animation de racine + pose figée. Pas de flou.

### 2.8 Bouche — V7 159,80–160,53 s (« he opened his mouth »)
* Décalque neutre (yeux points, bouche trait) de f4794 à f4812 ; **f4814 : bouche triangulaire ouverte** (dents blanches, langue rose) — swap en 1 image, au moment où le mot « mouth » est prononcé → la narration *déclenche* l'expression.
* Caméra en lente poussée pendant tout le passage.

### 2.9 Effondrement — V1 115,30–115,63 s
* Maisons basculant dans un gouffre, trajectoires différentes par bâtiment, aucune déformation → **corps rigides simulés** ; caméra inclinée (angle hollandais ≈ 20°) pour l'instabilité.

## 3. Principes d'animation identifiés (12 principes)

| Principe | Où | Comment |
|---|---|---|
| Squash & stretch | quasi absent (rigides) ; **appliqué aux sous-titres** (pop 70→112→100 %) | échelle du texte |
| Anticipation | V3 visage avant geste ; V4 Pia se penche avant de crier | décalage d'événements 2–5 images |
| Staging | 1 sujet par plan, centré (sous-titre au centre) | cadrage 9:16 serré |
| Straight-ahead / pose-to-pose | pose-to-pose (clés) + cycles | Moon Animator / clés Blender |
| Follow-through / overlap | dépassement des bras V3 ; cheveux/accessoires rigides (peu d'overlap) | easing outBack |
| Slow in / slow out | caméra (45–60 % des plans en ease-in-out ou ease-out mesurés) | interpolations Sine/Cubic |
| Arcs | bras en arc (rotation à l'épaule = arc par construction) | pivots |
| Secondary action | geste de la main pendant la marche (V1) | couches d'animation |
| Timing | gestes 4–7 images ; plans 1,3–2,5 s | — |
| Exaggeration | course bras horizontaux (V6), barbe géante (V2) | amplitude > réel |
| Solid drawing | volumes simples mais éclairés (ombres propres, AO) | rendu |
| Appeal | visages expressifs, couleurs saturées | bibliothèque de visages |

## 4. Ce qui évite l'effet « mannequin qui glisse »

1. **Phase du cycle liée à la distance parcourue** (pas au temps) → pas de patinage des pieds. Implémenté : `locomotion(j, dist/STRIDE*2π)`.
2. **Décélération avant l'arrêt** (slow-in) + fondu du poids de la marche vers l'idle (`weight`).
3. **Idle permanent** : respiration ~0,25 Hz, micro-balancement, clignements toutes les 2,5–4,5 s (4 images).
4. **Réactions décalées** : le second personnage réagit ~150 ms (4–5 images) après l'événement (`sisterPose`).
5. **Flou de mouvement** (pipeline B) : la différence la plus visible entre « jeu vidéo » et « film ». Reproduit par sur-échantillonnage temporel (`renderFrameMB`, testé : netteté −50 % sur les membres en mouvement, torse net).
6. **Caméra toujours légèrement en mouvement** (push-in lent) : même un personnage figé paraît vivant (76–88 % des plans ne sont pas statiques).

## 5. Implémentations fournies

| Mécanisme | Fichier | Fonction |
|---|---|---|
| Cycle marche/course | `web_threejs/src/animation.js` | `locomotion()` |
| Idle + respiration | idem | `idle()` |
| Clignement déterministe | idem | `blinkAt()` |
| Pistes de clés + easing | idem | `evalTrack()`, `Ease` |
| Geste cri avec anticipation/dépassement | idem | `gestureAlarm()` |
| Ressort critique (secondaire) | idem | `springStep()` |
| Équivalent Blender (clés BEZIER/CONSTANT) | `blender/r6_story_scene.py` | `walk_cycle()`, `alarm_gesture()`, `set_face()` |
| Équivalent Roblox | `roblox/FaceAndActing.luau` | `play()`, `talk()`, `autoBlink()`, `walkTo()` |
