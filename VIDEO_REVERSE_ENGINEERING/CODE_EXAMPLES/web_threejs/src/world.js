// =====================================================================================
// world.js — RECONSTRUCTED modular suburb ("In this town...") environment + lighting.
//
// The environments in V1–V7 are low-poly modular kits: box houses with gable roofs, sidewalks,
// lamp posts, ball/cone trees, repeated many times (V1 town square, V3 street). We rebuild that
// with InstancedMesh so 200 houses cost a handful of draw calls.
// Lighting reproduces the "sunny Roblox" look: one warm directional sun with soft shadows,
// a sky/ground hemisphere fill, exponential fog for depth. Values are ESTIMATES tuned by eye.
// =====================================================================================
import * as THREE from 'three';

function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

export function buildWorld(scene, { seed = 7, preset = 'day' } = {}) {
  const P = {
    day:    { sky: 0x8ec5ff, ground: 0x6fbf4a, sun: 0xfff1d6, sunI: 2.6, hemiI: 0.9, fog: 0xbfdcff, sunPos: [8, 14, 6] },
    sunset: { sky: 0xf08a5d, ground: 0x7a5c8f, sun: 0xffb070, sunI: 2.2, hemiI: 0.6, fog: 0xc98aa0, sunPos: [-12, 4, -6] },
  }[preset];
  scene.background = new THREE.Color(P.sky);
  scene.fog = new THREE.Fog(P.fog, 18, 70);

  // --- lights ---
  const hemi = new THREE.HemisphereLight(P.sky, P.ground, P.hemiI); scene.add(hemi);
  const sun = new THREE.DirectionalLight(P.sun, P.sunI);
  sun.position.set(...P.sunPos); sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048);
  Object.assign(sun.shadow.camera, { left: -15, right: 15, top: 15, bottom: -15, near: 1, far: 60 });
  sun.shadow.radius = 4; sun.shadow.bias = -0.0005; sun.shadow.normalBias = 0.02;
  scene.add(sun);

  // --- ground, road, sidewalks ---
  const mat = (c, r = 0.9) => new THREE.MeshStandardMaterial({ color: c, roughness: r });
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(200, 200), mat(0x5fb83a));
  ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const road = new THREE.Mesh(new THREE.PlaneGeometry(6, 200), mat(0x3b3f4a, 0.95));
  road.rotation.x = -Math.PI / 2; road.position.y = 0.01; road.receiveShadow = true; scene.add(road);
  for (const x of [-4, 4]) {
    const walk = new THREE.Mesh(new THREE.BoxGeometry(2, 0.12, 200), mat(0xcfc8bb));
    walk.position.set(x, 0.06, 0); walk.receiveShadow = true; scene.add(walk);
  }
  // dashed centre line (instanced)
  const dash = new THREE.InstancedMesh(new THREE.PlaneGeometry(0.15, 1.2), mat(0xffffff, 0.6), 60);
  const m4 = new THREE.Matrix4(), q = new THREE.Quaternion().setFromEuler(new THREE.Euler(-Math.PI / 2, 0, 0));
  for (let i = 0; i < 60; i++) { m4.compose(new THREE.Vector3(0, 0.02, -90 + i * 3), q, new THREE.Vector3(1, 1, 1)); dash.setMatrixAt(i, m4); }
  scene.add(dash);

  // --- modular houses: body + roof instanced, per-instance colour ---
  const N = 40, r = rng(seed);
  const body = new THREE.InstancedMesh(new THREE.BoxGeometry(1, 1, 1), mat(0xffffff, 0.85), N);
  const roofGeo = new THREE.CylinderGeometry(0.0001, 0.75, 1, 4, 1); roofGeo.rotateY(Math.PI / 4); // pyramid roof
  const roof = new THREE.InstancedMesh(roofGeo, mat(0xffffff, 0.8), N);
  const palette = [0xf2e6c9, 0x9cc3e6, 0xe89a8a, 0xb8d89a, 0xf4d06f, 0xd6b3e6, 0xffffff];
  const roofs = [0x7a3b2e, 0x3d4a6b, 0x5a5a5a, 0x8b2f3c];
  const s3 = new THREE.Vector3(), p3 = new THREE.Vector3(), id = new THREE.Quaternion();
  for (let i = 0; i < N; i++) {
    const side = i % 2 ? 1 : -1, z = -80 + Math.floor(i / 2) * 5 + r() * 1.5;
    const w = 3 + r() * 1.5, h = 2.2 + r() * 1.6, d = 3 + r();
    p3.set(side * (8 + r()), h / 2, z); s3.set(w, h, d); body.setMatrixAt(i, m4.compose(p3, id, s3));
    body.setColorAt(i, new THREE.Color(palette[Math.floor(r() * palette.length)]));
    p3.set(side * (8 + 0), h + 0.75, z); s3.set(w * 1.45, 1.5, d * 1.45); roof.setMatrixAt(i, m4.compose(p3, id, s3));
    roof.setColorAt(i, new THREE.Color(roofs[Math.floor(r() * roofs.length)]));
  }
  for (const m of [body, roof]) { m.castShadow = m.receiveShadow = true; scene.add(m); }

  // --- trees: trunk + "ball" canopy instanced (V1/V2 style lollipop trees) ---
  const T = 30;
  const trunk = new THREE.InstancedMesh(new THREE.CylinderGeometry(0.12, 0.15, 1.2, 6), mat(0x6b4a2b), T);
  const crown = new THREE.InstancedMesh(new THREE.IcosahedronGeometry(0.9, 1), new THREE.MeshStandardMaterial({ color: 0x3f9e3a, roughness: 0.8, flatShading: true }), T);
  for (let i = 0; i < T; i++) {
    const side = i % 2 ? 1 : -1, z = -75 + i * 5 + r() * 2, x = side * (5.4 + r() * 0.3), k = 0.8 + r() * 0.5;
    trunk.setMatrixAt(i, m4.compose(p3.set(x, 0.6, z), id, s3.set(1, 1, 1)));
    crown.setMatrixAt(i, m4.compose(p3.set(x, 1.6 + k * 0.5, z), id, s3.set(k, k, k)));
  }
  for (const m of [trunk, crown]) { m.castShadow = true; m.receiveShadow = true; scene.add(m); }
  return { sun, hemi };
}
