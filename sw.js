const CACHE = 'confianza-tut-v1';
const ASSETS = ['index.html', 'logo.png', 'icon-192.png', 'icon-512.png', 'icon-512-maskable.png', 'manifest.webmanifest'];

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

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);

  // Datos siempre desde red
  if (url.pathname.includes('/data/')) {
    return e.respondWith(
      fetch(e.request).catch(() =>
        caches.match(e.request).then(r => r || new Response('Sin conexión', { status: 503 }))
      )
    );
  }

  // Assets: cache first
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).then(res => {
      const clone = res.clone();
      caches.open(CACHE).then(c => c.put(e.request, clone));
      return res;
    }))
  );
});
