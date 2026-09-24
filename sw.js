const CACHE = 'confianza-tut-v2';
const ASSETS = ['logo.png', 'icon-192.png', 'icon-512.png', 'icon-512-maskable.png', 'manifest.webmanifest'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(names =>
      Promise.all(names.map(name => name !== CACHE ? caches.delete(name) : null))
    )
  );
  self.clients.claim();
});

function isShell(url) {
  return url.pathname.endsWith('/') || url.pathname.endsWith('/index.html');
}

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);

  // HTML (shell) y datos: siempre desde red, con fallback a caché offline
  if (isShell(url) || url.pathname.includes('/data/')) {
    e.respondWith(
      fetch(e.request).then(res => {
        if (isShell(url)) { const clone = res.clone(); caches.open(CACHE).then(c => c.put(e.request, clone)); }
        return res;
      }).catch(() =>
        caches.match(e.request).then(r => r || new Response('Sin conexión', { status: 503 }))
      )
    );
    return;
  }

  // Assets estáticos: cache first
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).then(res => {
      const clone = res.clone();
      caches.open(CACHE).then(c => c.put(e.request, clone));
      return res;
    }))
  );
});
