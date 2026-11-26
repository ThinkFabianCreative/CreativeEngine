import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path'; import {spawn} from 'node:child_process';
import { chromium } from 'playwright';
const root = path.dirname(new URL(import.meta.url).pathname);
const mode = process.argv[2] || 'stills'; const FPS = +(process.argv[3]||60); const DUR = 15;
const types={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript'};
const srv = http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0])); if(!fs.existsSync(f)){r.writeHead(404);return r.end();} r.writeHead(200,{'content-type':types[path.extname(f)]||'application/octet-stream'}); fs.createReadStream(f).pipe(r);}).listen(8731);
const browser = await chromium.launch({executablePath: process.env.HOME+'/Library/Caches/ms-playwright/chromium-1243/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing', args:['--use-angle=metal','--ignore-gpu-blocklist','--enable-gpu']});
const page = await browser.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
page.on('console',m=>console.log('[page]',m.text())); page.on('pageerror',e=>console.log('[err]',e.message));
await page.goto('http://localhost:8731/index.html'); await page.waitForFunction(()=>window.ready===true,null,{timeout:60000});
fs.mkdirSync(path.join(root,'out'),{recursive:true});
if(mode==='stills'){ const ts=(process.argv[4]||'1,3,5.2,7.6,10,12,14.5').split(',').map(Number);
  for(const t of ts){ await page.evaluate(t=>window.renderAt(t),t); await page.screenshot({path:path.join(root,'out',`still_${t}.jpg`),quality:85,type:'jpeg'}); console.log('still',t);} }
else { const ff=spawn('ffmpeg',['-y','-f','image2pipe','-framerate',String(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','16','-preset','slow','-movflags','+faststart',path.join(root,'out','marble-run.mp4')],{stdio:['pipe','inherit','inherit']});
  const N=DUR*FPS; for(let i=0;i<N;i++){ await page.evaluate(t=>window.renderAt(t),i/FPS); const b=await page.screenshot({type:'jpeg',quality:95}); if(!ff.stdin.write(b)) await new Promise(r=>ff.stdin.once('drain',r)); if(i%60===0) console.log('frame',i,'/',N);} ff.stdin.end(); await new Promise(r=>ff.on('close',r)); }
await browser.close(); srv.close();
