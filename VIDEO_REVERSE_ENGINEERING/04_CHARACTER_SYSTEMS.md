# 04 — Systèmes de personnages

Sources : planches-contact de tous les plans (`KEYFRAMES/`), images pleine résolution, bandes image-par-image (`tools/frame_strip.py`). Descriptions = observations **[CONFIRMÉ visuellement]** sauf mention.

## 1. Construction commune : le rig « R6 »

Les 7 vidéos utilisent la même topologie de personnage **[CONFIRMÉ]** :

| Élément | Observation | Construction technique |
|---|---|---|
| Corps | 6 blocs rigides : tête, torse, 2 bras, 2 jambes ; proportions torse 2×2×1, membres 1×2×1, tête ~1,2 (unités « studs ») | Primitives (cubes) ou maillages Roblox R6 ; **aucune déformation** visible (ni coude, ni genou, ni skinning) |
| Articulations | rotations autour des épaules, hanches, cou uniquement | Hiérarchie parent-enfant avec pivots aux articulations (Roblox `Motor6D` ; Blender objets parentés/armature à 1 os par membre) |
| Visage | dessin 2D plaqué sur la face avant de la tête | Décalque/texture ; changements d'expression **instantanés** (V7 f4812→f4814 : bouche « trait » → « triangle ouvert » sans intermédiaire) |
| Cheveux, chapeaux, barbes | volumes 3D posés sur la tête | Accessoires maillés (catalogue Roblox / UGC) ; texture striée fine sur les cheveux bouclés (V6) |
| Vêtements | textures 2D sur les blocs (rayures, plaid, imprimés, logos « PH », étoile) | « Classic shirts/pants » Roblox (textures basse résolution, visiblement pixelisées en gros plan V4/V7) ou textures équivalentes |

**Pourquoi ça fonctionne** : la lisibilité vient de la silhouette et de la couleur, pas du détail anatomique. Un rig à 6 os s'anime vite, se réutilise d'une vidéo à l'autre et reste lisible à 576 px de large.

**Topologie observable** : boîtes biseautées légèrement arrondies (V2, V3, V6 : arêtes adoucies → bevel / « smooth plastic ») vs arêtes vives (V4, V7 : rendu Roblox standard). Indice de famille de rendu, voir `14_COMPARATIVE_ANALYSIS.md`.

## 2. Fiches personnages par vidéo

### V1 — « Shadow » (@jexario)
| Personnage | Signes distinctifs | Rôle |
|---|---|---|
| Narrateur | cheveux blonds en houppe, veste turquoise à liseré orange sur t-shirt blanc logo soleil, jean marine | protagoniste, présent de 0 s à la fin |
| Voisin | cheveux gris, haut rouge | exposition (chèque géant/loto) |
| Ami d'école | chemise verte | exposition (contrôle raté) |
| Passants « sans ombre » | femme, homme d'affaires (costume), policier | montée du mystère |
| Maire | âgé, cheveux blancs, costume violet | résolution (évacuation) |
| Foule | ≥30 avatars variés (place, 43–47 s ; prairie, 102–109 s) | échelle de la ville |
Particularité : **l'ombre est un personnage** (silhouette différente de son propriétaire, 0–3 s, 52–56 s, 128–139 s) — voir 09 §ombre.

### V2 — « Mailman » (@pawranoid.pets)
| Personnage | Signes | Rôle |
|---|---|---|
| Narrateur (enfant) | cheveux roux bouclés, mini-moustache, maillot rayé vert/jaune/rouge, salopette bleue à pièces rouges | protagoniste |
| Papa | très grand, chauve, énorme barbe noire volumineuse, chemise à carreaux rouge, jean | contraste visuel avec le fils |
| Facteur | cheveux roux bouclés, moustache, uniforme bleu, casquette, sacoche | « vrai père » sous-entendu |
| Maman | robe rouge à sequins | chute comique |
| Jumeaux, bébé à moustache | mêmes cheveux roux | gag d'accumulation |
Visages : **dessins expressifs personnalisés** (sourcils, reflets dans les yeux, joues roses), pas les décalques Roblox classiques → atelier graphique dédié **[FORTEMENT PROBABLE]**.

