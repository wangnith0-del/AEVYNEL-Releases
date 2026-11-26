// =====================================================================================
// post.js — RECONSTRUCTED post-processing chain.
// Order (matches what is observable in V1/V3/V6): scene -> bloom -> grade (lift/gain/sat/warmth)
// -> vignette -> grain -> output. Values are tuned estimates; V3 measured corner/centre luma 0.695.
// =====================================================================================
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

export const GradeShader = {
  uniforms: {
    tDiffuse: { value: null }, uTime: { value: 0 },
    uSaturation: { value: 1.15 }, uWarmth: { value: 0.04 }, uContrast: { value: 1.06 },
    uVignette: { value: 0.35 }, uGrain: { value: 0.025 }, uAspect: { value: 9 / 16 },
  },
  vertexShader: `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }`,
  fragmentShader: `
    uniform sampler2D tDiffuse; uniform float uTime, uSaturation, uWarmth, uContrast, uVignette, uGrain, uAspect;
    varying vec2 vUv;
    float hash(vec2 p){ return fract(sin(dot(p, vec2(12.9898,78.233))) * 43758.5453); }
    void main(){
      vec3 c = texture2D(tDiffuse, vUv).rgb;
      float l = dot(c, vec3(0.2126,0.7152,0.0722));
      c = mix(vec3(l), c, uSaturation);                  // saturation
      c += vec3(uWarmth, uWarmth*0.3, -uWarmth);         // warm shift (orange/teal-free, cheap)
      c = (c - 0.5) * uContrast + 0.5;                   // contrast around mid-grey
      vec2 d = (vUv - 0.5) * vec2(uAspect, 1.0) * 1.6;   // elliptical vignette for 9:16
      c *= 1.0 - uVignette * smoothstep(0.35, 1.0, dot(d,d));
      c += (hash(vUv * 1024.0 + uTime) - 0.5) * uGrain;  // animated grain
      gl_FragColor = vec4(clamp(c, 0.0, 1.0), 1.0);
    }`,
};

export function buildPost(renderer, scene, camera, w, h, opts = {}) {
  const composer = new EffectComposer(renderer);
  composer.setSize(w, h);
  composer.addPass(new RenderPass(scene, camera));
  composer.addPass(new UnrealBloomPass(new THREE.Vector2(w, h), opts.bloom ?? 0.35, 0.6, 0.85)); // strength, radius, threshold
  composer.addPass(new OutputPass());                    // tone mapping + sRGB before grading in display space
  const grade = new ShaderPass(GradeShader);
  Object.entries(opts.grade || {}).forEach(([k, v]) => (grade.uniforms[k].value = v));
  composer.addPass(grade);
  return { composer, grade };
}
