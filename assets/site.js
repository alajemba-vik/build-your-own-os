/* Build your own OS: English/French, Mac/Windows switch, copy buttons, reference code, progress. No tracking. */
(function () {
  const FR = document.documentElement.lang === 'fr';
  const L = FR ? { copy: 'Copier', copied: 'Copié', manual: 'Sélectionnez et copiez', loading: 'Chargement…',
                   failed: 'Impossible de le charger ici.', open: 'Ouvrir', onGitHub: 'sur GitHub', finished: 'terminé' }
               : { copy: 'Copy', copied: 'Copied', manual: 'Select and copy', loading: 'Loading…',
                   failed: "Couldn't load it here.", open: 'Open', onGitHub: 'on GitHub', finished: 'finished' };
  const root = document.body.dataset.root || '';   /* '' for English pages, '../' for French pages in fr/ */
  const store = { get: (k) => { try { return localStorage.getItem(k); } catch (e) { return null; } },
                  set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} } };

  /* macOS / Windows: guess from the browser once, then remember the choice */
  const guess = /Win/i.test(navigator.platform || navigator.userAgent) ? 'win' : 'mac';
  function setOS(os) {
    document.body.dataset.os = os; store.set('byos.os', os);
    document.querySelectorAll('.os-switch button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.os === os)));
  }
  setOS(store.get('byos.os') || guess);
  document.querySelectorAll('.os-switch button').forEach(b => b.addEventListener('click', () => setOS(b.dataset.os)));

  /* English / French: remember the choice, and open English pages in French for someone who chose French */
  const sw = document.querySelector('.lang-switch');
  if (sw) {
    sw.addEventListener('click', () => store.set('byos.lang', sw.dataset.lang));
    if (!FR && store.get('byos.lang') === 'fr') location.replace(sw.href + location.hash);
  }

  /* mobile menu */
  const menu = document.querySelector('.menu-btn');
  if (menu) menu.addEventListener('click', () => {
    const open = document.body.classList.toggle('menu-open'); menu.setAttribute('aria-expanded', String(open));
  });

  /* copy buttons */
  function addCopy(box, getText) {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'copy'; b.textContent = L.copy;
    b.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(getText()); b.textContent = L.copied; }
      catch (e) { b.textContent = L.manual; }
      setTimeout(() => { b.textContent = L.copy; }, 1600);
    });
    box.appendChild(b);
  }
  document.querySelectorAll('.code').forEach(c => addCopy(c, () => c.querySelector('pre').innerText.trim()));
  document.querySelectorAll('.prompt').forEach(p => addCopy(p, () => [...p.querySelectorAll('p')].map(x => x.innerText).join('\n\n').trim()));

  /* "peek at the reference": load the real files from the repository when opened */
  const esc = (s) => s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  document.querySelectorAll('details.ref').forEach(d => {
    d.addEventListener('toggle', async () => {
      if (!d.open || d.dataset.loaded) return;
      d.dataset.loaded = '1';
      for (const path of d.dataset.files.split(/\s+/)) {
        const box = document.createElement('div'); box.className = 'code file';
        box.innerHTML = `<span class="label">${esc(path)}</span><pre>${L.loading}</pre>`;
        d.appendChild(box);
        try {
          const r = await fetch(root + path); if (!r.ok) throw new Error(r.status);
          box.querySelector('pre').innerHTML = esc(await r.text());
        } catch (e) {
          box.querySelector('pre').innerHTML = `${L.failed} <a href="https://github.com/alajemba-vik/build-your-own-os/blob/main/${esc(path)}">${L.open} ${esc(path)} ${L.onGitHub}</a>`;
        }
        addCopy(box, () => box.querySelector('pre').innerText);
      }
    });
  });

  /* progress: "I finished this chapter" */
  const page = document.body.dataset.page;
  const done = JSON.parse(store.get('byos.done') || '{}');
  const box = document.querySelector('.done input');
  if (box && page) {
    box.checked = !!done[page];
    box.addEventListener('change', () => { done[page] = box.checked; store.set('byos.done', JSON.stringify(done)); paintTicks(); });
  }
  function paintTicks() {
    document.querySelectorAll('nav.side a[data-page]').forEach(a => {
      const t = a.querySelector('.tick');
      if (t) t.textContent = done[a.dataset.page] ? '✓' : '';
      if (t) t.setAttribute('aria-label', done[a.dataset.page] ? L.finished : '');
    });
  }
  paintTicks();
})();
