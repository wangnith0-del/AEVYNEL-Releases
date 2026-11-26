// =====================================================================================
// render.mjs — headless, frame-exact export: Playwright drives the page, pulls every frame as PNG,
// then ffmpeg encodes 30 fps H.264 (yuv420p, BT.709 tags, same spec as the analysed files).
// Usage: [MB=6] [FRAMES=74,76] node render.mjs [outDir=out] [width=576] [height=1024]
// =====================================================================================
import { createRequire } from 'node:module';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const { chromium } = createRequire(import.meta.url)('playwright'); // pre-installed globally (NODE_PATH)

const [outDir = 'out', W = '576', H = '1024'] = process.argv.slice(2);
const MB = +(process.env.MB || 1);                 // MB=6 node render.mjs -> 6 sub-frames per frame
const ONLY = process.env.FRAMES ? process.env.FRAMES.split(',').map(Number) : null; // e.g. FRAMES=74,76
const root = path.dirname(new URL(import.meta.url).pathname);
const types = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript' };

// minimal static server (ES modules cannot load from file://)
const server = http.createServer((req, res) => {
  const p = path.join(root, decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!p.startsWith(root) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': types[path.extname(p)] || 'application/octet-stream' });
  fs.createReadStream(p).pipe(res);
}).listen(0);
const port = server.address().port;

fs.mkdirSync(path.join(outDir, 'frames'), { recursive: true });
const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const page = await browser.newPage({ viewport: { width: +W, height: +H }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('PAGE ERROR', e.message));
await page.goto(`http://127.0.0.1:${port}/index.html?capture=1&w=${W}&h=${H}`);
await page.waitForFunction(() => window.ready === true, null, { timeout: 60000 });
const total = await page.evaluate(() => Math.round(window.DURATION * window.FPS));
const t0 = Date.now();
for (const i of ONLY || [...Array(total).keys()]) {
  const dataUrl = MB > 1
    ? await page.evaluate(([i, n]) => window.renderFrameMB(i, n), [i, MB])          // motion-blurred frame
    : await page.evaluate(i => { window.renderFrame(i); return document.querySelector('canvas').toDataURL('image/png'); }, i);
  fs.writeFileSync(path.join(outDir, 'frames', `f${String(i).padStart(5, '0')}.png`), Buffer.from(dataUrl.split(',')[1], 'base64'));
}
console.log(`rendered ${(ONLY || [...Array(total).keys()]).length} frames in ${((Date.now() - t0) / 1000).toFixed(1)} s`);
await browser.close(); server.close();

if (!ONLY) execFileSync('ffmpeg', ['-v', 'error', '-y', '-framerate', '30', '-i', path.join(outDir, 'frames', 'f%05d.png'),
  '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p',
  '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart',
  path.join(outDir, 'render.mp4')], { stdio: 'inherit' });
if (!ONLY) console.log('wrote', path.join(outDir, 'render.mp4'));
