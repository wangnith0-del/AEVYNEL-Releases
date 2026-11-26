// =====================================================================================
// character.js — RECONSTRUCTED (not original source) R6-style blocky character.
//
// Reproduces the character construction observed in all 7 videos:
//   6 rigid parts (head, torso, 2 arms, 2 legs) -> "R6" topology, no skinning needed.
//   Faces are a 2D texture on the front of the head, swapped per expression (observed in V7:
//   mouth goes from "line" to "open triangle" between two consecutive frames, no in-between).
//
// Hierarchy (pivots placed at the joints so rotations look anatomical):
//   root (feet on y=0)
//    └─ hips (pelvis height)          <- vertical bob / sway applied here
//        ├─ torso
//        │   ├─ neck pivot ─ head ─ face plane, hair
//        │   ├─ L shoulder pivot ─ L arm
//        │   └─ R shoulder pivot ─ R arm
//        ├─ L hip pivot ─ L leg
//        └─ R hip pivot ─ R leg
// Units: 1 unit = 1 Roblox stud * 0.25 (an R6 avatar is ~5 studs tall -> ~1.25 units... we
// use a 2-unit-tall character so camera numbers stay readable).
// =====================================================================================
import * as THREE from 'three';

const S = 0.4; // stud scale: R6 torso is 2x2x1 studs -> 0.8 x 0.8 x 0.4 units

/** Draw one expression into a 2D canvas. Expressions mirror those observed in the videos. */
export function drawFace(ctx, expr = 'neutral', { blink = 0, skin = '#f5c542' } = {}) {
  const W = ctx.canvas.width, H = ctx.canvas.height;
  ctx.clearRect(0, 0, W, H); // transparent: the head colour shows through
  ctx.fillStyle = '#111'; ctx.strokeStyle = '#111'; ctx.lineCap = 'round';
  const eyeY = H * 0.42, eyeDX = W * 0.17;
  const eyeOpen = 1 - blink;                         // blink 0..1 squashes the eyes vertically
  const eye = (x, h = 0.09) => {
    ctx.beginPath(); ctx.ellipse(x, eyeY, W * 0.045, Math.max(1, H * h * eyeOpen * 0.5), 0, 0, Math.PI * 2); ctx.fill();
  };
  ctx.lineWidth = W * 0.035;
  switch (expr) {
    case 'smile':
      eye(W / 2 - eyeDX); eye(W / 2 + eyeDX);
      ctx.beginPath(); ctx.arc(W / 2, H * 0.55, W * 0.18, 0.15 * Math.PI, 0.85 * Math.PI); ctx.stroke(); break;
    case 'shock': // round eyes with white highlight + small "o" mouth + sweat drop (V3 "screamed")
      for (const x of [W / 2 - eyeDX, W / 2 + eyeDX]) {
        ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(x, eyeY, W * 0.08, 0, 7); ctx.fill();
        ctx.lineWidth = W * 0.02; ctx.stroke(); ctx.fillStyle = '#111';
        ctx.beginPath(); ctx.arc(x, eyeY, W * 0.035, 0, 7); ctx.fill();
      }
      ctx.beginPath(); ctx.ellipse(W / 2, H * 0.66, W * 0.04, H * 0.05, 0, 0, 7); ctx.fill();
      ctx.fillStyle = '#5ab4ff'; ctx.beginPath(); ctx.ellipse(W * 0.8, H * 0.3, W * 0.03, H * 0.05, 0, 0, 7); ctx.fill(); break;
    case 'sad': // tears = separate blue strokes (V6 "memorize", V7 "about")
      eye(W / 2 - eyeDX); eye(W / 2 + eyeDX);
      ctx.lineWidth = W * 0.025;
      ctx.beginPath(); ctx.moveTo(W * 0.25, H * 0.3); ctx.lineTo(W * 0.4, H * 0.27); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(W * 0.75, H * 0.3); ctx.lineTo(W * 0.6, H * 0.27); ctx.stroke();
      ctx.beginPath(); ctx.arc(W / 2, H * 0.72, W * 0.12, 1.15 * Math.PI, 1.85 * Math.PI); ctx.stroke();
      ctx.strokeStyle = '#4aa8ff'; ctx.lineWidth = W * 0.03;
      ctx.beginPath(); ctx.moveTo(W / 2 - eyeDX, eyeY + H * 0.06); ctx.lineTo(W / 2 - eyeDX, H * 0.62); ctx.stroke(); break;
    case 'yell': // squint ">" "<" + open mouth (V4 "Wake up!")
      ctx.lineWidth = W * 0.03;
      ctx.beginPath(); ctx.moveTo(W * 0.27, eyeY - 8); ctx.lineTo(W * 0.37, eyeY); ctx.lineTo(W * 0.27, eyeY + 8); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(W * 0.73, eyeY - 8); ctx.lineTo(W * 0.63, eyeY); ctx.lineTo(W * 0.73, eyeY + 8); ctx.stroke();
      ctx.beginPath(); ctx.ellipse(W / 2, H * 0.66, W * 0.12, H * 0.1, 0, 0, 7); ctx.fill();
      ctx.fillStyle = '#e33'; ctx.beginPath(); ctx.ellipse(W / 2, H * 0.71, W * 0.07, H * 0.04, 0, 0, 7); ctx.fill(); break;
    case 'sleep':
      ctx.beginPath(); ctx.arc(W / 2 - eyeDX, eyeY, W * 0.06, 0.1, Math.PI - 0.1); ctx.stroke();
      ctx.beginPath(); ctx.arc(W / 2 + eyeDX, eyeY, W * 0.06, 0.1, Math.PI - 0.1); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(W * 0.44, H * 0.66); ctx.lineTo(W * 0.56, H * 0.66); ctx.stroke(); break;
    default: // neutral "classic" face
      eye(W / 2 - eyeDX); eye(W / 2 + eyeDX);
      ctx.beginPath(); ctx.arc(W / 2, H * 0.52, W * 0.16, 0.25 * Math.PI, 0.75 * Math.PI); ctx.stroke();
  }
}

