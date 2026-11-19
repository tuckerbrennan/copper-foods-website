const gallery = document.querySelector('[data-website-gallery]');
const endpoint = new URL('https://xdkrnc3ra3.execute-api.us-east-2.amazonaws.com/website-photos');
endpoint.searchParams.set('restaurant', gallery.dataset.websiteGallery);

try {
  const response = await fetch(endpoint, {cache: 'no-store'});
  if (response.ok) {
    const photos = await response.json();
    const grid = gallery.querySelector('.website-photo-grid');
    for (const photo of photos) {
      const image = document.createElement('img');
      image.src = photo.url;
      image.alt = photo.alt;
      image.loading = 'lazy';
      image.decoding = 'async';
      image.referrerPolicy = 'no-referrer';
      grid.append(image);
    }
    gallery.hidden = grid.childElementCount === 0;
  }
} catch {
  // The existing gallery remains visible when the staging photo service is unavailable.
}
