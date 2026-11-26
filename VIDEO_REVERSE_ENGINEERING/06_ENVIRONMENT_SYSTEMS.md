# 06 — Systèmes d'environnement

## 1. Inventaire des décors (observé sur les 510 images clés)

| Vidéo | Décors | Échelle / densité | Remarques |
|---|---|---|---|
| V1 | rue piétonne pavée + mur blanc (ombres), boulangerie, kiosque loterie, mairie à colonnes, place centrale avec fontaine et foule, chambre, école, montagne en dôme, forêt de sapins coniques, grotte souterraine (stalactites, lumière), prairie, chantier de reconstruction | ville entière visible en plongée (≈100+ maisons colorées style nordique/Amsterdam) | maisons à pignons très colorées alignées (kit modulaire) ; dôme de roche « lowpoly » |
| V2 | banlieue américaine : maisons à étage, boîte aux lettres, trottoirs, route à marquage, montagnes enneigées et montgolfières au fond, chambre d'enfant (tapis arc-en-ciel), trampoline, buisson | panorama aérien en ouverture | ciel lavande, « carte postale » |
| V3 | rue résidentielle encombrée de voitures, chantier de gratte-ciel (poutres rouges), Hill Road + mur de briques, maison avec porche, chambre, cuisine (pizza), épicerie (étagères de bonbons), gare et passage à niveau, voie ferrée | quartier | intérieurs meublés détaillés |
| V4 | maisons type Bloxburg (bardage), jardin potager (tomates géantes), chambres, salle de bain/cuisine, magasin de parapluies, sous-sol, quartier inondé (eau), toits sous l'orage | quartier complet visible en plongée nocturne | eau animée, pluie, éclairs |
| V5 | meule de foin géante, village au pied, banque de la vache, échoppes (« Cow's hay shop », « Tool shop », « Lost & found »), cratère, plaine au coucher, bassin doré | meule = élément dominant | des milliers de brins de paille en sol et en particules |
| V6 | rue enneigée au coucher, cimetière, maison (cuisine, salon, entrée, porche), étang gelé avec bancs et roseaux | quartier + étang | neige en particules, empreintes |
| V7 | rue avec panneau « NO SLEEPING », magasin « Chairs », intérieurs (salon, chambre), bus scolaire (intérieur/extérieur), plateau TV du maire (« Wake check »), carte de la ville, quartier de nuit | ville de type Brookhaven | habillage UI/infographie intégré au décor |

## 2. Méthodes de construction identifiées

| Méthode | Indices | Vidéos | Statut |
|---|---|---|---|
| **Kits modulaires répétés** (maison = corps + toit + fenêtres) | mêmes façades répétées avec variations de couleur ; alignements réguliers | toutes | **[CONFIRMÉ visuellement]** |
| Cartes/maps Roblox existantes (« RP towns ») | intérieurs/meubles/bus caractéristiques des jeux de rôle Roblox populaires | V4, V7 | **[FORTEMENT PROBABLE]** ; nom exact du jeu **[INDÉTERMINABLE]** |
| Décors construits sur mesure | lieux uniques au scénario (grotte sous la ville, meule de foin, étang gelé, plateau TV « Wake check ») | V1, V5, V6, V7 | **[FORTEMENT PROBABLE]** |
| Instancing de végétation | arbres « boules » et sapins coniques identiques | V1, V2, V3, V6 | **[FORTEMENT PROBABLE]** |
| Particules à grande échelle | paille (V5), neige (V4, V6), pluie (V4), poussière dorée (V1 grotte) | — | **[CONFIRMÉ visuellement]** |
| Physique rigide | effondrement de la ville (V1 112–118 s) | V1 | **[FORTEMENT PROBABLE]** |
| Habillage 2D intégré (enseignes, calendriers, UI TV) | textes lisibles sur des surfaces 3D (« COW BANK », « FEBRUARY VISIT », « WAKE CHECK », « EMERGENCY DOOR ») | V4–V7 | **[CONFIRMÉ visuellement]** — textures/SurfaceGui |
| Fonds 2D / parallaxe | aucun indice : le test de parallaxe montre des fonds réellement 3D | — | **[CONFIRMÉ : non utilisé de façon dominante]** |

## 3. Composition spatiale et cohérence

* **Profondeur** : premier plan (personnage) / plan moyen (décor de rue) / arrière-plan (collines, montagnes, ciel) + brouillard atmosphérique. La plongée aérienne « établit » la ville (V1 26–29 s, V2 0–3 s, V4 66 s, V7 101 s).
* **Échelle** : l'élément du « pitch » est surdimensionné et toujours lisible (meule V5, ombre géante V1, barbe V2, tomates V4).
* **Cohérence inter-plans** : mêmes assets réutilisés d'un plan à l'autre et, chez @whatifstoriess_, d'un épisode à l'autre (maison, cuisine, chambre de Lily réapparaissent en V3 et V6 avec un autre éclairage) **[CONFIRMÉ visuellement]**.
* **Densité** : décor chargé mais peu contrasté derrière le sujet ; le sujet porte les couleurs les plus saturées → lisibilité à petite taille.

## 4. Recette de reconstruction

1. **Kit** : 10–20 modules (maison 2 tailles, toit, porche, clôture, lampadaire, arbre rond, sapin, voiture, panneau). Tout en primitives ou maillages low-poly, matériaux unis.
2. **Générateur de rue** : une ligne de lots, choix de module + couleur par PRNG à graine fixe (`world.js` : 40 maisons + 30 arbres = **6 draw calls** grâce à `InstancedMesh`).
3. **Lieux « héros »** construits à la main pour chaque épisode (1–3 par histoire) : c'est là que l'effort visuel va.
4. **Presets d'ambiance** (jour / coucher / nuit d'orage) appliqués à tout le décor (voir 08).
5. **Particules** spécifiques au concept (paille, neige, poussière dorée).

Code : `CODE_EXAMPLES/web_threejs/src/world.js` (Three.js, testé) ; `roblox/CinematicDirector.luau → applyLook()` (presets Roblox) ; `blender/r6_story_scene.py` (sol réfléchissant, mur).
