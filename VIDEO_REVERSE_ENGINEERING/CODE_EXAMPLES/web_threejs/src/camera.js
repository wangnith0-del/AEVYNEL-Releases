// =====================================================================================
// camera.js — RECONSTRUCTED shot-list camera director.
//
// Measured in the videos (ANALYSIS_DATA/*_camera.json, *_zoom_forensics.json):
//  * 510 shots, median 1.35–2.5 s; push-in is the dominant move (up to 57 % of shots in V4).
//  * the moves show PARALLAX (RANSAC similarity fit: 29–43 % inliers vs 100 % for a synthetic
//    2D zoom) => they are real 3D camera moves made in the engine, not editor zooms.
//  * jitter is near zero (median 0.004–0.09 px/frame) => tweened cameras, not handheld capture.
//  * speed profiles mix ease-in-out, ease-in and ease-out (no single global curve).
// A shot = { start, end, from:{pos,look,fov}, to:{pos,look,fov}, ease, shake }.
// =====================================================================================
import * as THREE from 'three';
import { Ease, lerp, clamp } from './animation.js';

const v3 = a => new THREE.Vector3(...a);

export class CameraDirector {
  constructor(camera, shots) { this.camera = camera; this.shots = shots; }
  shotAt(t) { return this.shots.find(s => t >= s.start && t < s.end) || this.shots[this.shots.length - 1]; }
  /** Evaluate the camera for absolute time t. Returns the active shot (hard cut between shots). */
  apply(t) {
    const s = this.shotAt(t);
    const u = (Ease[s.ease || 'inOutSine'])(clamp((t - s.start) / (s.end - s.start)));
    const pos = v3(s.from.pos).lerp(v3(s.to.pos), u);
    const look = v3(s.from.look).lerp(v3(s.to.look), u);
    // optional low-frequency "breathing" so static shots are never dead-still (sum of incommensurate sines)
    if (s.shake) {
      const a = s.shake;
      pos.x += a * (Math.sin(t * 1.3) * 0.6 + Math.sin(t * 2.9) * 0.4);
      pos.y += a * (Math.sin(t * 1.7 + 1) * 0.6 + Math.sin(t * 3.7) * 0.4);
    }
    this.camera.position.copy(pos);
    this.camera.fov = lerp(s.from.fov ?? 50, s.to.fov ?? s.from.fov ?? 50, u);
    this.camera.updateProjectionMatrix();
    this.camera.lookAt(look);
    return s;
  }
  /** Helper: a push-in toward a target, the workhorse move of the genre. */
  static pushIn(start, end, target, { dist0 = 4, dist1 = 2.6, height = 0.2, side = 0, fov = 45, ease = 'inOutSine', shake = 0 } = {}) {
    const [x, y, z] = target;
    return { start, end, ease, shake,
      from: { pos: [x + side, y + height, z + dist0], look: target, fov },
      to: { pos: [x + side * (dist1 / dist0), y + height, z + dist1], look: target, fov } };
  }
}
