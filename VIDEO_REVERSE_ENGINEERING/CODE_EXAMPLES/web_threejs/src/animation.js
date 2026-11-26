// =====================================================================================
// animation.js — RECONSTRUCTED animation layer for R6 characters.
//
// What the frame-by-frame inspection showed (see 05_ANIMATION_SYSTEMS.md):
//  * walk/run cycles are the classic R6 "pendulum": arms and legs swing in opposition,
//    no knees/elbows (rigid parts) -> believability comes from body bob, torso lean,
//    head counter-motion and per-limb motion blur (V3/V6), not from joint detail.
//  * gestures (V3 "screamed": arms raise in ~6 frames, overshoot then settle) are keyframed
//    with ease-out + small overshoot = anticipation / follow-through.
//  * idle: subtle breathing + periodic blinks; faces swap instantly.
// Everything is a pure function of time t (seconds) => deterministic, frame-exact renders.
// =====================================================================================

export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const lerp = (a, b, t) => a + (b - a) * t;
export const Ease = {
  linear: t => t,
  inOutSine: t => -(Math.cos(Math.PI * t) - 1) / 2,
  outCubic: t => 1 - Math.pow(1 - t, 3),
  inCubic: t => t * t * t,
  inOutCubic: t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  outBack: (t, s = 1.70158) => 1 + (s + 1) * Math.pow(t - 1, 3) + s * Math.pow(t - 1, 2), // overshoot
};

/**
 * Locomotion cycle. phase advances with distance travelled (not time) so feet never "skate":
 * stride length L -> phase = distance / L * 2π. speed in units/s, gait 'walk' | 'run'.
 */
export function locomotion(j, phase, { gait = 'walk', weight = 1 } = {}) {
  const run = gait === 'run';
  const legAmp = (run ? 0.95 : 0.55) * weight;   // radians
  const armAmp = (run ? 1.05 : 0.5) * weight;
  const s = Math.sin(phase);
  j.lHip.rotation.x = s * legAmp; j.rHip.rotation.x = -s * legAmp;
  j.lShoulder.rotation.x = -s * armAmp; j.rShoulder.rotation.x = s * armAmp;   // opposition
  // body bob: twice per cycle (each foot contact), lowest at contact
  j.hips.position.y = 0.8 + Math.abs(Math.cos(phase)) * (run ? 0.06 : 0.025) * weight;
  j.torso.rotation.x = (run ? 0.18 : 0.04) * weight;         // forward lean sells momentum
  j.torso.rotation.y = s * 0.08 * weight;                    // shoulder/hip counter-twist
  j.neck.rotation.y = -s * 0.06 * weight;                    // head stabilises against twist
  j.hips.rotation.z = Math.cos(phase) * 0.03 * weight;       // lateral weight shift
}

/** Idle: breathing (≈0.25 Hz) + micro sway; keeps "statues" alive between actions. */
export function idle(j, t, amount = 1) {
  const br = Math.sin(t * Math.PI * 2 * 0.25);
  j.torso.scale.y = 1 + br * 0.008 * amount;
  j.neck.rotation.x = br * 0.02 * amount;
  j.lShoulder.rotation.z = -0.04 - br * 0.015 * amount;
  j.rShoulder.rotation.z = 0.04 + br * 0.015 * amount;
  j.hips.rotation.z = Math.sin(t * 0.7) * 0.01 * amount;
}

/** Blink schedule: deterministic pseudo-random intervals 2.5–4.5 s, 4-frame blink (close, hold, open). */
export function blinkAt(t, seed = 1) {
  let acc = 0.8, k = 0;
  while (acc < t + 1) {
    const r = Math.abs(Math.sin(seed * 12.9898 + k * 78.233)) % 1;
    if (t >= acc && t < acc + 0.13) { const u = (t - acc) / 0.13; return u < 0.5 ? u * 2 : (1 - u) * 2; }
    acc += 2.5 + r * 2; k++;
  }
  return 0;
}

/**
 * Keyframe track evaluation. keys: [{t, v, ease}] where ease applies to the segment ENDING at that key.
 * Values may be numbers or arrays (vectors).
 */
export function evalTrack(keys, t) {
  if (t <= keys[0].t) return keys[0].v;
  for (let i = 1; i < keys.length; i++) {
    if (t <= keys[i].t) {
      const a = keys[i - 1], b = keys[i];
      const u = (Ease[b.ease || 'inOutSine'])((t - a.t) / (b.t - a.t));
      return Array.isArray(a.v) ? a.v.map((x, k) => lerp(x, b.v[k], u)) : lerp(a.v, b.v, u);
    }
  }
  return keys[keys.length - 1].v;
}

/**
 * "Scream / alarm" gesture reconstructed from V3 f2115–f2137: anticipation (arms dip 2 frames),
 * fast raise (~5 frames, outBack overshoot), hold with tremble. t0 = gesture start.
 */
export function gestureAlarm(j, t, t0) {
  const lt = t - t0; if (lt < 0) return false;
  const arm = evalTrack([
    { t: 0, v: 0 }, { t: 0.07, v: 0.15, ease: 'outCubic' },        // anticipation: slight down/back
    { t: 0.25, v: -2.2, ease: 'outBack' },                           // raise with overshoot
    { t: 0.45, v: -2.0, ease: 'inOutSine' },                         // settle (follow-through)
  ], lt);
  const tremble = lt > 0.45 ? Math.sin(lt * 40) * 0.03 : 0;
  j.lShoulder.rotation.x = arm + tremble; j.rShoulder.rotation.x = arm - tremble;
  j.lShoulder.rotation.z = -0.35; j.rShoulder.rotation.z = 0.35;
  j.neck.rotation.x = -0.12 * clamp(lt / 0.25);                      // head tilts back with the shout
  return true;
}

/**
 * Critically-damped spring for secondary motion (hair, accessories, camera follow).
 * Stateless variant: response of a spring to a step of size `step` applied at time t0.
 */
export function springStep(t, t0, step, omega = 14) {
  const x = Math.max(0, t - t0);
  return step * (1 - (1 + omega * x) * Math.exp(-omega * x));
}
