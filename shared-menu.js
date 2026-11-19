const host = document.querySelector('[data-shared-menu]');

if (host) {
  const api = host.dataset.menuApi || 'https://xdkrnc3ra3.execute-api.us-east-2.amazonaws.com';
  const url = new URL(api + '/restaurant-menu', location.origin);
  url.searchParams.set('restaurant', host.dataset.sharedMenu);
  try {
    const response = await fetch(url, {cache: 'no-store'});
    if (!response.ok) throw Error('Menu unavailable');
    const {pages} = await response.json();
    if (pages.length) {
      for (const page of pages) {
        const source = new URL(url);
        source.searchParams.set('photo', page.file);
        const section = document.createElement('section');
        const figure = document.createElement('figure');
        const items = Array.isArray(page.items) ? page.items : [];
        if (items.length) {
          const heading = document.createElement('h2');
          heading.textContent = page.label;
          const list = document.createElement('dl');
          list.className = 'reviewed-menu-items';
          for (const item of items) {
            const row = document.createElement('div');
            row.className = 'reviewed-menu-item';
            const name = document.createElement('dt');
            name.textContent = item.name;
            const price = document.createElement('dd');
            price.textContent = item.price;
            row.append(name, price);
            if (item.description) {
              const description = document.createElement('dd');
              description.className = 'reviewed-menu-description';
              description.textContent = item.description;
              row.append(description);
            }
            list.append(row);
          }
          section.append(heading, list);
        }
        const link = document.createElement('a');
        const img = document.createElement('img');
        link.href = source.href;
        link.target = '_blank';
        link.rel = 'noopener';
        link.setAttribute('aria-label', 'Open full size: ' + page.label);
        img.alt = page.label;
        img.src = source.href;
        img.loading = 'lazy';
        if (items.length) link.textContent = 'View menu photo';
        else link.append(img);
        figure.append(link);
        section.append(figure);
        host.append(section);
      }
      host.hidden = false;
      document.querySelectorAll('[data-menu-fallback]').forEach(fallback => { fallback.hidden = true; });
      host.dataset.published = 'true';
    }
  } catch {
    // Keep the last bundled menu available when the published feed is unavailable.
  }
}
