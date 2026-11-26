# 13 — Performances et optimisation

## 1. Ce qui a été réellement mesuré ici

| Mesure | Environnement | Résultat |
|---|---|---|
| Rendu Three.js 576×1024, ombres PCF soft 2048², bloom + grade, 2 personnages, 40 maisons + 30 arbres instanciés | Chromium headless, **SwiftShader (CPU, sans GPU)**, 4 vCPU | 180 images en 37,5 s ≈ **0,21 s/image** (inclut le transfert PNG) |
| Idem avec flou de mouvement 8 sous-images | idem | ≈ 1,75 s/image (2 images en 3,5 s) |
| Blender 4.2 Cycles CPU, 576×1024, 24 échantillons + débruitage, flou de mouvement | bpy, 4 vCPU | 4 images en 81 s ≈ **20 s/image** (inclut import de bpy et construction de scène) |
| Draw calls du décor Three.js | — | **6** pour 40 maisons + 30 arbres (InstancedMesh) + quelques maillages uniques |

Rien n'a été mesuré sur GPU (aucun GPU disponible) : les chiffres GPU ci-dessous sont des **ordres de grandeur [HYPOTHÈSE]**.

## 2. Complexité des scènes observées

* Géométrie : primitives et low-poly ; une ville entière reste en dizaines de milliers de triangles.
* Points lourds : **ombres** (shadow maps), **particules** (paille V5, neige V6), **post plein écran**, et pour le pipeline B le **nombre d'échantillons** et le flou de mouvement.
* Textures : basse résolution (décalques/vêtements Roblox) → RAM/VRAM faibles.

## 3. Leviers par ordre de rapport qualité/coût

| Levier | Gain | Perte visuelle | Notes |
|---|---|---|---|
| **Instancing** des kits | ×10–×100 draw calls | aucune | `world.js` |
| **Rendu image par image hors temps réel** | qualité indépendante de la puissance | aucune | `render.mjs` : même un PC faible rend parfaitement, juste plus lentement |
| Résolution de rendu = résolution de diffusion utile | 1080×1920 suffit ; TikTok redescend à 576×1024 en téléchargement | nulle à la diffusion | ne pas rendre en 4K |
| Shadow map bien cadrée (frustum serré autour de l'action) | netteté ×2 à taille égale | aucune | `shadow.camera` left/right/top/bottom |
| Frustum culling (natif) | auto | — | garder `frustumCulled = true` |
| LOD : maisons lointaines en boîtes sans fenêtres | 30–60 % géométrie | invisible à 576 px | — |
| Flou de mouvement seulement sur les plans d'action | ×N seulement là où ça se voit | aucune ailleurs | `MB=6` par plan |
| Eevee au lieu de Cycles (pipeline B) | ×10–×50 vitesse | GI moins exacte | suffisant pour ce style |
| Particules : sprites + densité adaptée au cadre | — | — | la paille V5 = cartes instanciées |
| Cache des décors entre épisodes (V3/V6) | temps de production | — | réutilisation d'assets |

## 4. Trois configurations de reproduction

### Légère — ordinateur peu puissant (iGPU, 8 Go RAM)
* Three.js (ce dossier) en **rendu offline image par image** (`render.mjs`), 1080×1920 ou 720×1280.
* Ombres 1024², `PCFSoftShadowMap`, bloom 0,3, pas de flou de mouvement (ou `MB=4` sur les plans d'action uniquement).
* Particules ≤ 300.
* Estimation : 0,2–0,5 s/image (mesuré 0,21 s/image en CPU pur à 576×1024) → 2 min de vidéo ≈ 15–60 min de rendu.

### Intermédiaire — PC standard (GPU milieu de gamme)
* Roblox Studio + capture OBS 1080p60 (pipeline A) **ou** Three.js avec `MB=6` partout.
* Ombres 2048², DOF sur gros plans, grain/vignette.
* Rendu Three.js temps quasi réel ; capture Roblox en temps réel.

### Avancée — station de travail
* Blender Eevee (ou Cycles 64–128 échantillons + débruitage) : flou de mouvement, AO, DOF, réflexions sélectives.
* Rendu en séquences EXR/PNG, compositing, 1080×1920.
* Estimation Eevee GPU : 0,5–3 s/image **[HYPOTHÈSE]** ; Cycles GPU 5–20 s/image **[HYPOTHÈSE]** (mesuré ici ≈ 20 s/image en Cycles **CPU** à 24 échantillons).

## 5. Meilleur rapport qualité/performance

1. Rendu **déterministe hors temps réel** (aucune image perdue, qualité constante).
2. **Instancing + presets d'éclairage** (le décor ne coûte presque rien).
3. **Flou de mouvement par sous-échantillonnage seulement sur les plans d'action** : c'est l'effet qui rapproche le plus le rendu temps réel du rendu « film » (pipeline B), pour un coût ciblé.
4. Post léger (bloom + grade + vignette + grain dans un seul shader).
5. Ne pas sur-investir dans la géométrie : la diffusion se fait à 576–1080 px de large.
