# 03 — Timeline complète

Deux niveaux :
1. **Temps forts annotés** (manuellement, à partir des planches-contact de tous les plans, des bandes image par image et des transcriptions) : visuel, personnages, caméra, lumière/VFX, son, technique, difficulté (★ facile → ★★★ difficile), confiance.
2. **Tableau exhaustif des 510 plans** (généré par `tools/build_timeline.py` à partir des mesures) : timecodes, durée, narration exacte pendant le plan, mouvement de caméra mesuré, easing, verdict 3D/2D, luminance, saturation, lien vers l'image clé.

Limites : la détection automatique sous-compte les micro-plans des séquences de montage rapide (V5 79,5–81,3 s) et peut fusionner deux plans très semblables ; concordance 81–100 % avec le détecteur de scènes FFmpeg (`ANALYSIS_DATA/shot_detection_crosscheck.txt`). Le dernier plan de chaque vidéo est la carte de fin TikTok (hors production).

---

## Partie 1 — Temps forts annotés

### V1 « Shadow » (0–143 s, contenu 0–138,6 s)
| TC | Narration | Visuel | Caméra | Lumière / VFX | Son | Technique probable | Diff. | Conf. |
|---|---|---|---|---|---|---|---|---|
| 0,0–8,3 | règle : l'ombre montre le futur (+24 h) | narrateur devant un mur blanc ; **son ombre a une autre silhouette** ; plans : boulangerie, ombre d'une vieille dame avec canne | poussées lentes, plans fixes | soleil dur, ombres nettes | voix dès 0,00 ; bed léger | ombre d'un double invisible (Roblox local transparency ou Blender camera-invisible) | ★★ | ombre CONFIRMÉE ; méthode HYPOTHÈSE |
| 8,3–31,1 | exemples : voisin + chèque → loterie → millionnaire ; ami + contrôle raté → révise | ombres « jouant » le futur ; kiosque loterie ; mairie avec confettis et chèque « $1,000,000 » ; chambre/bureau | fixes + dérives | confettis (particules) | — | décors modulaires, particules | ★★ | FORT |
| 31,1–56,8 | mystère : les gens perdent leur ombre | femme au soleil sans ombre ; homme d'affaires ; policier ; place pleine de foule | dérives lentes, plan d'ensemble de la place | ombres absentes : objets `CastShadow=false` | — | toggle d'ombre par personnage | ★ | FORT |
| 56,8–64,1 | l'ombre du narrateur le montre sur la montagne | montagne-dôme, sapins ; marche vers la montagne (59–61 s, marche R6 + geste de main) | frontal fixe | plein jour | — | animation en couches (marche + geste) | ★ | CONFIRMÉ (image par image) |
| 64,1–90,0 | fissures, grotte sous la ville, la ville va s'effondrer | fissures autour de la ville ; grotte immense (stalactites, poussière dorée, faisceaux) ; coupe de la ville au-dessus du vide | plongées, plan large | ambiance chaude, faisceaux, particules | — | lieu héros construit sur mesure | ★★★ | FORT |
| 90,7–108,1 | évacuation | maire ; bus ; familles ; foule sur la colline ; **les ombres reviennent** | travellings, plans larges | jour | — | foule instanciée | ★★ | FORT |
| 108,6–119,2 | la ville s'effondre | maisons basculant dans le gouffre (113–118 s), **angle hollandais ~20°** | plan large incliné | — | — | simulation corps rigides, sans flou | ★★★ | FORT |
| 119,6–138,6 | reconstruction ; l'ombre entourée de monde | chantier (grue), nouvelle école plus grande, ombre-fête au mur | dérives | jour | bed final | — | ★★ | FORT |

### V2 « Mailman » (0–74,9 s, contenu 0–70,8 s)
| TC | Narration | Visuel | Caméra | Lumière / VFX | Son | Technique | Diff. | Conf. |
|---|---|---|---|---|---|---|---|---|
| 0,0–2,9 | règle : chaque enfant ressemble à son père | survol aérien descendant de la banlieue, montagnes, montgolfières | **drone descendant** (flux croissant 0→3,9 px/img) | pastel lavande | voix 0,00 | caméra sur spline | ★★ | CONFIRMÉ |
| 2,9–8,6 | « Huss huss… » même nez, cheveux, rire | père/fils identiques (basketteurs « 7 », lunettes) — gag visuel | poussées rapides avec flou | flou de mouvement | gag vocal « huss » | rendu offline | ★★ | CONFIRMÉ |
| 8,6–14,1 | sauf moi : papa chauve, barbe ; moi roux, mini-moustache | contre-plongée sur Papa géant ; gros plan narrateur | contre-plongée | — | — | — | ★ | CONFIRMÉ |
| 14,3–34,4 | le facteur roux et moustachu vient 3×/jour… | facteur, boîte aux lettres, anniversaire, vélo, soupe par la fenêtre | push-in quasi systématiques | — | — | visages dessinés sur mesure | ★★ | CONFIRMÉ |
| 34,8–43,0 | les jumeaux, le gamin d'en face, le bébé à moustache | trampoline (sauts déphasés, flou), bébé en poussette | — | flou de mouvement | — | — | ★★ | CONFIRMÉ (image par image) |
| 43,1–57,8 | enquête : jumelles, voiture de papa part, facteur sonne, maman en robe, rideaux | **POV jumelles** (masque noir 2 lobes), sonnette, maman en robe rouge, rideaux | POV, push-in | masque PNG | — | calque d'éditeur | ★ | CONFIRMÉ |
| 57,8–66,0 | « je les ai entendus… » (silence 3,1 s) → « maman l'aide à s'entraîner » | façade, boîte aux lettres, narrateur perplexe | — | — | **pause 3,1 s** + « huss » | gag par le silence | ★ | CONFIRMÉ |
| 66,4–70,8 | monte sur la poubelle, visage contre la vitre, et… | fin sur **très gros plan visage choqué** (« glass ») | gros plan | — | coupe sèche | fin ouverte | ★ | CONFIRMÉ |

### V3 « Guardian angel » (0–138,8 s, contenu 0–131,6 s)
| TC | Narration | Visuel | Caméra | Lumière / VFX | Son | Technique | Diff. | Conf. |
|---|---|---|---|---|---|---|---|---|
| 0,0–7,2 | règle : un ange gardien vous sauve | rue encombrée en plongée fixe ; gens ; **flash blanc 6,2 s** | plongée statique | flash | voix | fondu au blanc | ★ | CONFIRMÉ |
| 7,7–18,8 | ouvrier du gratte-ciel, bus sans freins, plume d'or | chantier (poutres rouges), **flash doré 10,1–10,9 s**, bus scolaire, mur de briques, plume | poussées, contre-plongées | émissif + bloom | — | VFX lumière | ★★ | CONFIRMÉ |
| 19,4–34,1 | moi 12 ans, Lily 7 ans, 11 plumes dans un bocal ; grand-père | présentation des personnages ; bocal lumineux ; portrait du grand-père | push-in | lampe chaude, vignette forte | — | — | ★★ | CONFIRMÉ |
| 34,5–58,2 | routine : école, selfies au rayon bonbons, Biscuit, pizza, « Jinx », « Sure, sweetheart » | **indices plantés** : Lily parle seule, selfie, chien qui suit, maman qui répond | variés | intérieurs chauds | — | setup du twist | ★★ | CONFIRMÉ |
| 58,5–79,1 | passage à niveau : barrière, sac coincé, train, cri, **lumière dorée aveuglante** | gare, feux, barrière ; cri (bras levés en 5 images, flou) ; **72,6–74,1 s blanc** puis fondu depuis le blanc (74,9–75,4 s) | rapide, push-in ease-in | flash + bloom + fondu | montée | flou de mouvement de rendu | ★★★ | CONFIRMÉ (image par image) |
| 79,8–98,9 | « Number 12 », Lily pleure vers les rails : « I always knew it was you » ; souvenir : il est mort il y a 3 ans | Lily seule, rails vides ; flash-back | dérives lentes | coucher | **bed plus dense dès ~80 s** | — | ★★ | CONFIRMÉ (mesure audio) |
| 99,2–125,2 | relecture des indices ; « I never had one. I am one. » | rappel des plans (selfies : un seul enfant, Biscuit), **aura dorée** autour du frère | push-in | aura émissive | — | — | ★★ | CONFIRMÉ |
| 125,7–131,6 | 12e plume, couvercle « MY BROTHER » | insert couvercle écrit, chambre | insert | lumière chaude | fin | texture texte | ★ | CONFIRMÉ |

### V4 « Weather » (0–130,5 s, contenu 0–126,4 s)
| TC | Narration | Visuel | Caméra | Lumière / VFX | Son | Technique | Diff. | Conf. |
|---|---|---|---|---|---|---|---|---|
| 0,0–12,2 | règle : le premier réveillé choisit la météo ; Grand-mère « Sunny and 75 » | Grand-mère **surgit dans le cadre à 0,6 s** ; neige ; réveil 3:00 ; arc-en-ciel | poussées linéaires, flux élevé au départ | **neige en particules**, filtre saturé + accentué | voix | capture Roblox + filtre | ★ | CONFIRMÉ |
| 12,6–29,0 | tomates géantes, 14 réveils, coq de M. Ortiz | potager, enfants priant, coq | push-in | — | — | — | ★ | CONFIRMÉ |
| 29,0–49,0 | moi, le plus gros dormeur ; Pia saute sur le lit « Wake up! » | narrateur endormi partout ; Pia (alternance de 2 visages au rythme du cri) | — | — | réplique aiguë | swap de décalques | ★ | CONFIRMÉ (image par image) |
| 49,2–74,6 | M. Grimsby, magasin de parapluies, dort au sous-sol, choisit l'ouragan | magasin, sous-sol, réveil 12:00, **orage** | — | pluie, éclairs, nuit bleue | — | particules + éclairage | ★★ | CONFIRMÉ |
| 74,8–98,2 | parapluies à 100 $ en barque ; 6e jour ; la ville sur les toits ; rien ne marche | inondation, barque, toits, calendrier | plongées | eau, pluie | — | eau Roblox | ★★ | FORT |
| 98,4–119,4 | il s'endort exprès sur le toit à 11:59:58 | **inserts montre 11:58 / 11:59:57 / 11:59:58** ; tonnerre | inserts | éclair | tonnerre | — | ★ | CONFIRMÉ |
| 119,7–126,4 | « Three, two, one » — Pia : « Wake up! » | Pia saute sur lui | — | — | chute | — | ★ | CONFIRMÉ |

### V5 « Golden needle » (0–119,8 s, contenu 0–115,1 s)
| TC | Narration | Visuel | Caméra | Lumière / VFX | Son | Technique | Diff. | Conf. |
|---|---|---|---|---|---|---|---|---|
| 0,0–1,1 | « In this town… » | **gros plan Grand-mère, éclat ✦ sur le chignon** → recul aérien continu jusqu'à la meule | **reveal 1,1 s sans coupe, flux 4→20 px/img** | soleil, ciel nuageux | voix 0,00 | caméra animée exponentielle | ★★ | CONFIRMÉ (image par image) |
| 1,1–14,6 | 5 M de brins, une aiguille d'or ; le chercheur de 41 ans | meule géante, intérieur doré (étincelle), chercheur barbu | push-in | paille en particules | — | instancing de brins | ★★★ | CONFIRMÉ |
| 14,9–41,9 | tout le monde creuse ; la vache paie 1 pièce/brin ; outils ; dynamite ; cratère ; tricheur | banque de la vache (lunettes, chaîne), échoppes, souffleur, dynamite, cratère | push-in | — | — | modèles sur mesure (vache) | ★★ | CONFIRMÉ |
| 42,3–44,6 | **CTA** « check my profile » | — | — | — | — | — | ★ | CONFIRMÉ |
| 44,9–69,6 | Grand-mère traverse la meule ; moi et ma cuillère ; Kevin la grenouille ; papa disparu | **plongeon** (rotation de racine), grenouille | — | — | — | — | ★★ | CONFIRMÉ |
| 69,8–83,7 | toute la ville creuse 3 jours | **montage rapide ≈ 10 plans de 4–6 images**, **meule qui rétrécit** (81,4–81,8 s) | — | — | — | montage + animation d'échelle | ★★ | CONFIRMÉ (image par image) |
| 83,9–93,7 | le dernier brin : rien, juste Kevin ; la vache rote | plaine au coucher, maire, trou avec grenouille | contre-plongées | coucher | silence relatif | — | ★★ | CONFIRMÉ |
| 93,9–115,1 | l'aiguille était la barrette de Grand-mère ; « Did you see it before I did? » | Grand-mère, bassin doré de Kevin, place en fête | push-in | doré | — | **payoff de l'indice de l'image 0** | ★ | CONFIRMÉ |

### V6 « The visit » (0–124,1 s, contenu 0–116,2 s)
| TC | Narration | Visuel | Caméra | Lumière / VFX | Son | Technique | Diff. | Conf. |
|---|---|---|---|---|---|---|---|---|
| 0,0–21,6 | règle : les morts reviennent un jour ; pas de miroir ; empreintes qui fondent ; ne jamais leur dire | rue enneigée au coucher, cimetière, calendrier « VISIT », fiche « RULE #1 », grand-père | coupe à 0,5 s, poussées | neige, coucher | voix | rendu offline | ★★ | CONFIRMÉ |
| 22,2–44,6 | miroirs couverts, journal caché, pancakes ; Lily (7) tombée dans l'étang ; « today was Lily's visit » | miroir drapé, **pancakes au sirop spéculaire**, Lily, visages en larmes | push-in ease-in-out | intérieurs chauds, DOF | — | matériaux PBR | ★★ | CONFIRMÉ |
| 45,0–62,4 | journal caché, TV débranchée, « onions » ; Lily marche dans mes pas ; Biscuit gémit ; papa mémorise un visage | marche dans la neige, chien sous le porche, papa | travellings | neige | **bascule musicale 60,9 s (+27 dB graves)** | cue musical au pivot | ★★ | CONFIRMÉ (mesure) |
| 63,0–79,1 | Lily court vers l'étang ; poursuite ; « This is where you saved me » | **course** (cycle ≈ 28 images, flou), étang au coucher | travelling arrière | soleil bas | nappe grave | flou de mouvement de rendu | ★★★ | CONFIRMÉ (image par image) |
| 79,6–97,4 | **reflet : Lily seule**, une seule trace de pas ; « it was mine » | **reflet sélectif** dans la glace ; empreintes uniques | plongées | reflet glossy | — | `visible_glossy=False` (testé) | ★★★ | CONFIRMÉ |
| 97,9–116,2 | « Why did you tell me? » ; adieu ; « Stay off the ice » ; coucher | câlin, soleil qui se couche, bleu après le coucher, Lily repart seule | lents | **coucher = horloge narrative** | fin | — | ★★ | CONFIRMÉ |

### V7 « No sleep » (0–167,2 s, contenu 0–162,3 s)
| TC | Narration | Visuel | Caméra | Lumière / VFX | Son | Technique | Diff. | Conf. |
|---|---|---|---|---|---|---|---|---|
| 0,0–16,0 | règle : dormir est interdit ; le maire n'a pas dormi depuis 40 ans ; chaises seulement ; amendes | panneau « NO SLEEPING », plateau TV « DAYS AWAKE 14,610 », magasin « CHAIRS », policiers à lampes | push-in ease-in | jour → nuit | voix | capture Roblox, infographies dans le décor | ★★ | CONFIRMÉ |
| 16,0–35,5 | « wake check » à minuit sur toutes les TV ; maisons éteintes choisies d'abord ; Ava 6 ans épuisée | plateau TV, téléphone « WAKE CHECK LIVE 12:00 », carte « CALLING… » | push-in | émissifs bleus | — | habillage UI 3D | ★★ | CONFIRMÉ |
| 35,9–58,4 | promesse à Ava ; Random Kid dans le bus, burger, ne parle jamais | bus scolaire (int./ext.), insertion « *RANDOM KID AGAIN* » + flèche, **passage gris/blanc 44,3–45,5 s** | gros plans pixelisés | flash | rires | décalques Roblox agrandis | ★ | CONFIRMÉ |
| 58,7–77,0 | il fredonne → tout le bus s'endort ; garage 6 h plus tard | visages endormis, garage | — | — | fredonnement | — | ★ | CONFIRMÉ |
| 77,0–101,2 | plan : seule maison éteinte = celle de Random Kid | carte, rue de nuit, police, explication | — | nuit | — | — | ★★ | CONFIRMÉ |
| 101,5–115,6 | minuit, appel en direct « Are you sleeping? Say something » | plateau du maire, visage de Random Kid, **bouche qui s'ouvre** | push-in | écrans | répliques du maire | swap de décalque sur le mot | ★ | CONFIRMÉ (image par image) |
| 115,6–124,2 | **berceuse chantée** | toute la ville s'endort | — | — | **musique retirée, chant ~557 Hz** | son diégétique | ★★ | CONFIRMÉ (mesure) |
| 124,6–162,3 | tous dorment, le maire aussi ; « sleep check » à 21 h ; « je ne connais toujours pas son nom » → endormi | réveil collectif, maire heureux, chute au garage | — | jour | bed plein (+29 dB graves 124 s) | chute en boucle | ★ | CONFIRMÉ |

---

## Partie 2 — Tableau exhaustif des plans (mesuré)

### V1 — `856391f0-v26044gc0000dc3vmpfog65mstlrss6g.mp4` — 4290 frames, 48 shots

| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 00:00.00 | 00:03.30 | 3.30 | In this town, your shadow shows your future. | push_in | ease_out (fast start, decelerating) | 3D | 172 | 76 | [img](KEYFRAMES/V1/V1_shot000_0000.00s.jpg) |
| 1 | 00:03.30 | 00:05.73 | 2.43 | Whatever your shadow is doing right now is exactly | slow_drift | ease_in_out | 3D | 172 | 65 | [img](KEYFRAMES/V1/V1_shot001_0003.30s.jpg) |
| 2 | 00:05.73 | 00:08.33 | 2.60 | what you'll be doing 24 hours later. | slow_drift | ease_out (fast start, decelerating) | 3D | 134 | 150 | [img](KEYFRAMES/V1/V1_shot002_0005.73s.jpg) |
| 3 | 00:08.33 | 00:10.50 | 2.17 | And people use this to their advantage. | static | n/a |  | 170 | 62 | [img](KEYFRAMES/V1/V1_shot003_0008.33s.jpg) |
| 4 | 00:10.50 | 00:12.33 | 1.83 | My neighbor once saw his shadow holding | slow_drift | ease_in_out | 3D | 192 | 47 | [img](KEYFRAMES/V1/V1_shot004_0010.50s.jpg) |
| 5 | 00:12.33 | 00:13.93 | 1.60 | a giant check. | slow_drift | ease_in (accelerating) | 3D | 175 | 65 | [img](KEYFRAMES/V1/V1_shot005_0012.33s.jpg) |
| 6 | 00:13.93 | 00:16.03 | 2.10 | He immediately bought a lottery ticket. The | slow_drift | ease_in_out | 3D | 62 | 198 | [img](KEYFRAMES/V1/V1_shot006_0013.93s.jpg) |
| 7 | 00:16.03 | 00:18.70 | 2.67 | next day, he became a millionaire. At | slow_drift | ease_in_out | 3D | 173 | 84 | [img](KEYFRAMES/V1/V1_shot007_0016.03s.jpg) |
| 8 | 00:18.70 | 00:23.13 | 4.43 | school, my best friend saw his shadow crying over a failed math test. He | slow_drift | ease_in_out | 3D | 189 | 47 | [img](KEYFRAMES/V1/V1_shot008_0018.70s.jpg) |
| 9 | 00:23.13 | 00:28.27 | 5.13 | studied all night, and eventually, his shadow changed. That's the best part. The | slow_drift | ease_in (accelerating) | 3D | 192 | 62 | [img](KEYFRAMES/V1/V1_shot009_0023.13s.jpg) |
| 10 | 00:28.27 | 00:31.43 | 3.17 | future isn't permanent. You can change it. | slow_drift | ease_in_out | 3D | 156 | 78 | [img](KEYFRAMES/V1/V1_shot010_0028.27s.jpg) |
| 11 | 00:31.43 | 00:34.03 | 2.60 | But one morning, something strange happened. | slow_drift | ease_in (accelerating) | 3D | 122 | 90 | [img](KEYFRAMES/V1/V1_shot011_0031.43s.jpg) |
| 12 | 00:34.03 | 00:39.63 | 5.60 | While walking to school, I noticed a woman standing in direct sunlight without a shadow. | slow_drift | ease_in_out | 3D | 184 | 64 | [img](KEYFRAMES/V1/V1_shot012_0034.03s.jpg) |
| 13 | 00:39.63 | 00:41.77 | 2.13 | Then, a businessman lost his shadow. | slow_drift | ease_out (fast start, decelerating) | 3D | 190 | 43 | [img](KEYFRAMES/V1/V1_shot013_0039.63s.jpg) |
| 14 | 00:41.77 | 00:43.83 | 2.07 | Then, a police officer. | static | n/a |  | 189 | 44 | [img](KEYFRAMES/V1/V1_shot014_0041.77s.jpg) |
| 15 | 00:43.83 | 00:47.33 | 3.50 | Within hours, almost everyone in town had lost theirs. | slow_drift | ease_in (accelerating) | 3D | 117 | 115 | [img](KEYFRAMES/V1/V1_shot015_0043.83s.jpg) |
| 16 | 00:47.33 | 00:48.87 | 1.53 | Nobody understood why. | pan_or_track_left | linear/constant |  | 82 | 146 | [img](KEYFRAMES/V1/V1_shot016_0047.33s.jpg) |
| 17 | 00:48.87 | 00:52.23 | 3.37 | Even the scientists had never seen anything like this before. But | static | n/a |  | 128 | 114 | [img](KEYFRAMES/V1/V1_shot017_0048.87s.jpg) |
| 18 | 00:52.23 | 00:56.63 | 4.40 | my shadow was still there. It showed me standing on a mountain outside the town, | slow_drift | ease_in (accelerating) | 3D | 173 | 68 | [img](KEYFRAMES/V1/V1_shot018_0052.23s.jpg) |
| 19 | 00:56.63 | 00:59.23 | 2.60 | looking down at something in horror. I | static | n/a |  | 140 | 121 | [img](KEYFRAMES/V1/V1_shot019_0056.63s.jpg) |
| 20 | 00:59.23 | 01:01.63 | 2.40 | was supposed to go hiking there tomorrow, but instead, | slow_drift | ease_out (fast start, decelerating) | 3D | 129 | 170 | [img](KEYFRAMES/V1/V1_shot020_0059.23s.jpg) |
| 21 | 01:01.63 | 01:04.13 | 2.50 | I decided to go today. | static | n/a |  | 126 | 168 | [img](KEYFRAMES/V1/V1_shot021_0061.63s.jpg) |
| 22 | 01:04.13 | 01:06.33 | 2.20 | When I reached the mountain, I noticed enormous cracks | push_in | ease_in (accelerating) | 3D | 112 | 136 | [img](KEYFRAMES/V1/V1_shot022_0064.13s.jpg) |
| 23 | 01:06.33 | 01:08.70 | 2.37 | in the ground surrounding our town. I | static | n/a |  | 105 | 134 | [img](KEYFRAMES/V1/V1_shot023_0066.33s.jpg) |
| 24 | 01:08.70 | 01:11.30 | 2.60 | followed one of them into an underground cave, | static | n/a |  | 129 | 148 | [img](KEYFRAMES/V1/V1_shot024_0068.70s.jpg) |
| 25 | 01:11.30 | 01:17.63 | 6.33 | and what I discovered terrified me. There was a gigantic empty space directly beneath o… | slow_drift | ease_in_out | 3D | 188 | 78 | [img](KEYFRAMES/V1/V1_shot025_0071.30s.jpg) |
| 26 | 01:17.63 | 01:19.83 | 2.20 | The entire city was sitting on a thin layer of | static | n/a |  | 110 | 190 | [img](KEYFRAMES/V1/V1_shot026_0077.63s.jpg) |
| 27 | 01:19.83 | 01:22.37 | 2.53 | rock that was slowly breaking apart. | static | n/a |  | 99 | 174 | [img](KEYFRAMES/V1/V1_shot027_0079.83s.jpg) |
| 28 | 01:22.37 | 01:24.53 | 2.17 | Suddenly, everything made sense. | static | n/a |  | 69 | 143 | [img](KEYFRAMES/V1/V1_shot028_0082.37s.jpg) |
| 29 | 01:24.53 | 01:27.43 | 2.90 | Tomorrow, the entire town would collapse, and | slow_drift | ease_in (accelerating) | 3D | 120 | 181 | [img](KEYFRAMES/V1/V1_shot029_0084.53s.jpg) |
| 30 | 01:27.43 | 01:30.70 | 3.27 | everyone without a shadow wouldn't survive. | slow_drift | ease_in_out | 3D | 90 | 148 | [img](KEYFRAMES/V1/V1_shot030_0087.43s.jpg) |
| 31 | 01:30.70 | 01:32.03 | 1.33 | I rushed back and showed the mayor | static | n/a |  | 113 | 84 | [img](KEYFRAMES/V1/V1_shot031_0090.70s.jpg) |
| 32 | 01:32.03 | 01:36.03 | 4.00 | pictures of the underground cavern. He immediately ordered an evacuation. | slow_drift | ease_in_out | 3D | 143 | 88 | [img](KEYFRAMES/V1/V1_shot032_0092.03s.jpg) |
| 33 | 01:36.03 | 01:37.77 | 1.73 | Families packed their belongings. | push_in | ease_in_out | 3D | 136 | 108 | [img](KEYFRAMES/V1/V1_shot033_0096.03s.jpg) |
| 34 | 01:37.77 | 01:40.33 | 2.57 | Buses transported children and elderly people. | push_in | ease_in (accelerating) | 3D | 107 | 108 | [img](KEYFRAMES/V1/V1_shot034_0097.77s.jpg) |
| 35 | 01:40.33 | 01:42.83 | 2.50 | Thousands of residents abandoned their homes, and | static | n/a |  | 113 | 125 | [img](KEYFRAMES/V1/V1_shot035_0100.33s.jpg) |
| 36 | 01:42.83 | 01:46.27 | 3.43 | as they reached safety, their shadows started coming back. By | static | n/a |  | 116 | 199 | [img](KEYFRAMES/V1/V1_shot036_0102.83s.jpg) |
| 37 | 01:46.27 | 01:48.77 | 2.50 | sunset, everyone had escaped. The | static | n/a |  | 134 | 177 | [img](KEYFRAMES/V1/V1_shot037_0106.27s.jpg) |
| 38 | 01:48.77 | 01:53.93 | 5.17 | following morning, we watched from the mountain as our entire town disappeared into the… | push_in | ease_out (fast start, decelerating) | 3D | 126 | 120 | [img](KEYFRAMES/V1/V1_shot038_0108.77s.jpg) |
| 39 | 01:53.93 | 01:55.23 | 1.30 | had lost our homes, | static | n/a |  | 107 | 190 | [img](KEYFRAMES/V1/V1_shot039_0113.93s.jpg) |
| 40 | 01:55.23 | 01:56.23 | 1.00 | our schools, and | slow_drift | ease_in (accelerating) | 3D | 123 | 168 | [img](KEYFRAMES/V1/V1_shot040_0115.23s.jpg) |
| 41 | 01:56.23 | 01:57.87 | 1.63 | everything we had built, but | slow_drift | ease_in (accelerating) | 3D | 83 | 155 | [img](KEYFRAMES/V1/V1_shot041_0116.23s.jpg) |
| 42 | 01:57.87 | 01:59.63 | 1.77 | we still had each other. | static | n/a |  | 140 | 112 | [img](KEYFRAMES/V1/V1_shot042_0117.87s.jpg) |
| 43 | 01:59.63 | 02:04.50 | 4.87 | Over the following months, everyone worked together to build a new town on solid ground. | static | n/a |  | 147 | 148 | [img](KEYFRAMES/V1/V1_shot043_0119.63s.jpg) |
| 44 | 02:04.50 | 02:06.23 | 1.73 | New houses, new shops, | push_in | ease_in_out | 3D | 112 | 90 | [img](KEYFRAMES/V1/V1_shot044_0124.50s.jpg) |
| 45 | 02:06.23 | 02:08.00 | 1.77 | and even a bigger school. | slow_drift | ease_out (fast start, decelerating) | 3D | 164 | 67 | [img](KEYFRAMES/V1/V1_shot045_0126.23s.jpg) |
| 46 | 02:08.00 | 02:19.00 | 11.00 | One morning, I looked down at my shadow. It was surrounded by people, celebrating the o… | slow_drift | ease_in (accelerating) | 3D | 161 | 90 | [img](KEYFRAMES/V1/V1_shot046_0128.00s.jpg) |
| 47 | 02:19.00 | 02:23.00 | 4.00 | *(TikTok end card)* | slow_drift | linear/constant |  | 21 | 116 | [img](KEYFRAMES/V1/V1_shot047_0139.00s.jpg) |

### V2 — `5bbdae42-v15044gf0000dc25vm7og65linhp7ks0.mp4` — 2246 frames, 43 shots

| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 00:00.00 | 00:02.87 | 2.87 | In this town, every kid looks exactly like their dad. | push_in | ease_out (fast start, decelerating) | 3D | 124 | 86 | [img](KEYFRAMES/V2/V2_shot000_0000.00s.jpg) |
| 1 | 00:02.87 | 00:04.93 | 2.07 | Hush, hush, hush, hush, hush, hush. Same | push_in | ease_in (accelerating) | 3D | 118 | 82 | [img](KEYFRAMES/V2/V2_shot001_0002.87s.jpg) |
| 2 | 00:04.93 | 00:05.83 | 0.90 | nose, | push_in | ease_in (accelerating) | 3D | 113 | 80 | [img](KEYFRAMES/V2/V2_shot002_0004.93s.jpg) |
| 3 | 00:05.83 | 00:06.73 | 0.90 | same hair, same | push_in | ease_in_out | 3D | 121 | 79 | [img](KEYFRAMES/V2/V2_shot003_0005.83s.jpg) |
| 4 | 00:06.73 | 00:07.73 | 1.00 | weird laugh. | push_in | ease_in_out | 3D | 122 | 74 | [img](KEYFRAMES/V2/V2_shot004_0006.73s.jpg) |
| 5 | 00:07.73 | 00:08.63 | 0.90 | Except me. | push_in | ease_in_out | 3D | 101 | 96 | [img](KEYFRAMES/V2/V2_shot005_0007.73s.jpg) |
| 6 | 00:08.63 | 00:09.53 | 0.90 | My dad is tall, | tilt_or_crane_up | ease_out (fast start, decelerating) |  | 99 | 98 | [img](KEYFRAMES/V2/V2_shot006_0008.63s.jpg) |
| 7 | 00:09.53 | 00:11.57 | 2.03 | bald, and has a huge black beard. | pull_out | ease_in (accelerating) | 3D | 91 | 91 | [img](KEYFRAMES/V2/V2_shot007_0009.53s.jpg) |
| 8 | 00:11.57 | 00:14.10 | 2.53 | I have curly red hair and a tiny mustache. | push_in | ease_in (accelerating) | 3D | 115 | 105 | [img](KEYFRAMES/V2/V2_shot008_0011.57s.jpg) |
| 9 | 00:14.10 | 00:16.80 | 2.70 | You know who else has curly red hair and a tiny mustache? | push_in | ease_in (accelerating) | 3D | 141 | 81 | [img](KEYFRAMES/V2/V2_shot009_0014.10s.jpg) |
| 10 | 00:16.80 | 00:17.70 | 0.90 | Our mailman, | push_in | ease_in_out | 3D | 133 | 79 | [img](KEYFRAMES/V2/V2_shot010_0016.80s.jpg) |
| 11 | 00:17.70 | 00:18.97 | 1.27 | he comes three times a day. | push_in | ease_out (fast start, decelerating) | 3D | 128 | 83 | [img](KEYFRAMES/V2/V2_shot011_0017.70s.jpg) |
| 12 | 00:18.97 | 00:20.17 | 1.20 | Even on Sundays, | push_in | ease_in_out | 3D | 106 | 85 | [img](KEYFRAMES/V2/V2_shot012_0018.97s.jpg) |
| 13 | 00:20.17 | 00:21.33 | 1.17 | even when there's no mail, | tilt_or_crane_up | ease_in (accelerating) |  | 98 | 82 | [img](KEYFRAMES/V2/V2_shot013_0020.17s.jpg) |
| 14 | 00:21.33 | 00:24.33 | 3.00 | he never forgets my birthday. Last year, he gave me a bike. | subject_motion_or_orbit | ease_in (accelerating) |  | 110 | 95 | [img](KEYFRAMES/V2/V2_shot014_0021.33s.jpg) |
| 15 | 00:24.33 | 00:25.67 | 1.33 | Dad gave me socks. | push_in | linear/constant | 3D | 106 | 93 | [img](KEYFRAMES/V2/V2_shot015_0024.33s.jpg) |
| 16 | 00:25.67 | 00:27.60 | 1.93 | When I had the flu, he brought me soup through | push_in | ease_in_out | 3D | 174 | 102 | [img](KEYFRAMES/V2/V2_shot016_0025.67s.jpg) |
| 17 | 00:27.60 | 00:29.07 | 1.47 | my bedroom window. And | push_in | ease_in_out | 3D | 194 | 73 | [img](KEYFRAMES/V2/V2_shot017_0027.60s.jpg) |
| 18 | 00:29.07 | 00:30.77 | 1.70 | every time dad leaves for work, | push_in | ease_in (accelerating) | 3D | 102 | 93 | [img](KEYFRAMES/V2/V2_shot018_0029.07s.jpg) |
| 19 | 00:30.77 | 00:32.60 | 1.83 | the mailman shows up two minutes later. | pan_or_track_right | ease_in_out |  | 127 | 92 | [img](KEYFRAMES/V2/V2_shot019_0030.77s.jpg) |
| 20 | 00:32.60 | 00:34.60 | 2.00 | Mom says he just really loves his job. | push_in | ease_in_out | 3D | 209 | 54 | [img](KEYFRAMES/V2/V2_shot020_0032.60s.jpg) |
| 21 | 00:34.60 | 00:36.70 | 2.10 | Then, I started noticing something weird. | push_in | ease_out (fast start, decelerating) | 3D | 110 | 96 | [img](KEYFRAMES/V2/V2_shot021_0034.60s.jpg) |
| 22 | 00:36.70 | 00:39.03 | 2.33 | The twins next door have curly red hair, too. | subject_motion_or_orbit | ease_in_out |  | 129 | 85 | [img](KEYFRAMES/V2/V2_shot022_0036.70s.jpg) |
| 23 | 00:39.03 | 00:40.37 | 1.33 | So does the kid across the street. | pull_out | ease_in_out | 3D | 136 | 84 | [img](KEYFRAMES/V2/V2_shot023_0039.03s.jpg) |
| 24 | 00:40.37 | 00:42.97 | 2.60 | And the baby on the corner already has a mustache. | push_in | ease_in (accelerating) | 3D | 166 | 68 | [img](KEYFRAMES/V2/V2_shot024_0040.37s.jpg) |
| 25 | 00:42.97 | 00:45.43 | 2.47 | So yesterday, I decided to find out the truth. | push_in | ease_in (accelerating) | 3D | 127 | 90 | [img](KEYFRAMES/V2/V2_shot025_0042.97s.jpg) |
| 26 | 00:45.43 | 00:47.40 | 1.97 | I hid in the bushes with my binoculars. | slow_drift | ease_out (fast start, decelerating) | 3D | 102 | 101 | [img](KEYFRAMES/V2/V2_shot026_0045.43s.jpg) |
| 27 | 00:47.40 | 00:48.30 | 0.90 | Dad's car left. | subject_motion_or_orbit | linear/constant |  | 35 | 49 | [img](KEYFRAMES/V2/V2_shot027_0047.40s.jpg) |
| 28 | 00:48.30 | 00:50.93 | 2.63 | Two minutes later, the mail truck parked in front of our house. | slow_drift | ease_in_out | 3D | 123 | 97 | [img](KEYFRAMES/V2/V2_shot028_0048.30s.jpg) |
| 29 | 00:50.93 | 00:52.33 | 1.40 | The mailman rang the bell. | push_in | ease_in_out | 3D | 120 | 95 | [img](KEYFRAMES/V2/V2_shot029_0050.93s.jpg) |
| 30 | 00:52.33 | 00:53.23 | 0.90 | Mom opened the door in | push_in | ease_in_out | 3D | 149 | 74 | [img](KEYFRAMES/V2/V2_shot030_0052.33s.jpg) |
| 31 | 00:53.23 | 00:54.63 | 1.40 | her nicest dress. | static | n/a |  | 34 | 37 | [img](KEYFRAMES/V2/V2_shot031_0053.23s.jpg) |
| 32 | 00:54.63 | 00:56.63 | 2.00 | He went inside with no letters. | slow_drift | ease_out (fast start, decelerating) | 3D | 115 | 72 | [img](KEYFRAMES/V2/V2_shot032_0054.63s.jpg) |
| 33 | 00:56.63 | 00:57.97 | 1.33 | Then, the curtains closed. And | push_in | ease_out (fast start, decelerating) |  | 131 | 75 | [img](KEYFRAMES/V2/V2_shot033_0056.63s.jpg) |
| 34 | 00:57.97 | 01:00.00 | 2.03 | from inside, I heard them both going... | push_in | ease_in_out | 3D | 87 | 108 | [img](KEYFRAMES/V2/V2_shot034_0057.97s.jpg) |
| 35 | 01:00.00 | 01:01.73 | 1.73 |  | push_in | ease_out (fast start, decelerating) | 3D | 121 | 85 | [img](KEYFRAMES/V2/V2_shot035_0060.00s.jpg) |
| 36 | 01:01.73 | 01:03.50 | 1.77 |  | subject_motion_or_orbit | linear/constant |  | 120 | 86 | [img](KEYFRAMES/V2/V2_shot036_0061.73s.jpg) |
| 37 | 01:03.50 | 01:04.87 | 1.37 | Over and over, | static | n/a |  | 84 | 106 | [img](KEYFRAMES/V2/V2_shot037_0063.50s.jpg) |
| 38 | 01:04.87 | 01:06.27 | 1.40 | Mom must be helping him train. | slow_drift | ease_in (accelerating) | 3D | 90 | 105 | [img](KEYFRAMES/V2/V2_shot038_0064.87s.jpg) |
| 39 | 01:06.27 | 01:07.33 | 1.07 | I ran to the window, | pan_or_track_left | ease_out (fast start, decelerating) |  | 111 | 92 | [img](KEYFRAMES/V2/V2_shot039_0066.27s.jpg) |
| 40 | 01:07.33 | 01:08.53 | 1.20 | climbed on the trash can, | push_in | ease_in_out | 3D | 111 | 93 | [img](KEYFRAMES/V2/V2_shot040_0067.33s.jpg) |
| 41 | 01:08.53 | 01:10.87 | 2.33 | pressed my face against the glass, and... | push_in | ease_out (fast start, decelerating) | 3D | 174 | 138 | [img](KEYFRAMES/V2/V2_shot041_0068.53s.jpg) |
| 42 | 01:10.87 | 01:14.87 | 4.00 | *(TikTok end card)* | slow_drift | linear/constant |  | 21 | 116 | [img](KEYFRAMES/V2/V2_shot042_0070.87s.jpg) |

