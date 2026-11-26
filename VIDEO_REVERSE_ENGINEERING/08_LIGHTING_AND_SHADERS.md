# 08 — Éclairage et matériaux

Mesures : `ANALYSIS_DATA/*_grade.json` (échantillonnage 3 images/s sur toute la durée, carte de fin exclue) ; observations sur images pleine résolution. Les valeurs de paramètres proposées sont des **estimations** à ajuster à l'œil.

## 1. Empreinte colorimétrique mesurée (médianes ; p10–p90 dans les JSON)

| | Saturation (0–255) | Chaleur R−B | Contraste (σ luma) | Coin/centre (vignettage) | % noirs écrasés | Lecture |
|---|---|---|---|---|---|---|
| V1 | 108 | +10 | 49 | 0,98 | 0,4 | plein jour neutre, ciel bleu, herbe très verte |
| V2 | 89 | −3 | 48 | 1,07 | 0,3 | pastel lavande, « golden hour » doux |
| V3 | 140 | +33 | 60 | **0,695** | 0,1 | chaud, saturé, **vignettage fort constant** |
| V4 | **153** | −15 | 58 | 0,96 | 1,1 (p90 12,7) | sur-saturé + accentuation, nuits bleues |
| V5 | **165** | **+72** | 40 | 1,09 | 0,1 | or/jaune (foin), ciel bleu pur |
| V6 | 130 | +44 | 50 | 0,93 | 0,2 | coucher de soleil orange/rose, neige |
| V7 | 134 | +17 | **77** | 1,03 | **17,1** | très contrasté, beaucoup de scènes nocturnes |

## 2. Schémas d'éclairage par famille

### Pipeline A — capture Roblox (V1, V4, V5, V7)
* **Clé** : soleil directionnel unique (ombres nettes, légèrement adoucies : V1 mur 0–3 s, V1 prairie 59 s).
* **Remplissage** : ambiant/ciel uniforme (ombres jamais noires sauf V7 nuit).
* **Pas d'éclairage indirect coloré** visible (pas de rebond vert de l'herbe sur les personnages).
* Nuit (V4, V7) : lumière ambiante bleue + sources ponctuelles (fenêtres, lampadaires, écrans « Wake check » émissifs).
* Effets : bloom léger, atmosphère/brume en plan large, rayons de soleil (V1 grotte : faisceaux étroits **[HYPOTHÈSE : pièces néon/Beam plutôt que volumétrie réelle]**).
* Correspondance Roblox plausible : `Lighting.Technology = Future`, `Atmosphere`, `BloomEffect`, `ColorCorrectionEffect`, `SunRaysEffect` → `CinematicDirector.applyLook()`.

### Pipeline B — rendu offline (V2, V3, V6)
* **Ombres douces** à pénombre large et **occlusion ambiante** de contact (pieds, coins des meubles) — V3/V6 intérieurs.
* **Profondeur de champ** avec fond flou (V6 gros plans).
* **Réflexions** sur surfaces brillantes : glace de l'étang **sélective** (V6 81–85 s : Lily reflétée, son frère non), sirop des pancakes spéculaire (V6 36,7 s).
* **Éclairage chaud directionnel bas** (coucher) + ciel orange/rose → V6 ; lampes intérieures chaudes → V3 chambre/cuisine.
* Correspondance Blender plausible : Eevee/Cycles, soleil avec `angle` 2–5° (pénombre), AO, DOF caméra, `visible_glossy=False` pour le reflet sélectif → `r6_story_scene.py` (**testé**).

## 3. Matériaux

| Matériau | Où | Modèle plausible | Paramètres estimés |
|---|---|---|---|
| Plastique mat (corps, décor) | partout | PBR diélectrique | roughness 0,6–0,8 ; metalness 0 |
| Plastique lisse (V2/V3/V6) | personnages | PBR + bevel | roughness 0,4–0,5 ; arêtes arrondies |
| Glace | V6 étang | PBR brillant sombre | roughness 0,05–0,15 ; base sombre violacée |
| Sirop/aliments | V6 pancakes, V3 pizza | PBR spéculaire | roughness 0,2–0,3 |
| Émissif doré | V3 plumes/aura, V3 bocal | emission + bloom | emission ×3–5 ; bloom fort |
| Neige | V4, V6 | diffus blanc légèrement bleuté | roughness 0,9 |
| Eau (inondation) | V4 | eau Roblox/terrain ou plan transparent animé | réflexion du ciel orageux |
| Textures basse résolution | vêtements, visages (V4, V7) | filtrage bilinéaire visible | 64–512 px |

Aucun indice de subsurface scattering, réfraction complexe ou normal maps détaillées **[CONFIRMÉ visuellement : non nécessaire au style]**.

## 4. Lumière et narration

| Moment | Lumière | Effet |
|---|---|---|
| Exposition de la règle | plein jour neutre/saturé | monde « normal », lisible |
| Mystère/menace | assombrissement, ciel orageux (V4 66 s→), nuit (V7 minuit), grotte (V1) | tension |
| Miracle | **flash doré** + bloom (V3 « golden light ») | surnaturel, révélation |
| Deuil/adieu | **coucher de soleil** (V6 entier, V3 fin) puis bleu-violet après le coucher (V6 114–120 s) | le soleil qui se couche = la fin de la « visite » : la lumière **est** l'horloge narrative |
| Résolution | retour au jour clair (V1 nouvelle ville, V5 fête, V7 matin) | apaisement |

## 5. Reproduction (Three.js, testé)

`web_threejs/src/world.js` : `HemisphereLight` (ciel/sol) + `DirectionalLight` avec `PCFSoftShadowMap` 2048², `shadow.radius=4`, `Fog`. Presets `day` / `sunset`. Tone mapping ACES, puis grade en espace d'affichage (`post.js`).

```js
// preset "sunset" (V6-like) — valeurs estimées
{ sky: 0xf08a5d, ground: 0x7a5c8f, sun: 0xffb070, sunI: 2.2, hemiI: 0.6, fog: 0xc98aa0, sunPos: [-12, 4, -6] }
```
