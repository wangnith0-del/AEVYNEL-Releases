# 12 — Pipeline de production reconstruit

Reconstitution de l'idée à l'export. Les outils nommés sont ceux **compatibles avec les traces** ; quand plusieurs conviennent, ils sont listés. Statut par étape.

| # | Étape | Entrées → Sorties | Outils plausibles | Automatisable ? | Statut |
|---|---|---|---|---|---|
| 1 | Écriture du scénario | concept « In this town » → script 380–630 mots | humain, éventuellement LLM | oui (gabarit `11 §5`) | formule **[CONFIRMÉ]** ; outil **[INDÉTERMINABLE]** |
| 2 | Découpage technique | script → liste de propositions (1 proposition ≈ 1 plan) | tableur | oui (`shot_planner.py`) | **[FORTEMENT PROBABLE]** |
| 3 | Storyboard | propositions → plans (taille, angle, mouvement) | croquis / directement dans le moteur | partiel | **[HYPOTHÈSE]** |
| 4 | Personnages | fiches → avatars R6 + jeux de visages | Roblox avatar/catalogue ; Blender ; textures 2D | oui (factory) | **[CONFIRMÉ : R6]** |
| 5 | Environnements | → places/scènes (kits + lieux héros) | Roblox Studio, cartes RP existantes (V4, V7) ; Blender | partiel | **[FORTEMENT PROBABLE]** |
| 6 | Assets | → modèles, décalques, particules | Studio Toolbox / Creator Store, UGC, Blender | — | **[FORTEMENT PROBABLE]** |
| 7 | Construction des scènes | → scènes par lieu | moteur | — | — |
| 8 | Rigging | R6 natif (Motor6D) / parenting Blender | aucun rigging complexe | oui | **[CONFIRMÉ : rigide]** |
| 9 | Animation | clés + cycles | Roblox : Moon Animator / Animation Editor + Humanoid ; Blender : clés | partiel | **[FORTEMENT PROBABLE]** |
| 10 | Caméras | CFrame/caméra animée par plan | Moon Animator (Roblox) ; caméra Blender | oui (`CameraDirector`) | 3D **[CONFIRMÉ]**, outil **[HYPOTHÈSE]** |
| 11 | Éclairage | presets par ambiance | Lighting Roblox ; Blender World/Sun | oui | **[FORTEMENT PROBABLE]** |
| 12 | VFX | particules, flashs, masques | ParticleEmitter ; Blender ; éditeur | partiel | **[CONFIRMÉ : présence]** |
| 13 | Voix | script → voix off rapide (172–234 mots/min) | voix humaine ou TTS IA | oui | **[INDÉTERMINABLE]** (aucune preuve concluante) |
| 14 | Synchro A/V | voix → mots horodatés → coupes/textes/visages | Whisper / auto-captions de l'éditeur | oui | coupes sur mots **[CONFIRMÉ V1/V5/V7]** |
| 15 | Rendu | A : capture écran (OBS) ; B : rendu d'images | OBS ; Blender Eevee/Cycles | oui | **[FORTEMENT PROBABLE]** |
| 16 | Post-traitement | grade, vignette, filtres | éditeur (filtres) ; moteur (post) | oui | **[CONFIRMÉ : présence]** |
| 17 | Montage | rushes + voix → timeline 9:16 | CapCut (indices : sous-titres pop templatés, stickers) / Premiere / DaVinci | partiel | **[FORTEMENT PROBABLE : éditeur avec auto-captions]** |
| 18 | Encodage final | → MP4 1080×1920 30 fps H.264/AAC | export éditeur | oui | résolution de prod. **[HYPOTHÈSE]** ; 30 fps **[CONFIRMÉ]** |
| 19 | Publication / QC | → TikTok ; réencodage 576×1024 pour le téléchargement + carte de fin | plateforme | — | **[CONFIRMÉ]** |

## Pipeline automatisé recommandé (dépendances et sorties)

```
episode/
  script.txt ─┐
              ├─(1) tts_or_record → vo.wav
              ├─(2) whisper → words.json                       [faster-whisper, testé]
              ├─(3) shot_planner.py → shots.json               [testé]
              ├─(4) characters.json + world preset
              ├─(5) render (Three.js render.mjs | Blender r6_story_scene.py | Roblox + OBS) → frames/ → silent.mp4   [Three.js & Blender testés]
              ├─(6) captions_ass.py → captions.ass             [testé]
              └─(7) mix_and_master.sh silent.mp4 vo.wav music.wav captions.ass → final.mp4   [testé, −14,0 LUFS]
```

Contrôle qualité automatique proposé (réutilise `tools/`) :
* `analyze_video.py` + `camera_motion.py` sur le rendu → vérifier durée médiane de plan (cible 1,3–2,5 s), part de plans non statiques (> 75 %).
* `audio_analysis.py` → coupes à < 100 ms d'un mot (cible > 75 %).
* `ffmpeg -af ebur128` → −14 ± 1 LUFS.
* `caption_ocr.py` → sous-titres alignés (|décalage| < 100 ms).