### V3 — `6fbc8ec7-v26044gc0000dc1l1b7og65us58g66u0.mp4` — 4163 frames, 84 shots

| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 00:00.00 | 00:02.63 | 2.63 | In this town, everyone has a guardian angel. | static | n/a |  | 103 | 119 | [img](KEYFRAMES/V3/V3_shot000_0000.00s.jpg) |
| 1 | 00:02.63 | 00:03.60 | 0.97 | You can't see them. | slow_drift | ease_in_out | 3D | 93 | 132 | [img](KEYFRAMES/V3/V3_shot001_0002.63s.jpg) |
| 2 | 00:03.60 | 00:04.80 | 1.20 | You can't hear them. But | push_in | ease_in_out | 3D | 98 | 101 | [img](KEYFRAMES/V3/V3_shot002_0003.60s.jpg) |
| 3 | 00:04.80 | 00:06.07 | 1.27 | the second you're about to die, | slow_drift | ease_in_out | 3D | 93 | 135 | [img](KEYFRAMES/V3/V3_shot003_0004.80s.jpg) |
| 4 | 00:06.07 | 00:06.97 | 0.90 | they save | slow_drift | ease_in (accelerating) |  | 194 | 50 | [img](KEYFRAMES/V3/V3_shot004_0006.07s.jpg) |
| 5 | 00:06.97 | 00:07.60 | 0.63 | you. | static | n/a |  | 59 | 182 | [img](KEYFRAMES/V3/V3_shot005_0006.97s.jpg) |
| 6 | 00:07.60 | 00:08.77 | 1.17 | Last week, a construction worker | slow_drift | ease_in_out | 3D | 111 | 168 | [img](KEYFRAMES/V3/V3_shot006_0007.60s.jpg) |
| 7 | 00:08.77 | 00:09.90 | 1.13 | fell off a skyscraper. | pull_out | ease_in_out |  | 101 | 198 | [img](KEYFRAMES/V3/V3_shot007_0008.77s.jpg) |
| 8 | 00:09.90 | 00:10.10 | 0.20 |  | too_short |  |  | 71 | 192 | [img](KEYFRAMES/V3/V3_shot008_0009.90s.jpg) |
| 9 | 00:10.10 | 00:11.17 | 1.07 | A golden light flashed | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 230 | 27 | [img](KEYFRAMES/V3/V3_shot009_0010.10s.jpg) |
| 10 | 00:11.17 | 00:12.27 | 1.10 | and he landed on his feet. | push_in | ease_in_out |  | 99 | 147 | [img](KEYFRAMES/V3/V3_shot010_0011.17s.jpg) |
| 11 | 00:12.27 | 00:13.43 | 1.17 | A school bus lost | pull_out | ease_in_out |  | 106 | 173 | [img](KEYFRAMES/V3/V3_shot011_0012.27s.jpg) |
| 12 | 00:13.43 | 00:14.40 | 0.97 | its brakes on Hill Road. | slow_drift | ease_in (accelerating) |  | 100 | 155 | [img](KEYFRAMES/V3/V3_shot012_0013.43s.jpg) |
| 13 | 00:14.40 | 00:15.63 | 1.23 | It stopped one inch | push_in | ease_in (accelerating) | 3D | 61 | 160 | [img](KEYFRAMES/V3/V3_shot013_0014.40s.jpg) |
| 14 | 00:15.63 | 00:16.60 | 0.97 | from the wall. | push_in | ease_out (fast start, decelerating) | 3D | 100 | 187 | [img](KEYFRAMES/V3/V3_shot014_0015.63s.jpg) |
| 15 | 00:16.60 | 00:19.30 | 2.70 | And afterwards, there's always a golden feather. | slow_drift | ease_in_out | 3D | 105 | 188 | [img](KEYFRAMES/V3/V3_shot015_0016.60s.jpg) |
| 16 | 00:19.30 | 00:20.10 | 0.80 | I'm 12. | push_in | ease_in_out | 3D | 110 | 148 | [img](KEYFRAMES/V3/V3_shot016_0019.30s.jpg) |
| 17 | 00:20.10 | 00:21.70 | 1.60 | My little sister Lily is seven. | subject_motion_or_orbit | ease_in_out |  | 109 | 132 | [img](KEYFRAMES/V3/V3_shot017_0020.10s.jpg) |
| 18 | 00:21.70 | 00:24.43 | 2.73 | She has 11 golden feathers in a jar next to her bed. | static | n/a |  | 103 | 147 | [img](KEYFRAMES/V3/V3_shot018_0021.70s.jpg) |
| 19 | 00:24.43 | 00:25.30 | 0.87 | 11. | push_in | ease_in_out | 3D | 201 | 83 | [img](KEYFRAMES/V3/V3_shot019_0024.43s.jpg) |
| 20 | 00:25.30 | 00:27.27 | 1.97 | Most people find one in their whole life. | slow_drift | ease_out (fast start, decelerating) | 3D | 86 | 121 | [img](KEYFRAMES/V3/V3_shot020_0025.30s.jpg) |
| 21 | 00:27.27 | 00:28.33 | 1.07 | She climbs everything. She | push_in | ease_in_out | 3D | 118 | 148 | [img](KEYFRAMES/V3/V3_shot021_0027.27s.jpg) |
| 22 | 00:28.33 | 00:30.27 | 1.93 | runs into the street without looking. | slow_drift | ease_out (fast start, decelerating) | 3D | 103 | 154 | [img](KEYFRAMES/V3/V3_shot022_0028.33s.jpg) |
| 23 | 00:30.27 | 00:31.87 | 1.60 | Everybody wonders who her angel is. | slow_drift | ease_in (accelerating) | 3D | 109 | 136 | [img](KEYFRAMES/V3/V3_shot023_0030.27s.jpg) |
| 24 | 00:31.87 | 00:32.90 | 1.03 | I bet it's Grandpa. | push_in | ease_in_out |  | 107 | 145 | [img](KEYFRAMES/V3/V3_shot024_0031.87s.jpg) |
| 25 | 00:32.90 | 00:34.43 | 1.53 | She was always his favorite. | push_in | ease_in_out | 3D | 107 | 138 | [img](KEYFRAMES/V3/V3_shot025_0032.90s.jpg) |
| 26 | 00:34.43 | 00:36.20 | 1.77 | Every morning, I walk Lily to school. | pull_out | ease_in_out | 3D | 114 | 127 | [img](KEYFRAMES/V3/V3_shot026_0034.43s.jpg) |
| 27 | 00:36.20 | 00:39.37 | 3.17 | She talks the whole way. She never lets me get a single word in. | pan_or_track_right | ease_out (fast start, decelerating) |  | 110 | 128 | [img](KEYFRAMES/V3/V3_shot027_0036.20s.jpg) |
| 28 | 00:39.37 | 00:40.53 | 1.17 | We always stop at the corner store | slow_drift | ease_out (fast start, decelerating) | 3D | 111 | 130 | [img](KEYFRAMES/V3/V3_shot028_0039.37s.jpg) |
| 29 | 00:40.53 | 00:41.07 | 0.53 | and she takes | slow_drift | ease_out (fast start, decelerating) |  | 116 | 136 | [img](KEYFRAMES/V3/V3_shot029_0040.53s.jpg) |
| 30 | 00:41.07 | 00:45.33 | 4.27 | a selfie of us in front of the candy shelf. She never shows me. She says, I blinked again. | push_in | ease_in (accelerating) | 3D | 119 | 137 | [img](KEYFRAMES/V3/V3_shot030_0041.07s.jpg) |
| 31 | 00:45.33 | 00:46.63 | 1.30 | Biscuit always comes too. | push_in | ease_in (accelerating) | 3D | 104 | 171 | [img](KEYFRAMES/V3/V3_shot031_0045.33s.jpg) |
| 32 | 00:46.63 | 00:48.07 | 1.43 | He follows me everywhere. | pan_or_track_right | ease_in_out |  | 110 | 160 | [img](KEYFRAMES/V3/V3_shot032_0046.63s.jpg) |
| 33 | 00:48.07 | 00:49.53 | 1.47 | One night, Mom made pizza. | push_in | ease_in_out | 3D | 96 | 162 | [img](KEYFRAMES/V3/V3_shot033_0048.07s.jpg) |
| 34 | 00:49.53 | 00:51.77 | 2.23 | Mom, can we have pizza again tomorrow? I asked. | slow_drift | linear/constant | 3D | 108 | 175 | [img](KEYFRAMES/V3/V3_shot034_0049.53s.jpg) |
| 35 | 00:51.77 | 00:55.20 | 3.43 | And Lily said the exact same thing at the exact same time. | static | n/a |  | 112 | 150 | [img](KEYFRAMES/V3/V3_shot035_0051.77s.jpg) |
| 36 | 00:55.20 | 00:56.13 | 0.93 | Jinx, I said. | push_in | ease_in_out | 3D | 109 | 146 | [img](KEYFRAMES/V3/V3_shot036_0055.20s.jpg) |
| 37 | 00:56.13 | 00:57.27 | 1.13 | Mom laughed. Sure, | subject_motion_or_orbit | ease_in_out |  | 102 | 149 | [img](KEYFRAMES/V3/V3_shot037_0056.13s.jpg) |
| 38 | 00:57.27 | 00:57.97 | 0.70 | sweetheart. | slow_drift | ease_in_out |  | 103 | 176 | [img](KEYFRAMES/V3/V3_shot038_0057.27s.jpg) |
| 39 | 00:57.97 | 01:00.93 | 2.97 | On Saturday, Lily wanted to go to the old train station. | slow_drift | ease_in_out | 3D | 109 | 105 | [img](KEYFRAMES/V3/V3_shot039_0057.97s.jpg) |
| 40 | 01:00.93 | 01:01.57 | 0.63 | She goes there a lot. | push_in | ease_in (accelerating) |  | 86 | 100 | [img](KEYFRAMES/V3/V3_shot040_0060.93s.jpg) |
| 41 | 01:01.57 | 01:03.17 | 1.60 | She says she likes watching the trains. | pull_out | ease_out (fast start, decelerating) | 3D | 70 | 163 | [img](KEYFRAMES/V3/V3_shot041_0061.57s.jpg) |
| 42 | 01:03.17 | 01:05.03 | 1.87 | At the railway crossing, she stopped. | static | n/a |  | 103 | 101 | [img](KEYFRAMES/V3/V3_shot042_0063.17s.jpg) |
| 43 | 01:05.03 | 01:07.00 | 1.97 | And suddenly, the gate started closing. | pan_or_track_left | ease_in_out |  | 104 | 85 | [img](KEYFRAMES/V3/V3_shot043_0065.03s.jpg) |
| 44 | 01:07.00 | 01:07.73 | 0.73 | Her backpack got | subject_motion_or_orbit | ease_in (accelerating) |  | 94 | 112 | [img](KEYFRAMES/V3/V3_shot044_0067.00s.jpg) |
| 45 | 01:07.73 | 01:08.53 | 0.80 | caught on the fence | push_in | ease_in_out | 3D | 106 | 109 | [img](KEYFRAMES/V3/V3_shot045_0067.73s.jpg) |
| 46 | 01:08.53 | 01:09.63 | 1.10 | and a train was coming | static | n/a |  | 107 | 67 | [img](KEYFRAMES/V3/V3_shot046_0068.53s.jpg) |
| 47 | 01:09.63 | 01:10.50 | 0.87 | straight at her. | push_in | ease_in_out | 3D | 106 | 115 | [img](KEYFRAMES/V3/V3_shot047_0069.63s.jpg) |
| 48 | 01:10.50 | 01:11.47 | 0.97 | I screamed her | slow_drift | ease_out (fast start, decelerating) | 3D | 96 | 113 | [img](KEYFRAMES/V3/V3_shot048_0070.50s.jpg) |
| 49 | 01:11.47 | 01:12.50 | 1.03 | name and ran. | push_in | ease_in_out | 3D | 99 | 113 | [img](KEYFRAMES/V3/V3_shot049_0071.47s.jpg) |
| 50 | 01:12.50 | 01:15.93 | 3.43 | Then a blinding golden light covered everything. When it faded, | slow_drift | ease_out (fast start, decelerating) |  | 230 | 15 | [img](KEYFRAMES/V3/V3_shot050_0072.50s.jpg) |
| 51 | 01:15.93 | 01:18.00 | 2.07 | Lily was on the sidewalk, safe, | push_in | ease_in_out | 3D | 102 | 118 | [img](KEYFRAMES/V3/V3_shot051_0075.93s.jpg) |
| 52 | 01:18.00 | 01:19.53 | 1.53 | holding a golden feather. | slow_drift | ease_in (accelerating) | 3D | 95 | 146 | [img](KEYFRAMES/V3/V3_shot052_0078.00s.jpg) |
| 53 | 01:19.53 | 01:20.67 | 1.13 | Number 12. | subject_motion_or_orbit | linear/constant |  | 101 | 226 | [img](KEYFRAMES/V3/V3_shot053_0079.53s.jpg) |
| 54 | 01:20.67 | 01:22.03 | 1.37 | But she wasn't looking at me. | subject_motion_or_orbit | ease_in_out |  | 101 | 150 | [img](KEYFRAMES/V3/V3_shot054_0080.67s.jpg) |
| 55 | 01:22.03 | 01:24.37 | 2.33 | She was staring at the empty tracks, crying. | static | n/a |  | 92 | 129 | [img](KEYFRAMES/V3/V3_shot055_0082.03s.jpg) |
| 56 | 01:24.37 | 01:26.33 | 1.97 | And she whispered, I always knew it was you. | static | n/a |  | 97 | 131 | [img](KEYFRAMES/V3/V3_shot056_0084.37s.jpg) |
| 57 | 01:26.33 | 01:28.43 | 2.10 | I just never got to say thank you. | static | n/a |  | 97 | 141 | [img](KEYFRAMES/V3/V3_shot057_0086.33s.jpg) |
| 58 | 01:28.43 | 01:28.97 | 0.53 | To the tracks, | static | n/a |  | 97 | 90 | [img](KEYFRAMES/V3/V3_shot058_0088.43s.jpg) |
| 59 | 01:28.97 | 01:31.20 | 2.23 | I was standing right next to her. | slow_drift | ease_out (fast start, decelerating) | 3D | 98 | 140 | [img](KEYFRAMES/V3/V3_shot059_0088.97s.jpg) |
| 60 | 01:31.20 | 01:32.80 | 1.60 | And then I remembered. | push_in | ease_in_out | 3D | 101 | 110 | [img](KEYFRAMES/V3/V3_shot060_0091.20s.jpg) |
| 61 | 01:32.80 | 01:35.40 | 2.60 | Three years ago, Lily got stuck on these exact tracks. | subject_motion_or_orbit | ease_in_out |  | 98 | 98 | [img](KEYFRAMES/V3/V3_shot061_0092.80s.jpg) |
| 62 | 01:35.40 | 01:37.20 | 1.80 | I ran back and pushed her out of the way. | pan_or_track_left | ease_in_out |  | 91 | 80 | [img](KEYFRAMES/V3/V3_shot062_0095.40s.jpg) |
| 63 | 01:37.20 | 01:38.33 | 1.13 | She made it. | push_in | ease_in_out | 3D | 93 | 92 | [img](KEYFRAMES/V3/V3_shot063_0097.20s.jpg) |
| 64 | 01:38.33 | 01:38.80 | 0.47 | I didn't. | push_in | ease_in (accelerating) |  | 138 | 71 | [img](KEYFRAMES/V3/V3_shot064_0098.33s.jpg) |
| 65 | 01:38.80 | 01:40.37 | 1.57 | She never let me get a word in | pan_or_track_right | ease_in_out |  | 102 | 132 | [img](KEYFRAMES/V3/V3_shot065_0098.80s.jpg) |
| 66 | 01:40.37 | 01:42.20 | 1.83 | because she knew I couldn't answer. | pan_or_track_right | ease_in_out |  | 96 | 151 | [img](KEYFRAMES/V3/V3_shot066_0100.37s.jpg) |
| 67 | 01:42.20 | 01:44.83 | 2.63 | Sure, sweetheart. Mom was never answering me. | slow_drift | ease_in_out | 3D | 97 | 155 | [img](KEYFRAMES/V3/V3_shot067_0102.20s.jpg) |
| 68 | 01:44.83 | 01:47.30 | 2.47 | And all those selfies at the candy shelf, I never blinked. | push_in | ease_in_out | 2D | 99 | 159 | [img](KEYFRAMES/V3/V3_shot068_0104.83s.jpg) |
| 69 | 01:47.30 | 01:49.67 | 2.37 | There was only one kid in every picture. | static | n/a |  | 125 | 136 | [img](KEYFRAMES/V3/V3_shot069_0107.30s.jpg) |
| 70 | 01:49.67 | 01:51.27 | 1.60 | Biscuit wasn't following me around. | pan_or_track_left | ease_in_out |  | 109 | 134 | [img](KEYFRAMES/V3/V3_shot070_0109.67s.jpg) |
| 71 | 01:51.27 | 01:53.73 | 2.47 | He was the only one in our house who could still see me. | slow_drift | ease_in_out | 3D | 88 | 194 | [img](KEYFRAMES/V3/V3_shot071_0111.27s.jpg) |
| 72 | 01:53.73 | 01:55.70 | 1.97 | Lily doesn't go to the station to watch the trains. | slow_drift | ease_out (fast start, decelerating) | 3D | 90 | 118 | [img](KEYFRAMES/V3/V3_shot072_0113.73s.jpg) |
| 73 | 01:55.70 | 01:57.40 | 1.70 | She goes there to visit me. | push_in | ease_in_out | 3D | 92 | 109 | [img](KEYFRAMES/V3/V3_shot073_0115.70s.jpg) |
| 74 | 01:57.40 | 01:58.17 | 0.77 | And every feather | static | n/a |  | 108 | 132 | [img](KEYFRAMES/V3/V3_shot074_0117.40s.jpg) |
| 75 | 01:58.17 | 01:58.73 | 0.57 | in that jar | static | n/a |  | 100 | 145 | [img](KEYFRAMES/V3/V3_shot075_0118.17s.jpg) |
| 76 | 01:58.73 | 02:00.27 | 1.53 | was mine. | push_in | ease_in_out | 3D | 184 | 90 | [img](KEYFRAMES/V3/V3_shot076_0118.73s.jpg) |
| 77 | 02:00.27 | 02:03.37 | 3.10 | I spent three years wondering who my guardian angel was. I | static | n/a |  | 67 | 153 | [img](KEYFRAMES/V3/V3_shot077_0120.27s.jpg) |
| 78 | 02:03.37 | 02:04.63 | 1.27 | never had one. | static | n/a |  | 63 | 219 | [img](KEYFRAMES/V3/V3_shot078_0123.37s.jpg) |
| 79 | 02:04.63 | 02:05.70 | 1.07 | I am one. | push_in | ease_out (fast start, decelerating) | 3D | 97 | 201 | [img](KEYFRAMES/V3/V3_shot079_0124.63s.jpg) |
| 80 | 02:05.70 | 02:10.70 | 5.00 | That night, Lily put the twelfth feather in her jar. And for the first time, she wrote … | slow_drift | ease_in (accelerating) | 3D | 111 | 157 | [img](KEYFRAMES/V3/V3_shot080_0125.70s.jpg) |
| 81 | 02:10.70 | 02:11.97 | 1.27 | My brother. | slow_drift | ease_in (accelerating) | 3D | 195 | 64 | [img](KEYFRAMES/V3/V3_shot081_0130.70s.jpg) |
| 82 | 02:11.97 | 02:14.77 | 2.80 |  | static | n/a |  | 59 | 182 | [img](KEYFRAMES/V3/V3_shot082_0131.97s.jpg) |
| 83 | 02:14.77 | 02:18.77 | 4.00 | *(TikTok end card)* | slow_drift | linear/constant |  | 21 | 116 | [img](KEYFRAMES/V3/V3_shot083_0134.77s.jpg) |