### V3 & V6 — « Guardian angel » / « The visit » (@whatifstoriess_) — **mêmes personnages**
| Personnage | Signes | V3 | V6 |
|---|---|---|---|
| Narrateur (frère, 12 ans) | peau jaune classique, cheveux noirs bouclés, sweat orange imprimé « PH », poignets jaunes, jean, baskets à triangle rouge | ✓ | ✓ |
| Lily (7 ans) | cheveux bruns, nœud rose (V3) / bonnet rose à pompon (V6), haut rose étoile jaune (V3) / doudoune rose (V6) | ✓ | ✓ |
| Biscuit (chien) | beagle cubique, grands yeux expressifs, modèle dédié | ✓ | ✓ |
| Maman / Papa / Grand-père | Maman brune ; Papa chemise à carreaux (V6) ; Grand-père en portrait (V3) | ✓ | ✓ |
Visages : sourire « classique » + variantes dessinées (larmes bleues, goutte de sueur, yeux ronds) — swaps instantanés. **Réutilisation d'assets et de casting entre épisodes** **[CONFIRMÉ visuellement]**.

### V4 — « Weather » (@xxvideo.25)
Grand-mère (bonnet/cheveux violets, pyjama violet à motifs), narrateur (cheveux bruns, haut rayé vert), Pia (couettes en chignons, pyjama rose à cœurs), M. Grimsby (costume noir, cravate rouge, tête blanche à moustache), coq de M. Ortiz (modèle maillé), Papa (chemise bleue). Visages : **décalques Roblox du catalogue** (expressions « meme » : yeux plissés, bouche ouverte rouge). Avatars type Bloxburg/Brookhaven **[FORTEMENT PROBABLE]**.

### V5 — « Golden needle » (@goopie.yt)
Eli (cheveux bruns en pointes, t-shirt bleu étoile jaune, pantalon marine, chaussures rouges), Grand-mère (chignon blanc, gilet et jupe violets, perles — l'aiguille d'or est dans son chignon dès la première image : éclat ✦ visible sur le chignon de 0,00 à ~0,70 s **[CONFIRMÉ image par image]**, avant que la caméra ne recule), chercheur de 41 ans (cheveux longs et barbe immense), oncle (haut-de-forme), maire (haut-de-forme, monocle, écharpe), vache banquière (maillage dédié, lunettes de soleil, chaîne en or), Kevin la grenouille (maillage vert). Visages : décalques simples (yeux/sourcils/bouche) proches du style Roblox.

### V7 — « No sleep » (@elii.rbl)
Eli (chemise rouge, cheveux auburn, peau claire), Ava (couettes noires, haut rayé noir/blanc, ours en peluche), Maire (haut-de-forme, costume noir, tête blanche), Random Kid (peau foncée, cheveux noirs, chemise blanche cravate noire / sweat à capuche), policiers, chauffeur. Visages : **décalques Roblox classiques** très agrandis → texels visibles **[CONFIRMÉ]** ; « parole » par swap bouche fermée/ouverte.

## 3. Cohérence d'identité entre les plans

Mécanismes observés **[CONFIRMÉ]** :
1. **Palette verrouillée** par personnage (le sweat orange « PH » est identique sur 2 vidéos distinctes).
2. **Un trait de silhouette unique** : barbe géante (Papa V2), haut-de-forme (maires V5/V7), couettes (Ava, Pia), bonnet rose (Lily V6).
3. **Accessoire-signature** récurrent : ours en peluche d'Ava, bocal de plumes de Lily, montre de Papa (V4).
4. **Nom prononcé + plan sur le visage** au même moment (le sous-titre affiche le nom pendant le gros plan).
5. Asset unique sauvegardé et réutilisé (pas recréé par plan) → cohérence parfaite inter-plans et inter-épisodes.

## 4. Reproduire un personnage

| Méthode | Quand | Exemple fourni |
|---|---|---|
| Primitives procédurales + visage canvas | Web, prototypage, contrôle total | `web_threejs/src/character.js` (`buildCharacter`, `drawFace` : neutral/smile/shock/sad/yell/sleep) |
| Rig R6 importé + décalques | Roblox | `roblox/FaceAndActing.luau` (`setFace`, `talk`, `autoBlink`) |
| Primitives Blender + matériau de visage à facteur clé « CONSTANT » | Rendu offline | `blender/r6_story_scene.py` (`build_r6`, `face_material`, `set_face`) |
| Import d'avatars Roblox dans Blender | Pipeline B réaliste | export `.obj/.fbx` depuis Studio puis matériaux ; **[HYPOTHÈSE]** quant à l'usage par les créateurs V2/V3/V6 |

Recommandation : **factory paramétrique** (couleurs, accessoires, jeu de visages) + **bibliothèque de visages** commune (≥8 expressions : neutre, sourire, rire, choc, peur, triste/larmes, colère, endormi) ; chaque personnage = un JSON. C'est ce qui permet le casting récurrent de V3/V6.
