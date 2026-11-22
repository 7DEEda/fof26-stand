var C='fof26-v2';
self.addEventListener('install',function(e){e.waitUntil(caches.open(C).then(function(c){return c.addAll(['./','./pl/','./pl/manifest.webmanifest','./pl/icon-192.png']);}));self.skipWaiting();});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(n){return n!==C;}).map(function(n){return caches.delete(n);}));}));self.clients.claim();});
self.addEventListener('fetch',function(e){if(e.request.method!=='GET'||new URL(e.request.url).origin!==location.origin){return;}
e.respondWith(fetch(e.request).then(function(r){var cp=r.clone();caches.open(C).then(function(c){c.put(e.request,cp);});return r;}).catch(function(){return caches.match(e.request,{ignoreSearch:true});}));});