### V4 — `ffad1ac0-v15044gf0000dc3d877og65umu2pe8vg.mp4` — 3915 frames, 93 shots

| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 00:00.00 | 00:02.13 | 2.13 | In this town, whoever wakes up first each day | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 145 | 111 | [img](KEYFRAMES/V4/V4_shot000_0000.00s.jpg) |
| 1 | 00:02.13 | 00:03.87 | 1.73 | gets to pick that day's weather. | pull_out | ease_out (fast start, decelerating) | 3D | 186 | 80 | [img](KEYFRAMES/V4/V4_shot001_0002.13s.jpg) |
| 2 | 00:03.87 | 00:05.40 | 1.53 | You see, the second your eyes open, | push_in | ease_out (fast start, decelerating) | 3D | 144 | 93 | [img](KEYFRAMES/V4/V4_shot002_0003.87s.jpg) |
| 3 | 00:05.40 | 00:06.50 | 1.10 | you just say it out loud and | push_in | ease_out (fast start, decelerating) | 3D | 135 | 112 | [img](KEYFRAMES/V4/V4_shot003_0005.40s.jpg) |
| 4 | 00:06.50 | 00:07.67 | 1.17 | the sky does it. | tilt_or_crane_up | ease_in (accelerating) |  | 102 | 146 | [img](KEYFRAMES/V4/V4_shot004_0006.50s.jpg) |
| 5 | 00:07.67 | 00:09.40 | 1.73 | So, Grandma goes to bed at 6 o 'clock, | push_in | linear/constant | 3D | 148 | 97 | [img](KEYFRAMES/V4/V4_shot005_0007.67s.jpg) |
| 6 | 00:09.40 | 00:10.57 | 1.17 | wakes up at 3 o 'clock, | push_in | linear/constant | 3D | 105 | 135 | [img](KEYFRAMES/V4/V4_shot006_0009.40s.jpg) |
| 7 | 00:10.57 | 00:12.53 | 1.97 | and says, Sunny and 75. | slow_drift | linear/constant | 3D | 75 | 171 | [img](KEYFRAMES/V4/V4_shot007_0010.57s.jpg) |
| 8 | 00:12.53 | 00:13.97 | 1.43 | She wins almost every day, | push_in | ease_in_out | 3D | 143 | 96 | [img](KEYFRAMES/V4/V4_shot008_0012.53s.jpg) |
| 9 | 00:13.97 | 00:16.33 | 2.37 | and her tomatoes are the size of basketballs. | static | n/a |  | 114 | 191 | [img](KEYFRAMES/V4/V4_shot009_0013.97s.jpg) |
| 10 | 00:16.33 | 00:17.40 | 1.07 | The night before a test, | push_in | ease_in (accelerating) | 3D | 94 | 135 | [img](KEYFRAMES/V4/V4_shot010_0016.33s.jpg) |
| 11 | 00:17.40 | 00:22.17 | 4.77 | every kid in town sets 14 alarms and prays for a snow day. Stay up all night doesn't co… | push_in | linear/constant | 3D | 77 | 169 | [img](KEYFRAMES/V4/V4_shot011_0017.40s.jpg) |
| 12 | 00:22.17 | 00:23.70 | 1.53 | because you have to actually wake up. | slow_drift | ease_in (accelerating) | 3D | 90 | 158 | [img](KEYFRAMES/V4/V4_shot012_0022.17s.jpg) |
| 13 | 00:23.70 | 00:24.90 | 1.20 | And Mr. Ortiz's rooster | push_in | ease_in_out | 3D | 118 | 103 | [img](KEYFRAMES/V4/V4_shot013_0023.70s.jpg) |
| 14 | 00:24.90 | 00:27.13 | 2.23 | hasn't won once in nine years. | slow_drift | ease_out (fast start, decelerating) | 3D | 137 | 138 | [img](KEYFRAMES/V4/V4_shot014_0024.90s.jpg) |
| 15 | 00:27.13 | 00:28.87 | 1.73 | Me? I'm the deepest sleeper in town. | slow_drift | ease_in (accelerating) | 3D | 80 | 166 | [img](KEYFRAMES/V4/V4_shot015_0027.13s.jpg) |
| 16 | 00:28.87 | 00:30.60 | 1.73 | I've never picked the weather once, | slow_drift | linear/constant | ≈static | 130 | 110 | [img](KEYFRAMES/V4/V4_shot016_0028.87s.jpg) |
| 17 | 00:30.60 | 00:30.97 | 0.37 | not even | push_in | n/a |  | 116 | 131 | [img](KEYFRAMES/V4/V4_shot017_0030.60s.jpg) |
| 18 | 00:30.97 | 00:31.70 | 0.73 | on my birthday. | push_in | linear/constant |  | 107 | 117 | [img](KEYFRAMES/V4/V4_shot018_0030.97s.jpg) |
| 19 | 00:31.70 | 00:33.83 | 2.13 | I can fall asleep anywhere in one second. | push_in | linear/constant | ≈static | 112 | 151 | [img](KEYFRAMES/V4/V4_shot019_0031.70s.jpg) |
| 20 | 00:33.83 | 00:34.50 | 0.67 | In the car, | pan_or_track_right | linear/constant |  | 118 | 104 | [img](KEYFRAMES/V4/V4_shot020_0033.83s.jpg) |
| 21 | 00:34.50 | 00:35.27 | 0.77 | at the dentist, | push_in | linear/constant |  | 150 | 86 | [img](KEYFRAMES/V4/V4_shot021_0034.50s.jpg) |
| 22 | 00:35.27 | 00:36.93 | 1.67 | and once standing up in the lunch line. | slow_drift | linear/constant | 3D | 127 | 110 | [img](KEYFRAMES/V4/V4_shot022_0035.27s.jpg) |
| 23 | 00:36.93 | 00:38.40 | 1.47 | Alarms don't work on me. | push_in | ease_in (accelerating) | 3D | 137 | 118 | [img](KEYFRAMES/V4/V4_shot023_0036.93s.jpg) |
| 24 | 00:38.40 | 00:39.97 | 1.57 | Mom says I could sleep through a hurricane. | push_in | ease_in_out | 3D | 104 | 156 | [img](KEYFRAMES/V4/V4_shot024_0038.40s.jpg) |
| 25 | 00:39.97 | 00:41.87 | 1.90 | The only thing that wakes me up is my little sister, | push_in | ease_in_out | 3D | 148 | 116 | [img](KEYFRAMES/V4/V4_shot025_0039.97s.jpg) |
| 26 | 00:41.87 | 00:42.47 | 0.60 | Pia. | push_in | ease_out (fast start, decelerating) |  | 126 | 162 | [img](KEYFRAMES/V4/V4_shot026_0041.87s.jpg) |
| 27 | 00:42.47 | 00:43.87 | 1.40 | Every morning at 7 o 'clock, | push_in | linear/constant | 3D | 120 | 137 | [img](KEYFRAMES/V4/V4_shot027_0042.47s.jpg) |
| 28 | 00:43.87 | 00:45.30 | 1.43 | she jumps on my bed and yells, | push_in | ease_out (fast start, decelerating) | 3D | 103 | 161 | [img](KEYFRAMES/V4/V4_shot028_0043.87s.jpg) |
| 29 | 00:45.30 | 00:46.83 | 1.53 | Wake up! Right in my ear. | push_in | ease_in (accelerating) | 3D | 138 | 105 | [img](KEYFRAMES/V4/V4_shot029_0045.30s.jpg) |
| 30 | 00:46.83 | 00:48.27 | 1.43 | She's six, and she's never been | slow_drift | ease_in_out | 3D | 102 | 165 | [img](KEYFRAMES/V4/V4_shot030_0046.83s.jpg) |
| 31 | 00:48.27 | 00:49.10 | 0.83 | late once. | slow_drift | ease_out (fast start, decelerating) | 3D | 115 | 150 | [img](KEYFRAMES/V4/V4_shot031_0048.27s.jpg) |
| 32 | 00:49.10 | 00:49.83 | 0.73 | Then one day, | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 54 | 132 | [img](KEYFRAMES/V4/V4_shot032_0049.10s.jpg) |
| 33 | 00:49.83 | 00:51.43 | 1.60 | Mr. Grimsby opened an umbrella store | slow_drift | ease_out (fast start, decelerating) | 3D | 38 | 168 | [img](KEYFRAMES/V4/V4_shot033_0049.83s.jpg) |
| 34 | 00:51.43 | 00:52.60 | 1.17 | at the top of Hill Street. | slow_drift | linear/constant | ≈static | 107 | 112 | [img](KEYFRAMES/V4/V4_shot034_0051.43s.jpg) |
| 35 | 00:52.60 | 00:54.27 | 1.67 | Mr. Grimsby was the only one in town | push_in | ease_in (accelerating) | 3D | 59 | 133 | [img](KEYFRAMES/V4/V4_shot035_0052.60s.jpg) |
| 36 | 00:54.27 | 00:56.37 | 2.10 | willing to wake up at midnight every night. | push_in | linear/constant | 3D | 93 | 156 | [img](KEYFRAMES/V4/V4_shot036_0054.27s.jpg) |
| 37 | 00:56.37 | 00:57.80 | 1.43 | So, he went to bed at 9 o 'clock | slow_drift | ease_in_out | 3D | 90 | 202 | [img](KEYFRAMES/V4/V4_shot037_0056.37s.jpg) |
| 38 | 00:57.80 | 00:58.93 | 1.13 | in his basement, where it's | push_in | linear/constant | 3D | 82 | 221 | [img](KEYFRAMES/V4/V4_shot038_0057.80s.jpg) |
| 39 | 00:58.93 | 01:02.57 | 3.63 | quiet, and set his alarm for 12 o 'clock. It takes him three rings to wake up, | slow_drift | ease_in (accelerating) | 3D | 93 | 184 | [img](KEYFRAMES/V4/V4_shot039_0058.93s.jpg) |
| 40 | 01:02.57 | 01:04.37 | 1.80 | but Grandma never stood a chance. | push_in | linear/constant | 3D | 91 | 154 | [img](KEYFRAMES/V4/V4_shot040_0062.57s.jpg) |
| 41 | 01:04.37 | 01:05.20 | 0.83 | That first night, | push_in | linear/constant | 3D | 99 | 173 | [img](KEYFRAMES/V4/V4_shot041_0064.37s.jpg) |
| 42 | 01:05.20 | 01:05.67 | 0.47 | he picked a | push_in | ease_out (fast start, decelerating) |  | 116 | 136 | [img](KEYFRAMES/V4/V4_shot042_0065.20s.jpg) |
| 43 | 01:05.67 | 01:06.03 | 0.37 | hurricane. | push_in | n/a |  | 142 | 131 | [img](KEYFRAMES/V4/V4_shot043_0065.67s.jpg) |
| 44 | 01:06.03 | 01:06.30 | 0.27 |  | push_in | n/a |  | 159 | 133 | [img](KEYFRAMES/V4/V4_shot044_0066.03s.jpg) |
| 45 | 01:06.30 | 01:07.07 | 0.77 | It was so loud | push_in | ease_out (fast start, decelerating) |  | 126 | 128 | [img](KEYFRAMES/V4/V4_shot045_0066.30s.jpg) |
| 46 | 01:07.07 | 01:08.67 | 1.60 | that nobody in town could sleep, | pan_or_track_left | ease_out (fast start, decelerating) |  | 151 | 104 | [img](KEYFRAMES/V4/V4_shot046_0067.07s.jpg) |
| 47 | 01:08.67 | 01:09.30 | 0.63 | and every basement | pan_or_track_right | linear/constant |  | 88 | 103 | [img](KEYFRAMES/V4/V4_shot047_0068.67s.jpg) |
| 48 | 01:09.30 | 01:09.80 | 0.50 | but his | push_in | ease_out (fast start, decelerating) |  | 83 | 209 | [img](KEYFRAMES/V4/V4_shot048_0069.30s.jpg) |
| 49 | 01:09.80 | 01:10.93 | 1.13 | was full of water. | push_in | linear/constant | 3D | 128 | 123 | [img](KEYFRAMES/V4/V4_shot049_0069.80s.jpg) |
| 50 | 01:10.93 | 01:11.63 | 0.70 | So nobody else | push_in | linear/constant |  | 80 | 166 | [img](KEYFRAMES/V4/V4_shot050_0070.93s.jpg) |
| 51 | 01:11.63 | 01:12.30 | 0.67 | could wake up, | subject_motion_or_orbit | ease_in (accelerating) |  | 94 | 159 | [img](KEYFRAMES/V4/V4_shot051_0071.63s.jpg) |
| 52 | 01:12.30 | 01:13.27 | 0.97 | and Mr. Grimsby won | push_in | ease_out (fast start, decelerating) | 3D | 59 | 98 | [img](KEYFRAMES/V4/V4_shot052_0072.30s.jpg) |
| 53 | 01:13.27 | 01:14.70 | 1.43 | every single day. | pan_or_track_right | linear/constant |  | 139 | 115 | [img](KEYFRAMES/V4/V4_shot053_0073.27s.jpg) |
| 54 | 01:14.70 | 01:17.07 | 2.37 | He sold umbrellas for $100 each, | push_in | linear/constant | 3D | 119 | 117 | [img](KEYFRAMES/V4/V4_shot054_0074.70s.jpg) |
| 55 | 01:17.07 | 01:19.23 | 2.17 | from a rowboat, smiling the whole time. | slow_drift | ease_in_out | 3D | 110 | 135 | [img](KEYFRAMES/V4/V4_shot055_0077.07s.jpg) |
| 56 | 01:19.23 | 01:20.03 | 0.80 | By the sixth day, | push_in | linear/constant | 3D | 118 | 118 | [img](KEYFRAMES/V4/V4_shot056_0079.23s.jpg) |
| 57 | 01:20.03 | 01:23.17 | 3.13 | the river was up to our windows. Pia's bike floated past, | push_in | ease_in (accelerating) | 3D | 136 | 104 | [img](KEYFRAMES/V4/V4_shot057_0080.03s.jpg) |
| 58 | 01:23.17 | 01:24.40 | 1.23 | then Grandma's tomatoes. The | push_in | ease_out (fast start, decelerating) | 3D | 138 | 109 | [img](KEYFRAMES/V4/V4_shot058_0083.17s.jpg) |
| 59 | 01:24.40 | 01:25.90 | 1.50 | whole town was sitting on their | push_in | linear/constant | 3D | 79 | 152 | [img](KEYFRAMES/V4/V4_shot059_0084.40s.jpg) |
| 60 | 01:25.90 | 01:26.60 | 0.70 | roofs. | push_in | linear/constant |  | 93 | 157 | [img](KEYFRAMES/V4/V4_shot060_0085.90s.jpg) |
| 61 | 01:26.60 | 01:27.50 | 0.90 | Dad set 14 alarms | push_in | linear/constant | 3D | 60 | 156 | [img](KEYFRAMES/V4/V4_shot061_0086.60s.jpg) |
| 62 | 01:27.50 | 01:29.13 | 1.63 | and wore two earplugs, | tilt_or_crane_down | linear/constant |  | 69 | 172 | [img](KEYFRAMES/V4/V4_shot062_0087.50s.jpg) |
| 63 | 01:29.13 | 01:29.80 | 0.67 | but he couldn't fall asleep. | push_in | linear/constant |  | 68 | 157 | [img](KEYFRAMES/V4/V4_shot063_0089.13s.jpg) |
| 64 | 01:29.80 | 01:31.00 | 1.20 | Grandma counted sheep | subject_motion_or_orbit | ease_in (accelerating) |  | 112 | 149 | [img](KEYFRAMES/V4/V4_shot064_0089.80s.jpg) |
| 65 | 01:31.00 | 01:32.63 | 1.63 | all the way to 4 ,000. | push_in | linear/constant | 3D | 97 | 156 | [img](KEYFRAMES/V4/V4_shot065_0091.00s.jpg) |
| 66 | 01:32.63 | 01:35.20 | 2.57 | Mom closed her eyes so hard that she got a headache. | subject_motion_or_orbit | ease_in_out |  | 127 | 130 | [img](KEYFRAMES/V4/V4_shot066_0092.63s.jpg) |
| 67 | 01:35.20 | 01:35.97 | 0.77 | Nothing worked. | push_in | linear/constant |  | 74 | 175 | [img](KEYFRAMES/V4/V4_shot067_0095.20s.jpg) |
| 68 | 01:35.97 | 01:36.53 | 0.57 | Lightning, | subject_motion_or_orbit | linear/constant |  | 77 | 188 | [img](KEYFRAMES/V4/V4_shot068_0095.97s.jpg) |
| 69 | 01:36.53 | 01:37.30 | 0.77 | wind, | push_in | linear/constant |  | 104 | 174 | [img](KEYFRAMES/V4/V4_shot069_0096.53s.jpg) |
| 70 | 01:37.30 | 01:38.33 | 1.03 | thunder, every minute. | slow_drift | ease_out (fast start, decelerating) | 3D | 67 | 183 | [img](KEYFRAMES/V4/V4_shot070_0097.30s.jpg) |
| 71 | 01:38.33 | 01:38.80 | 0.47 | At 11 .58, | slow_drift | linear/constant |  | 75 | 159 | [img](KEYFRAMES/V4/V4_shot071_0098.33s.jpg) |
| 72 | 01:38.80 | 01:39.27 | 0.47 |  | slow_drift | ease_out (fast start, decelerating) |  | 81 | 157 | [img](KEYFRAMES/V4/V4_shot072_0098.80s.jpg) |
| 73 | 01:39.27 | 01:41.60 | 2.33 | I was sitting on our roof with Pia, and I yawned. | push_in | ease_in (accelerating) | 3D | 86 | 187 | [img](KEYFRAMES/V4/V4_shot073_0099.27s.jpg) |
| 74 | 01:41.60 | 01:41.87 | 0.27 | That's | slow_drift | n/a |  | 137 | 121 | [img](KEYFRAMES/V4/V4_shot074_0101.60s.jpg) |
| 75 | 01:41.87 | 01:42.73 | 0.87 | when I remembered. | push_in | ease_in_out | 3D | 146 | 110 | [img](KEYFRAMES/V4/V4_shot075_0101.87s.jpg) |
| 76 | 01:42.73 | 01:44.30 | 1.57 | You have to actually wake up, | slow_drift | ease_in (accelerating) | 3D | 120 | 77 | [img](KEYFRAMES/V4/V4_shot076_0102.73s.jpg) |
| 77 | 01:44.30 | 01:46.33 | 2.03 | and you can't wake up if you never fell asleep. | pan_or_track_left | ease_in_out |  | 74 | 181 | [img](KEYFRAMES/V4/V4_shot077_0104.30s.jpg) |
| 78 | 01:46.33 | 01:46.57 | 0.23 | And in | push_in | n/a |  | 66 | 189 | [img](KEYFRAMES/V4/V4_shot078_0106.33s.jpg) |
| 79 | 01:46.57 | 01:47.17 | 0.60 | a hurricane, | push_in | ease_out (fast start, decelerating) |  | 75 | 178 | [img](KEYFRAMES/V4/V4_shot079_0106.57s.jpg) |
| 80 | 01:47.17 | 01:48.77 | 1.60 | nobody out here could fall asleep, | push_in | ease_in_out | 3D | 89 | 170 | [img](KEYFRAMES/V4/V4_shot080_0107.17s.jpg) |
| 81 | 01:48.77 | 01:49.63 | 0.87 | except me. | push_in | ease_out (fast start, decelerating) | 3D | 135 | 136 | [img](KEYFRAMES/V4/V4_shot081_0108.77s.jpg) |
| 82 | 01:49.63 | 01:52.53 | 2.90 | I handed Pia Dad's watch. Wake me up at 12 o 'clock. At | push_in | linear/constant | 3D | 83 | 184 | [img](KEYFRAMES/V4/V4_shot082_0109.63s.jpg) |
| 83 | 01:52.53 | 01:54.50 | 1.97 | 11 .59 and 58 seconds, | slow_drift | linear/constant | 3D | 108 | 180 | [img](KEYFRAMES/V4/V4_shot083_0112.53s.jpg) |
| 84 | 01:54.50 | 01:56.17 | 1.67 | I lay down on the wet roof. | push_in | linear/constant | 3D | 70 | 184 | [img](KEYFRAMES/V4/V4_shot084_0114.50s.jpg) |
| 85 | 01:56.17 | 01:57.90 | 1.73 | Thunder cracked right over our house. | pan_or_track_right | ease_in (accelerating) |  | 95 | 170 | [img](KEYFRAMES/V4/V4_shot085_0116.17s.jpg) |
| 86 | 01:57.90 | 01:59.13 | 1.23 | I was asleep before it | slow_drift | ease_out (fast start, decelerating) | 3D | 138 | 117 | [img](KEYFRAMES/V4/V4_shot086_0117.90s.jpg) |
| 87 | 01:59.13 | 02:00.73 | 1.60 | finished. Pia watched the watch, | slow_drift | ease_out (fast start, decelerating) | 2D | 101 | 177 | [img](KEYFRAMES/V4/V4_shot087_0119.13s.jpg) |
| 88 | 02:00.73 | 02:02.73 | 2.00 | and the whole street watched from their roofs. | push_in | linear/constant | 3D | 69 | 182 | [img](KEYFRAMES/V4/V4_shot088_0120.73s.jpg) |
| 89 | 02:02.73 | 02:04.27 | 1.53 | Three, two, one. | slow_drift | linear/constant | 3D | 110 | 181 | [img](KEYFRAMES/V4/V4_shot089_0122.73s.jpg) |
| 90 | 02:04.27 | 02:05.90 | 1.63 | She jumped on me with both feet. | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 76 | 163 | [img](KEYFRAMES/V4/V4_shot090_0124.27s.jpg) |
| 91 | 02:05.90 | 02:06.50 | 0.60 | Wake up! | push_in | linear/constant |  | 108 | 170 | [img](KEYFRAMES/V4/V4_shot091_0125.90s.jpg) |
| 92 | 02:06.50 | 02:10.50 | 4.00 | *(TikTok end card)* | slow_drift | linear/constant |  | 21 | 116 | [img](KEYFRAMES/V4/V4_shot092_0126.50s.jpg) |

