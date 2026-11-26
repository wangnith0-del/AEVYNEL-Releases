# 09 — Effets visuels

Pour chaque effet : rôle · fonctionnement · création probable · place dans le pipeline · paramètres plausibles · coût · alternative légère. Statut de présence entre crochets.

## 1. Sous-titres « pop » mot-à-mot — **[CONFIRMÉ 7/7]**
* **Rôle** : rétention (lecture sans son), rythme, emphase. Un seul mot à l'écran.
* **Observé** : apparition à ~70 % de l'échelle → dépassement ~110 % → 100 % en ~3 images (V1 « supposed », V5 « he's », V7 « OPENED »). Couleurs : jaune à contour noir (V1, V2, V5), blanc à contour noir (V3, V4, V6), MAJUSCULES blanches + mots-clés colorés en dégradé rouge/bleu/jaune (V7). Hauteur : 58–76 % de l'image selon la chaîne.
* **Création probable** : sous-titres automatiques d'un éditeur (CapCut ou équivalent) avec preset d'animation **[FORTEMENT PROBABLE]** — rendu identique entre comptes différents, typique d'un template.
* **Pipeline** : dernier calque, au-dessus des effets : pendant le fondu au blanc de V3 (74,9–75,4 s) l'image est délavée mais le mot « everything » reste blanc pur à contour noir **[CONFIRMÉ image par image]**.
* **Code** : `pipeline/captions_ass.py` (ASS `\t` d'échelle, **testé**). Coût : négligeable.

## 2. Flou de mouvement — **[CONFIRMÉ V2, V3, V6 ; absent V1, V4, V5, V7]**
* Bras flous / torse net (V3 f2119–2123), corps flous en saut (V2), course (V6).
* **Création** : flou de rendu (obturateur) d'un moteur offline **[FORTEMENT PROBABLE]** ; alternative : flou par flux optique en post (RSMB, CapCut) **[HYPOTHÈSE alternative]**.
* **Pipeline** : au rendu (avant post).
* **Paramètres** : obturateur 180° (0,5 image).
* **Coût** : ×N rendus (sur-échantillonnage) ou vecteurs de vitesse (Eevee : faible).
* **Code** : Blender `render.use_motion_blur=True, motion_blur_shutter=0.5` (testé) ; Three.js `renderFrameMB(i, n)` (testé : 8 sous-images, netteté −50 % sur membres mobiles).

## 3. Ombre sans propriétaire (« l'ombre montre le futur ») — **[CONFIRMÉ V1]**
* **Rôle** : le concept même de V1 rendu visible dès l'image 0 (silhouette d'ombre différente du personnage).
* **Création possible** : (a) Blender : objet invisible à la caméra mais projetant une ombre (`visible_camera=False`) — **testé** ; (b) Roblox : personnage masqué localement (`LocalTransparencyModifier`) dont l'ombre reste rendue **[HYPOTHÈSE]** ; (c) décalque d'ombre 2D plaqué sur le mur. L'ombre de V1 est floutée en bord comme une vraie ombre de shadow map → (a) ou (b) plus probables que (c).
* **Coût** : celui d'un personnage supplémentaire dans la shadow map.

## 4. Reflet sélectif — **[CONFIRMÉ V6 81–85 s]**
* Lily reflétée dans la glace, son frère (le mort) absent du reflet : **révélation du twist par l'image**.
* **Création** : `visible_glossy=False` (Cycles/Eevee) — **testé** ; alternative temps réel : double inversé de Lily sous une glace semi-transparente (le frère n'a pas de double).

## 5. Flash / aura dorée — **[CONFIRMÉ V3]**
* 6,2 s, 10,1–10,9 s (« A golden light flashed »), 72,6–74,1 s (« blinding golden light »), auras dorées autour du frère (113–125 s) = la « présence » de l'ange.
* **Création** : objets émissifs + bloom fort, puis fondu au blanc d'éditeur ; luma > 215 mesurée sur ces passages.
* **Paramètres** : bloom intensité élevée/seuil bas ; fondu 6–10 images.
* **Alternative légère** : calque blanc additif + flou gaussien en post.

## 6. Particules — **[CONFIRMÉ]**
| Effet | Vidéo | Création plausible | Paramètres estimés |
|---|---|---|---|
| Neige | V4 (début, 2,1 s), V6 (toute l'histoire) | ParticleEmitter / système de particules, sprites ronds flous (bokeh) | 100–300 particules visibles, vitesse 0,5–1 u/s |
| Pluie + éclairs | V4 66–126 s | particules en traînées + flash d'éclairage | flash 2–4 images |
| Paille volante | V5 partout | particules « bâtonnet » orientées + milliers de brins au sol (instancing) | brins 2D en cartes |
| Poussière dorée | V1 grotte (71–77 s) | particules lumineuses lentes | — |
| Confettis | V1 mairie 16 s | particules colorées | — |
| Étincelle ✦ | V5 0–0,7 s (aiguille dans le chignon) | sprite étoile animé | rotation + pulsation |
| Empreintes dans la neige | V6 | décalques posés au contact | — |

## 7. Masques et habillage d'écran
* **Vignette « jumelles »** (V2 47–54 s) : masque noir à deux lobes = POV **[CONFIRMÉ]** — calque PNG dans l'éditeur.
* **Insertion graphique** : flèche rouge + texte « *RANDOM KID AGAIN* » (V7 44–45 s), fiche « VISIT DAY RULE #1 » (V6), « MY BROTHER » sur le couvercle (V3 131 s) — en partie dans la 3D (textures) et en partie en 2D d'éditeur.
* **Stickers persistants** (V4) : photo d'une personne réelle en bas-droite + bonhomme de neige en bas-gauche, présents tout le long **[CONFIRMÉ]** — calques image de l'éditeur ; rôle **[HYPOTHÈSE]** : « visage » de la chaîne / signature.
* **Filigrane créateur** `@elii.rbl` semi-transparent au centre (V7) — anti-repost.

## 8. Étalonnage et post-traitement plein écran
| Effet | Vidéos | Mesure | Ordre pipeline | Code |
|---|---|---|---|---|
| Vignettage | V3 (fort), V6 (léger) | coin/centre 0,695 / 0,93 | après grade, avant texte | `post.js` `uVignette` |
| Saturation/contraste poussés | V4, V5, V3 | sat. médiane 140–165 | grade | `uSaturation`, `uContrast` |
| Accentuation (« HDR/clarity ») | V4 (visuel), V5 (indice 0,92) | indice passe-haut | après grade | FFmpeg `unsharp=5:5:0.8` |
| Réchauffement | V5, V6, V3 | R−B +33…+72 | grade | `uWarmth` |
| Bloom | V3, V6, V1 | visuel | au rendu | `UnrealBloomPass(0.3–0.8)` |
| Grain | V5/V4/V1 (bruit aplats 4,4–5,6 vs 2,5 V7) | std résiduelle | dernier effet image | `uGrain` |
| Profondeur de champ | V6, V3 | visuel | au rendu | DOF caméra |

**Ordre recommandé** (implémenté) : rendu (ombres, DOF, flou de mouvement) → bloom → tone mapping → grade → vignette → grain → **texte/stickers** → encodage.

**Coûts** (Three.js, mesuré sur SwiftShader CPU, 576×1024) : rendu complet avec post ≈ 0,2 s/image ; avec flou ×8 ≈ ×8. Sur GPU réel, le post plein écran coûte < 1 ms à cette résolution **[HYPOTHÈSE non mesurée ici : pas de GPU]**.