function box(w, h, d, color, { map = null } = {}) {
  const m = new THREE.Mesh(
    new THREE.BoxGeometry(w, h, d),
    new THREE.MeshStandardMaterial({ color, roughness: 0.75, metalness: 0.0, map })
  );
  m.castShadow = true; m.receiveShadow = true;
  return m;
}

/** Shirt texture with a simple print, like Roblox "classic shirts" (low-res -> NearestFilter look). */
function shirtTexture(base, accent, label) {
  const c = document.createElement('canvas'); c.width = c.height = 64;
  const g = c.getContext('2d');
  g.fillStyle = base; g.fillRect(0, 0, 64, 64);
  g.fillStyle = accent; g.fillRect(0, 50, 64, 14); g.fillRect(20, 0, 24, 8);
  if (label) { g.fillStyle = '#fff'; g.font = 'bold 14px sans-serif'; g.fillText(label, 20, 34); }
  const t = new THREE.CanvasTexture(c); t.magFilter = THREE.NearestFilter; t.colorSpace = THREE.SRGBColorSpace;
  return t;
}

/**
 * Build a character. Returns { root, joints, setExpression, update }.
 * joints exposes the pivots the animation system drives.
 */
export function buildCharacter({
  skin = '#f5c542', shirt = '#e8562a', shirtAccent = '#f5c542', pants = '#2a3f7a',
  hair = '#2b1a10', label = 'PH', name = 'char'
} = {}) {
  const root = new THREE.Group(); root.name = name;
  const hips = new THREE.Group(); hips.position.y = 2 * S; root.add(hips);       // legs are 2 studs
  const torso = box(2 * S, 2 * S, 1 * S, '#ffffff', { map: shirtTexture(shirt, shirtAccent, label) });
  torso.position.y = 1 * S; hips.add(torso);

  // --- head + face (face is a transparent plane slightly in front of the head) ---
  const neck = new THREE.Group(); neck.position.y = 1 * S; torso.add(neck);
  const head = box(1.2 * S, 1.2 * S, 1.2 * S, skin); head.position.y = 0.6 * S; neck.add(head);
  const faceCanvas = document.createElement('canvas'); faceCanvas.width = faceCanvas.height = 256;
  const faceTex = new THREE.CanvasTexture(faceCanvas); faceTex.colorSpace = THREE.SRGBColorSpace;
  const face = new THREE.Mesh(new THREE.PlaneGeometry(1.2 * S, 1.2 * S),
    new THREE.MeshStandardMaterial({ map: faceTex, transparent: true, roughness: 0.8, polygonOffset: true, polygonOffsetFactor: -1 }));
  face.position.z = 0.6 * S + 0.001; head.add(face);
  // hair: a slightly larger flattened box + a few lumps (mesh accessory stand-in)
  const hairCap = box(1.3 * S, 0.5 * S, 1.3 * S, hair); hairCap.position.set(0, 0.45 * S, -0.03 * S); head.add(hairCap);
  for (let i = 0; i < 5; i++) {
    const lump = new THREE.Mesh(new THREE.SphereGeometry(0.22 * S, 12, 8), hairCap.material);
    lump.position.set((i - 2) * 0.27 * S, 0.62 * S, 0.1 * S - Math.abs(i - 2) * 0.12 * S); lump.castShadow = true; head.add(lump);
  }

  // --- limbs: pivot at the joint, mesh offset downward so rotation happens at shoulder/hip ---
  const limb = (x, y, color, parent) => {
    const pivot = new THREE.Group(); pivot.position.set(x, y, 0); parent.add(pivot);
    const m = box(1 * S, 2 * S, 1 * S, color); m.position.y = -1 * S + 0.0; pivot.add(m);
    return pivot;
  };
  const lShoulder = limb(-1.5 * S, 1.9 * S, shirt, hips); lShoulder.children[0].position.y = -0.9 * S;
  const rShoulder = limb(1.5 * S, 1.9 * S, shirt, hips); rShoulder.children[0].position.y = -0.9 * S;
  // hands keep skin colour on the lower part (classic look): add a skin cube at the end
  for (const sh of [lShoulder, rShoulder]) { const hand = box(1.01 * S, 0.5 * S, 1.01 * S, skin); hand.position.y = -1.65 * S; sh.add(hand); }
  const lHip = limb(-0.5 * S, 0, pants, hips);
  const rHip = limb(0.5 * S, 0, pants, hips);

  let expression = 'neutral', blink = 0;
  const redraw = () => { drawFace(faceCanvas.getContext('2d'), expression, { blink, skin }); faceTex.needsUpdate = true; };
  redraw();
  return {
    root,
    joints: { hips, torso, neck, head, lShoulder, rShoulder, lHip, rHip },
    /** Instant swap — matches the decal swap behaviour measured frame-by-frame in V7. */
    setExpression(e) { if (e !== expression) { expression = e; redraw(); } },
    setBlink(b) { b = Math.round(b * 4) / 4; if (b !== blink) { blink = b; redraw(); } },
    get expression() { return expression; },
  };
}