### V5 — `0863af51-v26044gc0000dc3kj67og65i4pmu3dkg.mp4` — 3592 frames, 55 shots

| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 00:00.00 | 00:03.53 | 3.53 | In this town, there's a haystack, five million straws, | pull_out | ease_out (fast start, decelerating) | 3D | 139 | 178 | [img](KEYFRAMES/V5/V5_shot000_0000.00s.jpg) |
| 1 | 00:03.53 | 00:06.23 | 2.70 | and somewhere inside, one golden needle. | push_in | ease_in_out | 3D | 107 | 242 | [img](KEYFRAMES/V5/V5_shot001_0003.53s.jpg) |
| 2 | 00:06.23 | 00:08.13 | 1.90 | It's worth more than the whole town. | push_in | ease_in_out | 3D | 101 | 242 | [img](KEYFRAMES/V5/V5_shot002_0006.23s.jpg) |
| 3 | 00:08.13 | 00:09.67 | 1.53 | Nobody has ever found it. | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 122 | 145 | [img](KEYFRAMES/V5/V5_shot003_0008.13s.jpg) |
| 4 | 00:09.67 | 00:12.17 | 2.50 | See that guy? He's been digging since he was nine. | push_in | ease_in_out | 3D | 153 | 186 | [img](KEYFRAMES/V5/V5_shot004_0009.67s.jpg) |
| 5 | 00:12.17 | 00:13.87 | 1.70 | He's 41. So far, | push_in | ease_in_out | 3D | 123 | 184 | [img](KEYFRAMES/V5/V5_shot005_0012.17s.jpg) |
| 6 | 00:13.87 | 00:14.87 | 1.00 | he's found a boot. | push_in | ease_in_out | 3D | 148 | 191 | [img](KEYFRAMES/V5/V5_shot006_0013.87s.jpg) |
| 7 | 00:14.87 | 00:17.50 | 2.63 | My name is Eli, and in our town, everybody digs. | push_in | ease_in_out | 3D | 143 | 165 | [img](KEYFRAMES/V5/V5_shot007_0014.87s.jpg) |
| 8 | 00:17.50 | 00:18.53 | 1.03 | Before school, | push_in | ease_in (accelerating) | 3D | 130 | 198 | [img](KEYFRAMES/V5/V5_shot008_0017.50s.jpg) |
| 9 | 00:18.53 | 00:19.40 | 0.87 | after work, | push_in | linear/constant | 3D | 116 | 213 | [img](KEYFRAMES/V5/V5_shot009_0018.53s.jpg) |
| 10 | 00:19.40 | 00:20.13 | 0.73 | on Christmas. | push_in | ease_in_out |  | 168 | 126 | [img](KEYFRAMES/V5/V5_shot010_0019.40s.jpg) |
| 11 | 00:20.13 | 00:22.00 | 1.87 | Here's how it works. You pull out hay, | push_in | ease_in_out | 3D | 149 | 185 | [img](KEYFRAMES/V5/V5_shot011_0020.13s.jpg) |
| 12 | 00:22.00 | 00:25.60 | 3.60 | you carry it to the cow, and the cow pays you one coin a straw. | pan_or_track_right | ease_out (fast start, decelerating) |  | 153 | 156 | [img](KEYFRAMES/V5/V5_shot012_0022.00s.jpg) |
| 13 | 00:25.60 | 00:28.27 | 2.67 | Our cow has eaten two million straws. | push_in | ease_out (fast start, decelerating) | 3D | 161 | 159 | [img](KEYFRAMES/V5/V5_shot013_0025.60s.jpg) |
| 14 | 00:28.27 | 00:30.27 | 2.00 | She owns the bank. She has a driver. | push_in | linear/constant | 3D | 152 | 144 | [img](KEYFRAMES/V5/V5_shot014_0028.27s.jpg) |
| 15 | 00:30.27 | 00:32.07 | 1.80 | With the coins, you buy tools. | push_in | ease_in_out | 3D | 150 | 131 | [img](KEYFRAMES/V5/V5_shot015_0030.27s.jpg) |
| 16 | 00:32.07 | 00:34.93 | 2.87 | A pitchfork, a leaf blower, a vacuum. My neighbor bought | push_in | linear/constant | 3D | 151 | 172 | [img](KEYFRAMES/V5/V5_shot016_0032.07s.jpg) |
| 17 | 00:34.93 | 00:35.57 | 0.63 | dynamite. | push_in | ease_out (fast start, decelerating) |  | 131 | 174 | [img](KEYFRAMES/V5/V5_shot017_0034.93s.jpg) |
| 18 | 00:35.57 | 00:36.57 | 1.00 | Now | tilt_or_crane_up | ease_in (accelerating) |  | 176 | 178 | [img](KEYFRAMES/V5/V5_shot018_0035.57s.jpg) |
| 19 | 00:36.57 | 00:37.80 | 1.23 | he lives in a crater, | tilt_or_crane_up | ease_in (accelerating) |  | 151 | 171 | [img](KEYFRAMES/V5/V5_shot019_0036.57s.jpg) |
| 20 | 00:37.80 | 00:41.03 | 3.23 | and people cheat. My uncle painted a toothpick gold. | push_in | ease_out (fast start, decelerating) | 3D | 91 | 173 | [img](KEYFRAMES/V5/V5_shot020_0037.80s.jpg) |
| 21 | 00:41.03 | 00:42.23 | 1.20 | He sold it twice. | push_in | ease_in_out | 3D | 134 | 132 | [img](KEYFRAMES/V5/V5_shot021_0041.03s.jpg) |
| 22 | 00:42.23 | 00:44.87 | 2.63 | And by the way, if you wanna make videos like this, check my profile. | slow_drift | ease_in (accelerating) | 3D | 112 | 143 | [img](KEYFRAMES/V5/V5_shot022_0042.23s.jpg) |
| 23 | 00:44.87 | 00:46.47 | 1.60 | My grandma doesn't need tools. | pull_out | ease_in (accelerating) | 3D | 157 | 145 | [img](KEYFRAMES/V5/V5_shot023_0044.87s.jpg) |
| 24 | 00:46.47 | 00:51.67 | 5.20 | She just walks in and comes out the other side with her arms full. She says the hay is … | pull_out | ease_in (accelerating) | 3D | 146 | 182 | [img](KEYFRAMES/V5/V5_shot024_0046.47s.jpg) |
| 25 | 00:51.67 | 00:53.00 | 1.33 | And me? I have a spoon. | push_in | ease_in (accelerating) | 3D | 133 | 181 | [img](KEYFRAMES/V5/V5_shot025_0051.67s.jpg) |
| 26 | 00:53.00 | 00:53.77 | 0.77 | On a good day, | push_in | ease_in_out |  | 153 | 182 | [img](KEYFRAMES/V5/V5_shot026_0053.00s.jpg) |
| 27 | 00:53.77 | 00:55.27 | 1.50 | I move nine straws. And | slow_drift | ease_in_out | 3D | 149 | 179 | [img](KEYFRAMES/V5/V5_shot027_0053.77s.jpg) |
| 28 | 00:55.27 | 00:57.27 | 2.00 | I have a frog. His name is Kevin. On | tilt_or_crane_up | ease_in_out |  | 121 | 190 | [img](KEYFRAMES/V5/V5_shot028_0055.27s.jpg) |
| 29 | 00:57.27 | 01:02.03 | 4.77 | day one, Kevin jumped into the hay. So now I'm looking for a frog in a haystack. | slow_drift | ease_out (fast start, decelerating) | 3D | 132 | 196 | [img](KEYFRAMES/V5/V5_shot029_0057.27s.jpg) |
| 30 | 01:02.03 | 01:02.90 | 0.87 | That's worse. | push_in | ease_in (accelerating) | 3D | 135 | 180 | [img](KEYFRAMES/V5/V5_shot030_0062.03s.jpg) |
| 31 | 01:02.90 | 01:04.03 | 1.13 | The frog moves. | push_in | ease_in_out | 3D | 142 | 190 | [img](KEYFRAMES/V5/V5_shot031_0062.90s.jpg) |
| 32 | 01:04.03 | 01:05.83 | 1.80 | But you find all kinds of things in there. | push_in | ease_in_out | 3D | 153 | 190 | [img](KEYFRAMES/V5/V5_shot032_0064.03s.jpg) |
| 33 | 01:05.83 | 01:06.67 | 0.83 | Car keys, | push_in | ease_in_out | 3D | 134 | 193 | [img](KEYFRAMES/V5/V5_shot033_0065.83s.jpg) |
| 34 | 01:06.67 | 01:09.80 | 3.13 | a piano. My dad, he'd been missing since Tuesday. | push_in | ease_in (accelerating) | 3D | 151 | 179 | [img](KEYFRAMES/V5/V5_shot034_0066.67s.jpg) |
| 35 | 01:09.80 | 01:12.33 | 2.53 | Last week, the whole town said enough. Everybody, | push_in | ease_in (accelerating) | 3D | 146 | 129 | [img](KEYFRAMES/V5/V5_shot035_0069.80s.jpg) |
| 36 | 01:12.33 | 01:18.23 | 5.90 | all at once. Pitchforks, blowers, vacuums, grandma. Even the dynamite guy came back. | pan_or_track_left | ease_in_out |  | 134 | 140 | [img](KEYFRAMES/V5/V5_shot036_0072.33s.jpg) |
| 37 | 01:18.23 | 01:18.67 | 0.43 | We gave him | push_in | n/a |  | 146 | 154 | [img](KEYFRAMES/V5/V5_shot037_0078.23s.jpg) |
| 38 | 01:18.67 | 01:19.43 | 0.77 | the far side. | push_in | ease_out (fast start, decelerating) |  | 155 | 160 | [img](KEYFRAMES/V5/V5_shot038_0078.67s.jpg) |
| 39 | 01:19.43 | 01:23.90 | 4.47 | We dug for three days. The mountain became a hill. The hill became a pile. | pull_out | ease_out (fast start, decelerating) | 3D | 128 | 167 | [img](KEYFRAMES/V5/V5_shot039_0079.43s.jpg) |
| 40 | 01:23.90 | 01:26.17 | 2.27 | And then, there was one straw left. The | push_in | ease_out (fast start, decelerating) |  | 130 | 162 | [img](KEYFRAMES/V5/V5_shot040_0083.90s.jpg) |
| 41 | 01:26.17 | 01:27.60 | 1.43 | mayor lifted it. | tilt_or_crane_up | ease_in (accelerating) |  | 112 | 146 | [img](KEYFRAMES/V5/V5_shot041_0086.17s.jpg) |
| 42 | 01:27.60 | 01:28.90 | 1.30 | Nothing, no needle, | tilt_or_crane_up | ease_in_out |  | 100 | 157 | [img](KEYFRAMES/V5/V5_shot042_0087.60s.jpg) |
| 43 | 01:28.90 | 01:29.73 | 0.83 | just Kevin. | push_in | ease_in_out | 3D | 90 | 184 | [img](KEYFRAMES/V5/V5_shot043_0088.90s.jpg) |
| 44 | 01:29.73 | 01:31.53 | 1.80 | Nobody said a word. The | static | n/a |  | 120 | 148 | [img](KEYFRAMES/V5/V5_shot044_0089.73s.jpg) |
| 45 | 01:31.53 | 01:32.43 | 0.90 | cow burped. | push_in | ease_in_out | 3D | 145 | 128 | [img](KEYFRAMES/V5/V5_shot045_0091.53s.jpg) |
| 46 | 01:32.43 | 01:33.90 | 1.47 | And my grandma gave me a hug. | slow_drift | ease_in_out | 3D | 127 | 133 | [img](KEYFRAMES/V5/V5_shot046_0092.43s.jpg) |
| 47 | 01:33.90 | 01:36.67 | 2.77 | That's when I saw it. Something shiny in her hair. | pan_or_track_right | ease_in_out |  | 145 | 134 | [img](KEYFRAMES/V5/V5_shot047_0093.90s.jpg) |
| 48 | 01:36.67 | 01:37.90 | 1.23 | Grandma, what is that? | static | n/a |  | 121 | 129 | [img](KEYFRAMES/V5/V5_shot048_0096.67s.jpg) |
| 49 | 01:37.90 | 01:41.40 | 3.50 | This old thing? I found it in the hay when I was six. It holds my bun. | slow_drift | ease_in (accelerating) | 3D | 126 | 125 | [img](KEYFRAMES/V5/V5_shot049_0097.90s.jpg) |
| 50 | 01:41.40 | 01:44.90 | 3.50 | So that's how I found the golden needle with a spoon and a hug. | slow_drift | ease_out (fast start, decelerating) | 3D | 119 | 167 | [img](KEYFRAMES/V5/V5_shot050_0101.40s.jpg) |
| 51 | 01:44.90 | 01:47.37 | 2.47 | We're rich now. Kevin has a golden pond. | slow_drift | ease_out (fast start, decelerating) | 3D | 165 | 157 | [img](KEYFRAMES/V5/V5_shot051_0104.90s.jpg) |
| 52 | 01:47.37 | 01:49.87 | 2.50 | And grandma has a new hairpin. It's a toothpick. | push_in | ease_in_out | 3D | 163 | 95 | [img](KEYFRAMES/V5/V5_shot052_0107.37s.jpg) |
| 53 | 01:49.87 | 01:55.73 | 5.87 | And you? It was in this video the whole time. Since the very first shot. Did you see it… | push_in | ease_in (accelerating) | 3D | 154 | 123 | [img](KEYFRAMES/V5/V5_shot053_0109.87s.jpg) |
| 54 | 01:55.73 | 01:59.73 | 4.00 | *(TikTok end card)* | slow_drift | linear/constant |  | 21 | 116 | [img](KEYFRAMES/V5/V5_shot054_0115.73s.jpg) |

