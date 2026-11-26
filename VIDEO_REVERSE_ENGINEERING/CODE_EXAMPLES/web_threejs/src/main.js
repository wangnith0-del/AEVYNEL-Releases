// =====================================================================================
// main.js — deterministic timeline. One "episode" = shot list + character actions + face events,
// all driven by absolute time t = frame / FPS (no requestAnimationFrame, no delta-time drift).
// window.renderFrame(i) is called by render.mjs (Playwright) to export frame i.
// The demo storyboard reproduces the grammar measured in the 7 videos:
//   S1 wide establishing + slow push-in (character walks toward camera)
//   S2 medium: stop -> anticipation -> "alarm" gesture, face swaps to shock, fast push-in ease-out
//   S3 close-up: blink, swap to smile, slow drift (static-ish shot with breathing camera)
// =====================================================================================
import * as THREE from 'three';
import { buildCharacter } from './character.js';
import { locomotion, idle, blinkAt, gestureAlarm, clamp, Ease } from './animation.js';
import { CameraDirector } from './camera.js';
import { buildWorld } from './world.js';
import { buildPost } from './post.js';

const params = new URLSearchParams(location.search);
const W = +(params.get('w') || 576), H = +(params.get('h') || 1024), FPS = 30;

const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1); renderer.setSize(W, H);
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();
buildWorld(scene, { preset: params.get('preset') || 'day' });
const camera = new THREE.PerspectiveCamera(45, W / H, 0.1, 300);

const hero = buildCharacter({ name: 'hero' });
const sister = buildCharacter({ name: 'sister', shirt: '#e0457b', shirtAccent: '#ffd0e0', pants: '#3a2f55', hair: '#5a2d16', label: '★' });
sister.root.scale.setScalar(0.85);
scene.add(hero.root, sister.root);

// ---- action script (what each character does, in absolute time) ----
const WALK_SPEED = 1.4, STRIDE = 1.1;                 // units/s, units per cycle
const STOP_T = 2.2, ALARM_T = 2.45;
function heroPose(t) {
  const j = hero.joints;
  // reset additive channels each frame (pure function of t)
  for (const k of ['lShoulder', 'rShoulder', 'lHip', 'rHip', 'torso', 'neck', 'hips']) j[k].rotation.set(0, 0, 0);
  j.hips.position.y = 0.8; j.torso.scale.set(1, 1, 1);
  // position: walk toward camera (+z), decelerate into the stop (slow-in) so feet don't slide
  const walkT = Math.min(t, STOP_T);
  const decel = 0.4;                                   // last 0.4 s decelerate
  const dist = walkT < STOP_T - decel ? walkT * WALK_SPEED
    : (STOP_T - decel) * WALK_SPEED + WALK_SPEED * decel * Ease.outCubic((walkT - (STOP_T - decel)) / decel) * 0.5;
  hero.root.position.set(-0.6, 0, -6 + dist);
  const weight = t < STOP_T - decel ? 1 : clamp(1 - (t - (STOP_T - decel)) / decel);
  if (weight > 0) locomotion(j, (dist / STRIDE) * Math.PI * 2, { gait: 'walk', weight });
  idle(j, t, 1 - weight);
  if (!gestureAlarm(j, t, ALARM_T)) { /* no gesture yet */ }
  // faces: instant swaps keyed to story beats; blinks layered on top
  hero.setExpression(t < ALARM_T ? 'neutral' : t < 4.6 ? 'shock' : 'smile');
  hero.setBlink(hero.expression === 'shock' ? 0 : blinkAt(t, 3));
}
function sisterPose(t) {
  const j = sister.joints;
  for (const k of ['lShoulder', 'rShoulder', 'lHip', 'rHip', 'torso', 'neck', 'hips']) j[k].rotation.set(0, 0, 0);
  sister.root.position.set(0.9, 0, -2.6); sister.root.rotation.y = -0.5;
  idle(j, t + 1.3, 1);
  j.neck.rotation.y = t > ALARM_T + 0.15 ? -0.5 * Ease.outCubic(clamp((t - ALARM_T - 0.15) / 0.3)) : 0; // reaction, 150 ms after
  sister.setExpression(t > ALARM_T + 0.15 ? 'shock' : 'smile');
  sister.setBlink(blinkAt(t, 9));
}

// ---- shot list (times in s). Cuts land on sentence starts in the real videos (median 20–30 ms before the word). ----
const shots = [
  { start: 0, end: 2.0, ease: 'inOutSine', from: { pos: [1.2, 1.6, 6], look: [-0.3, 1.0, -3], fov: 50 }, to: { pos: [0.9, 1.5, 3.8], look: [-0.4, 1.1, -3], fov: 50 } },
  { start: 2.0, end: 4.0, ease: 'outCubic', from: { pos: [0.6, 1.4, 1.5], look: [-0.4, 1.4, -2.0], fov: 45 }, to: { pos: [0.1, 1.45, 0.2], look: [-0.5, 1.5, -2.0], fov: 45 } },
  { start: 4.0, end: 6.0, ease: 'inOutSine', shake: 0.01, from: { pos: [-0.5, 1.95, -0.4], look: [-0.6, 1.85, -2.2], fov: 35 }, to: { pos: [-0.55, 1.93, -0.7], look: [-0.6, 1.85, -2.2], fov: 35 } },
];
const director = new CameraDirector(camera, shots);
const { composer, grade } = buildPost(renderer, scene, camera, W, H, { bloom: 0.3, grade: { uVignette: 0.3 } });

window.DURATION = shots[shots.length - 1].end; window.FPS = FPS;
window.renderFrame = (i) => {
  const t = i / FPS;
  heroPose(t); sisterPose(t);
  director.apply(t);
  grade.uniforms.uTime.value = i;          // grain changes every frame, deterministically
  composer.render();
  return t;
};
// ---- motion blur by temporal supersampling (what separates pipeline B from A, see 09_VISUAL_EFFECTS.md) ----
// Render n sub-frames spread over a 180° shutter (half a frame) and average them with a running mean.
// Camera cuts are respected: sub-samples never cross into the next shot.
const accum = document.createElement('canvas'); accum.width = W; accum.height = H;
const actx = accum.getContext('2d');
window.renderFrameMB = (i, n = 6, shutter = 0.5) => {
  const shot = director.shotAt(i / FPS);
  for (let k = 0; k < n; k++) {
    let t = (i + (k / n - 0.5) * shutter) / FPS;
    t = Math.min(Math.max(t, shot.start), shot.end - 1e-4);
    heroPose(t); sisterPose(t); director.apply(t);
    grade.uniforms.uGrain.value = 0;                 // add grain once, after averaging
    composer.render();
    actx.globalAlpha = 1 / (k + 1); actx.drawImage(renderer.domElement, 0, 0);
  }
  grade.uniforms.uGrain.value = 0.025;
  return accum.toDataURL('image/png');
};
window.ready = true;
if (!params.has('capture')) {               // live preview mode
  const t0 = performance.now();
  const loop = () => { window.renderFrame(Math.floor(((performance.now() - t0) / 1000 % window.DURATION) * FPS)); requestAnimationFrame(loop); };
  loop();
}