### V6 — `2f32ac23-v26044gc0000dbrq2fvog65vje5kn6j0.mp4` — 3723 frames, 84 shots

| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 00:00.00 | 00:00.53 | 0.53 | In this town, | push_in | ease_out (fast start, decelerating) |  | 110 | 99 | [img](KEYFRAMES/V6/V6_shot000_0000.00s.jpg) |
| 1 | 00:00.53 | 00:01.50 | 0.97 | when someone dies, | push_in | ease_out (fast start, decelerating) | 3D | 94 | 72 | [img](KEYFRAMES/V6/V6_shot001_0000.53s.jpg) |
| 2 | 00:01.50 | 00:02.67 | 1.17 | they get one more day. | subject_motion_or_orbit | linear/constant |  | 108 | 106 | [img](KEYFRAMES/V6/V6_shot002_0001.50s.jpg) |
| 3 | 00:02.67 | 00:04.03 | 1.37 | We call it the visit. | push_in | ease_in_out | 2D | 166 | 81 | [img](KEYFRAMES/V6/V6_shot003_0002.67s.jpg) |
| 4 | 00:04.03 | 00:05.37 | 1.33 | They come back at sunrise and | push_in | ease_in_out | 3D | 106 | 98 | [img](KEYFRAMES/V6/V6_shot004_0004.03s.jpg) |
| 5 | 00:05.37 | 00:06.60 | 1.23 | they leave at sunset. | tilt_or_crane_up | linear/constant |  | 99 | 135 | [img](KEYFRAMES/V6/V6_shot005_0005.37s.jpg) |
| 6 | 00:06.60 | 00:07.33 | 0.73 | They eat, | push_in | linear/constant |  | 116 | 135 | [img](KEYFRAMES/V6/V6_shot006_0006.60s.jpg) |
| 7 | 00:07.33 | 00:08.07 | 0.73 | they laugh, | subject_motion_or_orbit | ease_in (accelerating) |  | 138 | 131 | [img](KEYFRAMES/V6/V6_shot007_0007.33s.jpg) |
| 8 | 00:08.07 | 00:08.70 | 0.63 | they hug you, | push_in | ease_in (accelerating) |  | 114 | 155 | [img](KEYFRAMES/V6/V6_shot008_0008.07s.jpg) |
| 9 | 00:08.70 | 00:09.73 | 1.03 | just like before. | push_in | ease_in_out | 3D | 134 | 154 | [img](KEYFRAMES/V6/V6_shot009_0008.70s.jpg) |
| 10 | 00:09.73 | 00:11.67 | 1.93 | But visitors don't show up in mirrors. | slow_drift | ease_in_out | 3D | 100 | 107 | [img](KEYFRAMES/V6/V6_shot010_0009.73s.jpg) |
| 11 | 00:11.67 | 00:13.50 | 1.83 | Their footprints melt right out of the snow | pan_or_track_left | ease_in_out |  | 104 | 141 | [img](KEYFRAMES/V6/V6_shot011_0011.67s.jpg) |
| 12 | 00:13.50 | 00:15.40 | 1.90 | and they never remember how they died. | static | n/a |  | 114 | 131 | [img](KEYFRAMES/V6/V6_shot012_0013.50s.jpg) |
| 13 | 00:15.40 | 00:16.67 | 1.27 | And there's one rule, | pan_or_track_left | ease_out (fast start, decelerating) |  | 96 | 105 | [img](KEYFRAMES/V6/V6_shot013_0015.40s.jpg) |
| 14 | 00:16.67 | 00:18.50 | 1.83 | you never tell a visitor they're dead. | static | n/a |  | 119 | 130 | [img](KEYFRAMES/V6/V6_shot014_0016.67s.jpg) |
| 15 | 00:18.50 | 00:19.57 | 1.07 | If they figure it out, | push_in | ease_in_out | 3D | 122 | 82 | [img](KEYFRAMES/V6/V6_shot015_0018.50s.jpg) |
| 16 | 00:19.57 | 00:20.83 | 1.27 | they vanish on the spot. | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 122 | 88 | [img](KEYFRAMES/V6/V6_shot016_0019.57s.jpg) |
| 17 | 00:20.83 | 00:21.87 | 1.03 | No goodbye. | push_in | ease_in (accelerating) | 3D | 123 | 104 | [img](KEYFRAMES/V6/V6_shot017_0020.83s.jpg) |
| 18 | 00:21.87 | 00:24.40 | 2.53 | So on visit days, families cover every mirror, | slow_drift | ease_in_out | 2D | 116 | 140 | [img](KEYFRAMES/V6/V6_shot018_0021.87s.jpg) |
| 19 | 00:24.40 | 00:25.33 | 0.93 | hide the newspaper, | pan_or_track_right | ease_out (fast start, decelerating) |  | 111 | 137 | [img](KEYFRAMES/V6/V6_shot019_0024.40s.jpg) |
| 20 | 00:25.33 | 00:26.93 | 1.60 | and smile way too much. | push_in | ease_in_out | 3D | 124 | 148 | [img](KEYFRAMES/V6/V6_shot020_0025.33s.jpg) |
| 21 | 00:26.93 | 00:29.20 | 2.27 | On 12, my little sister Lily is seven. | push_in | ease_out (fast start, decelerating) | 3D | 112 | 106 | [img](KEYFRAMES/V6/V6_shot021_0026.93s.jpg) |
| 22 | 00:29.20 | 00:32.30 | 3.10 | Last winter, Lily fell through the ice on Miller Pond. | slow_drift | ease_in_out | 3D | 123 | 18 | [img](KEYFRAMES/V6/V6_shot022_0029.20s.jpg) |
| 23 | 00:32.30 | 00:33.03 | 0.73 | This morning, | push_in | ease_in_out |  | 105 | 166 | [img](KEYFRAMES/V6/V6_shot023_0032.30s.jpg) |
| 24 | 00:33.03 | 00:34.30 | 1.27 | every mirror in our house | push_in | ease_in_out | 3D | 109 | 105 | [img](KEYFRAMES/V6/V6_shot024_0033.03s.jpg) |
| 25 | 00:34.30 | 00:35.53 | 1.23 | was covered with a bed sheet. | push_in | ease_in_out | 3D | 139 | 72 | [img](KEYFRAMES/V6/V6_shot025_0034.30s.jpg) |
| 26 | 00:35.53 | 00:36.67 | 1.13 | Dad called in sick. | slow_drift | ease_out (fast start, decelerating) | 3D | 101 | 109 | [img](KEYFRAMES/V6/V6_shot026_0035.53s.jpg) |
| 27 | 00:36.67 | 00:38.30 | 1.63 | Mom made chocolate chip pancakes. | push_in | ease_in_out | 3D | 142 | 159 | [img](KEYFRAMES/V6/V6_shot027_0036.67s.jpg) |
| 28 | 00:38.30 | 00:40.13 | 1.83 | Nobody had made those since the pond. | subject_motion_or_orbit | ease_in_out |  | 108 | 102 | [img](KEYFRAMES/V6/V6_shot028_0038.30s.jpg) |
| 29 | 00:40.13 | 00:41.10 | 0.97 | So I knew, | push_in | ease_in_out | 3D | 124 | 133 | [img](KEYFRAMES/V6/V6_shot029_0040.13s.jpg) |
| 30 | 00:41.10 | 00:42.63 | 1.53 | today was Lily's visit. | push_in | ease_in_out | 3D | 151 | 116 | [img](KEYFRAMES/V6/V6_shot030_0041.10s.jpg) |
| 31 | 00:42.63 | 00:44.77 | 2.13 | And I swore she would never find out. | slow_drift | ease_in_out | 3D | 115 | 155 | [img](KEYFRAMES/V6/V6_shot031_0042.63s.jpg) |
| 32 | 00:44.77 | 00:45.90 | 1.13 | I hid the newspaper. | push_in | ease_in_out | 3D | 111 | 136 | [img](KEYFRAMES/V6/V6_shot032_0044.77s.jpg) |
| 33 | 00:45.90 | 00:46.67 | 0.77 | I unplugged | slow_drift | ease_out (fast start, decelerating) |  | 108 | 159 | [img](KEYFRAMES/V6/V6_shot033_0045.90s.jpg) |
| 34 | 00:46.67 | 00:47.03 | 0.37 | the TV. | push_in | n/a |  | 95 | 167 | [img](KEYFRAMES/V6/V6_shot034_0046.67s.jpg) |
| 35 | 00:47.03 | 00:48.50 | 1.47 | When she asked why Mom was crying, | push_in | ease_in_out | 3D | 120 | 100 | [img](KEYFRAMES/V6/V6_shot035_0047.03s.jpg) |
| 36 | 00:48.50 | 00:49.70 | 1.20 | I said, onions. | pan_or_track_left | ease_out (fast start, decelerating) |  | 123 | 144 | [img](KEYFRAMES/V6/V6_shot036_0048.50s.jpg) |
| 37 | 00:49.70 | 00:52.17 | 2.47 | All day, Lily wouldn't let go of my hand. | slow_drift | ease_in_out | 3D | 103 | 124 | [img](KEYFRAMES/V6/V6_shot037_0049.70s.jpg) |
| 38 | 00:52.17 | 00:52.80 | 0.63 | Outside, | push_in | ease_in (accelerating) |  | 115 | 81 | [img](KEYFRAMES/V6/V6_shot038_0052.17s.jpg) |
| 39 | 00:52.80 | 00:54.77 | 1.97 | she walked behind me, stepping in my footprints like | pan_or_track_right | ease_in_out |  | 114 | 113 | [img](KEYFRAMES/V6/V6_shot039_0052.80s.jpg) |
| 40 | 00:54.77 | 00:55.60 | 0.83 | she used to. | pan_or_track_right | ease_in_out |  | 120 | 28 | [img](KEYFRAMES/V6/V6_shot040_0054.77s.jpg) |
| 41 | 00:55.60 | 00:56.57 | 0.97 | Our dog Biscuit | push_in | ease_in (accelerating) | 3D | 113 | 116 | [img](KEYFRAMES/V6/V6_shot041_0055.60s.jpg) |
| 42 | 00:56.57 | 00:57.73 | 1.17 | hid under the porch and whimpered | push_in | ease_in_out | 3D | 98 | 131 | [img](KEYFRAMES/V6/V6_shot042_0056.57s.jpg) |
| 43 | 00:57.73 | 00:59.23 | 1.50 | every time we came close. | slow_drift | ease_in_out | 3D | 114 | 119 | [img](KEYFRAMES/V6/V6_shot043_0057.73s.jpg) |
| 44 | 00:59.23 | 01:00.77 | 1.53 | And Dad kept staring at us | push_in | ease_in (accelerating) | 3D | 96 | 126 | [img](KEYFRAMES/V6/V6_shot044_0059.23s.jpg) |
| 45 | 01:00.77 | 01:02.53 | 1.77 | like he was trying to memorize a face. | push_in | linear/constant | 3D | 95 | 113 | [img](KEYFRAMES/V6/V6_shot045_0060.77s.jpg) |
| 46 | 01:02.53 | 01:03.53 | 1.00 | At four o 'clock, | push_in | ease_in_out | 3D | 132 | 70 | [img](KEYFRAMES/V6/V6_shot046_0062.53s.jpg) |
| 47 | 01:03.53 | 01:05.37 | 1.83 | Lily let go of my hand and ran, | push_in | ease_in (accelerating) | 3D | 103 | 107 | [img](KEYFRAMES/V6/V6_shot047_0063.53s.jpg) |
| 48 | 01:05.37 | 01:06.77 | 1.40 | straight toward Miller Pond. | static | n/a |  | 102 | 128 | [img](KEYFRAMES/V6/V6_shot048_0065.37s.jpg) |
| 49 | 01:06.77 | 01:08.10 | 1.33 | I chased her through the snow, | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 100 | 130 | [img](KEYFRAMES/V6/V6_shot049_0066.77s.jpg) |
| 50 | 01:08.10 | 01:09.03 | 0.93 | screaming her name. | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 101 | 159 | [img](KEYFRAMES/V6/V6_shot050_0068.10s.jpg) |
| 51 | 01:09.03 | 01:10.93 | 1.90 | If she saw that pond, she'd remember, | push_in | ease_in_out |  | 106 | 128 | [img](KEYFRAMES/V6/V6_shot051_0069.03s.jpg) |
| 52 | 01:10.93 | 01:12.17 | 1.23 | and she'd be gone. | push_in | ease_out (fast start, decelerating) | 3D | 98 | 207 | [img](KEYFRAMES/V6/V6_shot052_0070.93s.jpg) |
| 53 | 01:12.17 | 01:13.63 | 1.47 | She stopped right at the edge, | pull_out | ease_out (fast start, decelerating) | 3D | 100 | 153 | [img](KEYFRAMES/V6/V6_shot053_0072.17s.jpg) |
| 54 | 01:13.63 | 01:14.37 | 0.73 | crying. | push_in | linear/constant |  | 97 | 175 | [img](KEYFRAMES/V6/V6_shot054_0073.63s.jpg) |
| 55 | 01:14.37 | 01:16.27 | 1.90 | This is where you saved me, she said. | static | n/a |  | 98 | 172 | [img](KEYFRAMES/V6/V6_shot055_0074.37s.jpg) |
| 56 | 01:16.27 | 01:17.90 | 1.63 | You pushed me up onto the ice, | slow_drift | ease_out (fast start, decelerating) | 3D | 120 | 28 | [img](KEYFRAMES/V6/V6_shot056_0076.27s.jpg) |
| 57 | 01:17.90 | 01:19.43 | 1.53 | but you didn't come back up. | static | n/a |  | 120 | 23 | [img](KEYFRAMES/V6/V6_shot057_0077.90s.jpg) |
| 58 | 01:19.43 | 01:21.30 | 1.87 | I looked down at the frozen pond. | static | n/a |  | 95 | 147 | [img](KEYFRAMES/V6/V6_shot058_0079.43s.jpg) |
| 59 | 01:21.30 | 01:25.20 | 3.90 | Lily's reflection was there, crying. Next to her, there was a nobody. | slow_drift | ease_in (accelerating) | 3D | 93 | 98 | [img](KEYFRAMES/V6/V6_shot059_0081.30s.jpg) |
| 60 | 01:25.20 | 01:26.40 | 1.20 | I looked behind us, | slow_drift | ease_in (accelerating) |  | 95 | 135 | [img](KEYFRAMES/V6/V6_shot060_0085.20s.jpg) |
| 61 | 01:26.40 | 01:27.73 | 1.33 | one set of footprints, | push_in | ease_in_out | 3D | 97 | 97 | [img](KEYFRAMES/V6/V6_shot061_0086.40s.jpg) |
| 62 | 01:27.73 | 01:28.37 | 0.63 | small ones. | push_in | ease_in (accelerating) |  | 137 | 67 | [img](KEYFRAMES/V6/V6_shot062_0087.73s.jpg) |
| 63 | 01:28.37 | 01:30.53 | 2.17 | Lily wasn't stepping in my footprints. | pan_or_track_right | ease_in_out |  | 117 | 35 | [img](KEYFRAMES/V6/V6_shot063_0088.37s.jpg) |
| 64 | 01:30.53 | 01:31.97 | 1.43 | She was making them work. | pan_or_track_right | ease_in_out |  | 118 | 54 | [img](KEYFRAMES/V6/V6_shot064_0090.53s.jpg) |
| 65 | 01:31.97 | 01:32.90 | 0.93 | The mirrors, | pan_or_track_left | ease_out (fast start, decelerating) |  | 166 | 45 | [img](KEYFRAMES/V6/V6_shot065_0091.97s.jpg) |
| 66 | 01:32.90 | 01:33.73 | 0.83 | the pancakes, | pan_or_track_right | ease_out (fast start, decelerating) |  | 158 | 88 | [img](KEYFRAMES/V6/V6_shot066_0092.90s.jpg) |
| 67 | 01:33.73 | 01:35.10 | 1.37 | Dad memorizing a face. | pan_or_track_left | ease_out (fast start, decelerating) |  | 113 | 68 | [img](KEYFRAMES/V6/V6_shot067_0093.73s.jpg) |
| 68 | 01:35.10 | 01:36.57 | 1.47 | It was never Lily's visit, | pan_or_track_left | ease_out (fast start, decelerating) |  | 93 | 150 | [img](KEYFRAMES/V6/V6_shot068_0095.10s.jpg) |
| 69 | 01:36.57 | 01:37.63 | 1.07 | it was mine. | push_in | ease_in (accelerating) | 3D | 97 | 164 | [img](KEYFRAMES/V6/V6_shot069_0096.57s.jpg) |
| 70 | 01:37.63 | 01:39.63 | 2.00 | Why did you tell me? I whispered, | subject_motion_or_orbit | ease_in (accelerating) |  | 96 | 203 | [img](KEYFRAMES/V6/V6_shot070_0097.63s.jpg) |
| 71 | 01:39.63 | 01:40.87 | 1.23 | now I'll finish. | push_in | ease_in (accelerating) | 3D | 92 | 208 | [img](KEYFRAMES/V6/V6_shot071_0099.63s.jpg) |
| 72 | 01:40.87 | 01:42.53 | 1.67 | She wiped her nose on her mitt. | slow_drift | ease_in_out | 3D | 98 | 196 | [img](KEYFRAMES/V6/V6_shot072_0100.87s.jpg) |
| 73 | 01:42.53 | 01:44.47 | 1.93 | The sun's going down anyway, she said, | static | n/a |  | 102 | 137 | [img](KEYFRAMES/V6/V6_shot073_0102.53s.jpg) |
| 74 | 01:44.47 | 01:46.27 | 1.80 | and I never got to say thank you. | slow_drift | ease_in (accelerating) | 3D | 98 | 194 | [img](KEYFRAMES/V6/V6_shot074_0104.47s.jpg) |
| 75 | 01:46.27 | 01:48.30 | 2.03 | So I hugged her as hard as I could. | slow_drift | ease_in_out | 3D | 98 | 171 | [img](KEYFRAMES/V6/V6_shot075_0106.27s.jpg) |
| 76 | 01:48.30 | 01:50.03 | 1.73 | Stay off the ice, I said, | slow_drift | ease_in (accelerating) | 3D | 94 | 202 | [img](KEYFRAMES/V6/V6_shot076_0108.30s.jpg) |
| 77 | 01:50.03 | 01:50.87 | 0.83 | forever. | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 95 | 204 | [img](KEYFRAMES/V6/V6_shot077_0110.03s.jpg) |
| 78 | 01:50.87 | 01:53.10 | 2.23 | She laughed and cried at the same time. | slow_drift | ease_out (fast start, decelerating) | 3D | 98 | 160 | [img](KEYFRAMES/V6/V6_shot078_0110.87s.jpg) |
| 79 | 01:53.10 | 01:54.43 | 1.33 | Then, the sun went down, | static | n/a |  | 102 | 132 | [img](KEYFRAMES/V6/V6_shot079_0113.10s.jpg) |
| 80 | 01:54.43 | 01:55.57 | 1.13 | and Lily walked away | subject_motion_or_orbit | ease_in (accelerating) |  | 79 | 156 | [img](KEYFRAMES/V6/V6_shot080_0114.43s.jpg) |
| 81 | 01:55.57 | 01:57.57 | 2.00 | on her own. | slow_drift | ease_in_out | 3D | 77 | 146 | [img](KEYFRAMES/V6/V6_shot081_0115.57s.jpg) |
| 82 | 01:57.57 | 02:00.10 | 2.53 |  | static | n/a |  | 75 | 136 | [img](KEYFRAMES/V6/V6_shot082_0117.57s.jpg) |
| 83 | 02:00.10 | 02:04.10 | 4.00 | *(TikTok end card)* | slow_drift | linear/constant |  | 21 | 116 | [img](KEYFRAMES/V6/V6_shot083_0120.10s.jpg) |

### V7 — `47e73f86-v12025gd0000dc1k507og65j9la4m0a0.mp4` — 5016 frames, 103 shots

| # | In | Out | Dur (s) | Narration during shot | Camera (flow) | Easing | 3D/2D | Luma | Sat | Keyframe |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 00:00.00 | 00:01.07 | 1.07 | In my town, nobody is | push_in | ease_in (accelerating) | 3D | 89 | 125 | [img](KEYFRAMES/V7/V7_shot000_0000.00s.jpg) |
| 1 | 00:01.07 | 00:01.93 | 0.87 | allowed to sleep. | push_in | ease_in_out | 3D | 99 | 114 | [img](KEYFRAMES/V7/V7_shot001_0001.07s.jpg) |
| 2 | 00:01.93 | 00:03.43 | 1.50 | The mayor made it the law last year. | push_in | ease_in (accelerating) | 3D | 71 | 170 | [img](KEYFRAMES/V7/V7_shot002_0001.93s.jpg) |
| 3 | 00:03.43 | 00:04.87 | 1.43 | He says sleep is a waste of time. | slow_drift | ease_out (fast start, decelerating) | 3D | 29 | 165 | [img](KEYFRAMES/V7/V7_shot003_0003.43s.jpg) |
| 4 | 00:04.87 | 00:07.13 | 2.27 | He hasn't slept in 40 years, and he's proud of it. | push_in | ease_in (accelerating) | 3D | 77 | 100 | [img](KEYFRAMES/V7/V7_shot004_0004.87s.jpg) |
| 5 | 00:07.13 | 00:09.07 | 1.93 | So beds are against the law now. | slow_drift | ease_in (accelerating) | 3D | 49 | 164 | [img](KEYFRAMES/V7/V7_shot005_0007.13s.jpg) |
| 6 | 00:09.07 | 00:10.97 | 1.90 | The furniture store only sells chairs. | push_in | linear/constant | 3D | 134 | 168 | [img](KEYFRAMES/V7/V7_shot006_0009.07s.jpg) |
| 7 | 00:10.97 | 00:11.87 | 0.90 | At night, the police | subject_motion_or_orbit | ease_in (accelerating) |  | 71 | 160 | [img](KEYFRAMES/V7/V7_shot007_0010.97s.jpg) |
| 8 | 00:11.87 | 00:13.93 | 2.07 | shine flashlights into every window. | static | n/a |  | 169 | 115 | [img](KEYFRAMES/V7/V7_shot008_0011.87s.jpg) |
| 9 | 00:13.93 | 00:14.93 | 1.00 | If your eyes are closed, | push_in | ease_in (accelerating) | 3D | 102 | 112 | [img](KEYFRAMES/V7/V7_shot009_0013.93s.jpg) |
| 10 | 00:14.93 | 00:16.07 | 1.13 | you pay $100. | slow_drift | ease_out (fast start, decelerating) |  | 16 | 205 | [img](KEYFRAMES/V7/V7_shot010_0014.93s.jpg) |
| 11 | 00:16.07 | 00:17.37 | 1.30 | And every night at midnight, | push_in | ease_out (fast start, decelerating) |  | 64 | 150 | [img](KEYFRAMES/V7/V7_shot011_0016.07s.jpg) |
| 12 | 00:17.37 | 00:18.50 | 1.13 | the mayor goes live on | push_in | ease_in (accelerating) | 3D | 89 | 154 | [img](KEYFRAMES/V7/V7_shot012_0017.37s.jpg) |
| 13 | 00:18.50 | 00:19.17 | 0.67 | every TV and | slow_drift | ease_in (accelerating) |  | 148 | 122 | [img](KEYFRAMES/V7/V7_shot013_0018.50s.jpg) |
| 14 | 00:19.17 | 00:20.20 | 1.03 | phone in town. | push_in | ease_in (accelerating) | 3D | 132 | 144 | [img](KEYFRAMES/V7/V7_shot014_0019.17s.jpg) |
| 15 | 00:20.20 | 00:21.43 | 1.23 | It's called the wake check, | push_in | ease_in (accelerating) | 3D | 84 | 116 | [img](KEYFRAMES/V7/V7_shot015_0020.20s.jpg) |
| 16 | 00:21.43 | 00:22.67 | 1.23 | and you can't turn it off. | push_in | ease_in_out | 3D | 116 | 144 | [img](KEYFRAMES/V7/V7_shot016_0021.43s.jpg) |
| 17 | 00:22.67 | 00:23.57 | 0.90 | He picks one house and | slow_drift | ease_out (fast start, decelerating) | 2D | 61 | 182 | [img](KEYFRAMES/V7/V7_shot017_0022.67s.jpg) |
| 18 | 00:23.57 | 00:25.20 | 1.63 | video calls it live. | subject_motion_or_orbit | ease_in_out |  | 118 | 171 | [img](KEYFRAMES/V7/V7_shot018_0023.57s.jpg) |
| 19 | 00:25.20 | 00:27.17 | 1.97 | Houses with the lights off get picked first. | push_in | ease_in (accelerating) | 3D | 25 | 222 | [img](KEYFRAMES/V7/V7_shot019_0025.20s.jpg) |
| 20 | 00:27.17 | 00:28.57 | 1.40 | If you look sleepy, you pay. | push_in | ease_in_out | 3D | 102 | 128 | [img](KEYFRAMES/V7/V7_shot020_0027.17s.jpg) |
| 21 | 00:28.57 | 00:30.73 | 2.17 | So nobody turns their lights off anymore. | pan_or_track_right | ease_in_out |  | 36 | 200 | [img](KEYFRAMES/V7/V7_shot021_0028.57s.jpg) |
| 22 | 00:30.73 | 00:32.23 | 1.50 | Everyone is tired all the time. | subject_motion_or_orbit | ease_in (accelerating) |  | 111 | 99 | [img](KEYFRAMES/V7/V7_shot022_0030.73s.jpg) |
| 23 | 00:32.23 | 00:35.73 | 3.50 | My sister Ava is six, and she's the most tired of all. | slow_drift | ease_in_out | 3D | 154 | 102 | [img](KEYFRAMES/V7/V7_shot023_0032.23s.jpg) |
| 24 | 00:35.73 | 00:37.90 | 2.17 | Eli, I'm so tired. | static | n/a |  | 135 | 148 | [img](KEYFRAMES/V7/V7_shot024_0035.73s.jpg) |
| 25 | 00:37.90 | 00:41.37 | 3.47 | She cries every night. I promised Ava I'd find a way to help her sleep. | slow_drift | ease_out (fast start, decelerating) | 3D | 167 | 100 | [img](KEYFRAMES/V7/V7_shot025_0037.90s.jpg) |
| 26 | 00:41.37 | 00:42.10 | 0.73 | On my bus, | push_in | ease_in (accelerating) |  | 98 | 129 | [img](KEYFRAMES/V7/V7_shot026_0041.37s.jpg) |
| 27 | 00:42.10 | 00:44.30 | 2.20 | a kid in the very back eats a burger every morning, | push_in | ease_out (fast start, decelerating) | 3D | 108 | 82 | [img](KEYFRAMES/V7/V7_shot027_0042.10s.jpg) |
| 28 | 00:44.30 | 00:44.50 | 0.20 | and | too_short |  |  | 174 | 11 | [img](KEYFRAMES/V7/V7_shot028_0044.30s.jpg) |
| 29 | 00:44.50 | 00:45.33 | 0.83 | I know this kid. | slow_drift | ease_in (accelerating) | 3D | 71 | 34 | [img](KEYFRAMES/V7/V7_shot029_0044.50s.jpg) |
| 30 | 00:45.33 | 00:45.53 | 0.20 | He | too_short |  |  | 169 | 24 | [img](KEYFRAMES/V7/V7_shot030_0045.33s.jpg) |
| 31 | 00:45.53 | 00:47.07 | 1.53 | helped me get my very first burger. | slow_drift | ease_in (accelerating) | 3D | 62 | 170 | [img](KEYFRAMES/V7/V7_shot031_0045.53s.jpg) |
| 32 | 00:47.07 | 00:48.20 | 1.13 | But when I said hi, | push_in | ease_out (fast start, decelerating) | 3D | 102 | 146 | [img](KEYFRAMES/V7/V7_shot032_0047.07s.jpg) |
| 33 | 00:48.20 | 00:50.53 | 2.33 | he just stared at me like he'd never seen me before. | push_in | ease_in (accelerating) | 3D | 83 | 94 | [img](KEYFRAMES/V7/V7_shot033_0048.20s.jpg) |
| 34 | 00:50.53 | 00:51.80 | 1.27 | Nobody has ever heard him talk. | slow_drift | ease_in_out | 3D | 86 | 116 | [img](KEYFRAMES/V7/V7_shot034_0050.53s.jpg) |
| 35 | 00:51.80 | 00:53.27 | 1.47 | Nobody even knows his name. | slow_drift | ease_out (fast start, decelerating) | 3D | 81 | 90 | [img](KEYFRAMES/V7/V7_shot035_0051.80s.jpg) |
| 36 | 00:53.27 | 00:55.27 | 2.00 | So everyone calls him Random Kid. | slow_drift | ease_in_out | 3D | 105 | 107 | [img](KEYFRAMES/V7/V7_shot036_0053.27s.jpg) |
| 37 | 00:55.27 | 00:56.67 | 1.40 | Hey, Random Kid, say something. Everyone | push_in | linear/constant | 3D | 116 | 72 | [img](KEYFRAMES/V7/V7_shot037_0055.27s.jpg) |
| 38 | 00:56.67 | 00:57.63 | 0.97 | laughs. He | push_in | linear/constant | 3D | 104 | 117 | [img](KEYFRAMES/V7/V7_shot038_0056.67s.jpg) |
| 39 | 00:57.63 | 00:58.63 | 1.00 | just keeps chewing. | push_in | linear/constant | 3D | 68 | 101 | [img](KEYFRAMES/V7/V7_shot039_0057.63s.jpg) |
| 40 | 00:58.63 | 00:59.40 | 0.77 | Then one morning, | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 81 | 94 | [img](KEYFRAMES/V7/V7_shot040_0058.63s.jpg) |
| 41 | 00:59.40 | 01:01.53 | 2.13 | he took a big bite and hummed. Hmm, hmm. | push_in | ease_in (accelerating) |  | 48 | 152 | [img](KEYFRAMES/V7/V7_shot041_0059.40s.jpg) |
| 42 | 01:01.53 | 01:03.43 | 1.90 | And every kid on the bus fell asleep, | push_in | ease_in_out | 3D | 95 | 95 | [img](KEYFRAMES/V7/V7_shot042_0061.53s.jpg) |
| 43 | 01:03.43 | 01:04.27 | 0.83 | including me. | push_in | ease_in_out | 3D | 93 | 159 | [img](KEYFRAMES/V7/V7_shot043_0063.43s.jpg) |
| 44 | 01:04.27 | 01:04.83 | 0.57 | I woke up six | push_in | linear/constant |  | 100 | 152 | [img](KEYFRAMES/V7/V7_shot044_0064.27s.jpg) |
| 45 | 01:04.83 | 01:06.43 | 1.60 | hours later in the bus garage. | push_in | ease_in_out | 3D | 74 | 147 | [img](KEYFRAMES/V7/V7_shot045_0064.83s.jpg) |
| 46 | 01:06.43 | 01:07.50 | 1.07 | We'd all slept through school. | push_in | ease_out (fast start, decelerating) | 3D | 104 | 88 | [img](KEYFRAMES/V7/V7_shot046_0066.43s.jpg) |
| 47 | 01:07.50 | 01:09.17 | 1.67 | The driver had headphones on, and he was too | push_in | ease_in_out | 3D | 27 | 115 | [img](KEYFRAMES/V7/V7_shot047_0067.50s.jpg) |
| 48 | 01:09.17 | 01:10.33 | 1.17 | tired to notice us. | push_in | linear/constant | 3D | 93 | 79 | [img](KEYFRAMES/V7/V7_shot048_0069.17s.jpg) |
| 49 | 01:10.33 | 01:12.37 | 2.03 | Random Kid was still awake finishing his burger, | subject_motion_or_orbit | ease_in_out |  | 89 | 73 | [img](KEYFRAMES/V7/V7_shot049_0070.33s.jpg) |
| 50 | 01:12.37 | 01:15.63 | 3.27 | and I felt better than I had all year. That's why he never talks. | subject_motion_or_orbit | ease_in_out |  | 97 | 154 | [img](KEYFRAMES/V7/V7_shot050_0072.37s.jpg) |
| 51 | 01:15.63 | 01:17.03 | 1.40 | His voice puts people to sleep. | push_in | linear/constant |  | 55 | 163 | [img](KEYFRAMES/V7/V7_shot051_0075.63s.jpg) |
| 52 | 01:17.03 | 01:18.27 | 1.23 | That gave me an idea. | push_in | ease_in (accelerating) | 3D | 110 | 149 | [img](KEYFRAMES/V7/V7_shot052_0077.03s.jpg) |
| 53 | 01:18.27 | 01:19.80 | 1.53 | The wake check is the one time every night | push_in | linear/constant | 3D | 135 | 91 | [img](KEYFRAMES/V7/V7_shot053_0078.27s.jpg) |
| 54 | 01:19.80 | 01:21.93 | 2.13 | when the whole town hears the same thing. | push_in | ease_in (accelerating) | 3D | 82 | 79 | [img](KEYFRAMES/V7/V7_shot054_0079.80s.jpg) |
| 55 | 01:21.93 | 01:24.00 | 2.07 | And houses with the lights off get picked first. | push_in | ease_in (accelerating) | 3D | 63 | 130 | [img](KEYFRAMES/V7/V7_shot055_0081.93s.jpg) |
| 56 | 01:24.00 | 01:26.30 | 2.30 | So if Random Kid's house was the only dark one, the | slow_drift | ease_out (fast start, decelerating) | 3D | 85 | 146 | [img](KEYFRAMES/V7/V7_shot056_0084.00s.jpg) |
| 57 | 01:26.30 | 01:27.17 | 0.87 | mayor would call him, | push_in | linear/constant | 3D | 92 | 137 | [img](KEYFRAMES/V7/V7_shot057_0086.30s.jpg) |
| 58 | 01:27.17 | 01:30.77 | 3.60 | and the whole town would hear his voice. Everyone would fall asleep at once, | slow_drift | ease_in_out | 3D | 174 | 74 | [img](KEYFRAMES/V7/V7_shot058_0087.17s.jpg) |
| 59 | 01:30.77 | 01:31.60 | 0.83 | even the police. | push_in | linear/constant | 3D | 70 | 82 | [img](KEYFRAMES/V7/V7_shot059_0090.77s.jpg) |
| 60 | 01:31.60 | 01:32.80 | 1.20 | Nobody would have to pay. | slow_drift | ease_out (fast start, decelerating) | 3D | 45 | 196 | [img](KEYFRAMES/V7/V7_shot060_0091.60s.jpg) |
| 61 | 01:32.80 | 01:35.10 | 2.30 | I just hoped his voice would work through a TV. | static | n/a |  | 150 | 118 | [img](KEYFRAMES/V7/V7_shot061_0092.80s.jpg) |
| 62 | 01:35.10 | 01:37.07 | 1.97 | That afternoon, I followed Random Kid home | push_in | ease_out (fast start, decelerating) | 3D | 132 | 120 | [img](KEYFRAMES/V7/V7_shot062_0095.10s.jpg) |
| 63 | 01:37.07 | 01:38.43 | 1.37 | and explained my plan. | push_in | ease_out (fast start, decelerating) | 3D | 56 | 183 | [img](KEYFRAMES/V7/V7_shot063_0097.07s.jpg) |
| 64 | 01:38.43 | 01:39.80 | 1.37 | I told him about Ava, too. | pull_out | ease_out (fast start, decelerating) | 3D | 164 | 133 | [img](KEYFRAMES/V7/V7_shot064_0098.43s.jpg) |
| 65 | 01:39.80 | 01:41.50 | 1.70 | He didn't say anything, but he nodded. | slow_drift | ease_in (accelerating) | 3D | 33 | 146 | [img](KEYFRAMES/V7/V7_shot065_0099.80s.jpg) |
| 66 | 01:41.50 | 01:43.57 | 2.07 | That night at midnight, every light in town was on, | slow_drift | linear/constant | 3D | 33 | 179 | [img](KEYFRAMES/V7/V7_shot066_0101.50s.jpg) |
| 67 | 01:43.57 | 01:44.40 | 0.83 | except his. | push_in | ease_in (accelerating) | 3D | 30 | 191 | [img](KEYFRAMES/V7/V7_shot067_0103.57s.jpg) |
| 68 | 01:44.40 | 01:45.63 | 1.23 | Ooh, lights off. | pull_out | ease_in (accelerating) | 3D | 53 | 93 | [img](KEYFRAMES/V7/V7_shot068_0104.40s.jpg) |
| 69 | 01:45.63 | 01:47.03 | 1.40 | Let's see who's sleeping tonight. The | pull_out | ease_in_out | 3D | 96 | 131 | [img](KEYFRAMES/V7/V7_shot069_0105.63s.jpg) |
| 70 | 01:47.03 | 01:48.67 | 1.63 | mayor called Random Kid live with | slow_drift | ease_in (accelerating) | 3D | 24 | 144 | [img](KEYFRAMES/V7/V7_shot070_0107.03s.jpg) |
| 71 | 01:48.67 | 01:50.33 | 1.67 | the whole town watching. | static | n/a |  | 169 | 105 | [img](KEYFRAMES/V7/V7_shot071_0108.67s.jpg) |
| 72 | 01:50.33 | 01:52.07 | 1.73 | Are you sleeping? Say something. | push_in | ease_in (accelerating) | 3D | 88 | 42 | [img](KEYFRAMES/V7/V7_shot072_0110.33s.jpg) |
| 73 | 01:52.07 | 01:54.77 | 2.70 | And Random Kid, the kid who never talks, opened his mouth. | static | n/a |  | 9 | 129 | [img](KEYFRAMES/V7/V7_shot073_0112.07s.jpg) |
| 74 | 01:54.77 | 01:55.17 | 0.40 |  | subject_motion_or_orbit | n/a |  | 23 | 147 | [img](KEYFRAMES/V7/V7_shot074_0114.77s.jpg) |
| 75 | 01:55.17 | 02:01.23 | 6.07 | Don't stay away from Tuna. Don't go to bed. | slow_drift | linear/constant | 3D | 44 | 145 | [img](KEYFRAMES/V7/V7_shot075_0115.17s.jpg) |
| 76 | 02:01.23 | 02:02.53 | 1.30 | I'll make you cup and coffee | push_in | ease_in (accelerating) | 3D | 89 | 132 | [img](KEYFRAMES/V7/V7_shot076_0121.23s.jpg) |
| 77 | 02:02.53 | 02:04.60 | 2.07 | for your head. | push_in | ease_in_out | 3D | 45 | 144 | [img](KEYFRAMES/V7/V7_shot077_0122.53s.jpg) |
| 78 | 02:04.60 | 02:06.33 | 1.73 | The mayor fell asleep on live TV. | push_in | ease_in (accelerating) | 3D | 91 | 148 | [img](KEYFRAMES/V7/V7_shot078_0124.60s.jpg) |
| 79 | 02:06.33 | 02:08.00 | 1.67 | The police fell asleep in their cars. | static | n/a |  | 61 | 75 | [img](KEYFRAMES/V7/V7_shot079_0126.33s.jpg) |
| 80 | 02:08.00 | 02:09.97 | 1.97 | Ava fell asleep before he even finished. | push_in | ease_in (accelerating) | 3D | 158 | 96 | [img](KEYFRAMES/V7/V7_shot080_0128.00s.jpg) |
| 81 | 02:09.97 | 02:12.03 | 2.07 | I had earplugs in, so I stayed awake and | slow_drift | linear/constant | 3D | 157 | 141 | [img](KEYFRAMES/V7/V7_shot081_0129.97s.jpg) |
| 82 | 02:12.03 | 02:13.00 | 0.97 | saw it all. | push_in | linear/constant | 3D | 43 | 153 | [img](KEYFRAMES/V7/V7_shot082_0132.03s.jpg) |
| 83 | 02:13.00 | 02:15.63 | 2.63 | Then I took one out, just to hear his voice. Bad idea. | slow_drift | ease_in (accelerating) | 3D | 165 | 132 | [img](KEYFRAMES/V7/V7_shot083_0133.00s.jpg) |
| 84 | 02:15.63 | 02:17.17 | 1.53 | I was asleep in two seconds. | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 139 | 168 | [img](KEYFRAMES/V7/V7_shot084_0135.63s.jpg) |
| 85 | 02:17.17 | 02:17.73 | 0.57 | The next morning, | push_in | linear/constant |  | 70 | 120 | [img](KEYFRAMES/V7/V7_shot085_0137.17s.jpg) |
| 86 | 02:17.73 | 02:19.77 | 2.03 | the whole town woke up at the same time. | slow_drift | ease_in_out | 3D | 84 | 94 | [img](KEYFRAMES/V7/V7_shot086_0137.73s.jpg) |
| 87 | 02:19.77 | 02:21.57 | 1.80 | Nobody had felt that good in a year, | subject_motion_or_orbit | ease_in (accelerating) |  | 129 | 141 | [img](KEYFRAMES/V7/V7_shot087_0139.77s.jpg) |
| 88 | 02:21.57 | 02:22.47 | 0.90 | especially the mayor. | push_in | ease_in_out | 3D | 91 | 148 | [img](KEYFRAMES/V7/V7_shot088_0141.57s.jpg) |
| 89 | 02:22.47 | 02:24.43 | 1.97 | That was his first sleep in 40 years. Why | slow_drift | ease_in_out | 3D | 88 | 93 | [img](KEYFRAMES/V7/V7_shot089_0142.47s.jpg) |
| 90 | 02:24.43 | 02:27.33 | 2.90 | didn't anybody remind me how good sleep feels? | push_in | ease_in (accelerating) | 3D | 72 | 154 | [img](KEYFRAMES/V7/V7_shot090_0144.43s.jpg) |
| 91 | 02:27.33 | 02:28.33 | 1.00 | That same day, he made | subject_motion_or_orbit | ease_in (accelerating) |  | 77 | 109 | [img](KEYFRAMES/V7/V7_shot091_0147.33s.jpg) |
| 92 | 02:28.33 | 02:29.57 | 1.23 | sleeping OK again. | pull_out | ease_out (fast start, decelerating) | 3D | 85 | 123 | [img](KEYFRAMES/V7/V7_shot092_0148.33s.jpg) |
| 93 | 02:29.57 | 02:31.27 | 1.70 | Now the wake check is the sleep check. | push_in | ease_in_out | 3D | 42 | 207 | [img](KEYFRAMES/V7/V7_shot093_0149.57s.jpg) |
| 94 | 02:31.27 | 02:33.50 | 2.23 | Every night at nine, the mayor calls Random Kid, | slow_drift | ease_in_out | 3D | 95 | 128 | [img](KEYFRAMES/V7/V7_shot094_0151.27s.jpg) |
| 95 | 02:33.50 | 02:35.40 | 1.90 | and the whole town falls asleep together. | slow_drift | ease_out (fast start, decelerating) | 3D | 32 | 180 | [img](KEYFRAMES/V7/V7_shot095_0153.50s.jpg) |
| 96 | 02:35.40 | 02:37.07 | 1.67 | Ava sleeps 12 hours a night now, but | push_in | ease_in_out | 3D | 95 | 174 | [img](KEYFRAMES/V7/V7_shot096_0155.40s.jpg) |
| 97 | 02:37.07 | 02:38.77 | 1.70 | I still don't know Random Kid's name. | push_in | linear/constant | 3D | 82 | 107 | [img](KEYFRAMES/V7/V7_shot097_0157.07s.jpg) |
| 98 | 02:38.77 | 02:39.80 | 1.03 | I asked him once. | subject_motion_or_orbit | ease_out (fast start, decelerating) |  | 93 | 163 | [img](KEYFRAMES/V7/V7_shot098_0158.77s.jpg) |
| 99 | 02:39.80 | 02:40.43 | 0.63 | He opened his mouth | push_in | linear/constant |  | 44 | 131 | [img](KEYFRAMES/V7/V7_shot099_0159.80s.jpg) |
| 100 | 02:40.43 | 02:41.13 | 0.70 | to answer, | push_in | ease_out (fast start, decelerating) |  | 45 | 122 | [img](KEYFRAMES/V7/V7_shot100_0160.43s.jpg) |
| 101 | 02:41.13 | 02:43.20 | 2.07 | and I woke up in the bus garage. | slow_drift | ease_out (fast start, decelerating) | 3D | 101 | 154 | [img](KEYFRAMES/V7/V7_shot101_0161.13s.jpg) |
| 102 | 02:43.20 | 02:47.20 | 4.00 | *(TikTok end card)* | slow_drift | linear/constant |  | 21 | 116 | [img](KEYFRAMES/V7/V7_shot102_0163.20s.jpg) |
