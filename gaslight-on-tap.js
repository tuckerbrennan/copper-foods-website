const section = document.querySelector('#on-tap');
const status = section.querySelector('#gl-tap-status');
const list = section.querySelector('#gl-tap-list');
const print = section.querySelector('#gl-print-taps');
if (new URLSearchParams(location.search).get('print') === 'taps') {
  document.body.classList.add('gl-print-taps');
  document.title = 'Gaslight | On Tap';
}
print.addEventListener('click', () => window.print());

function element(tag, text, className) {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
}

async function loadTaps() {
  try {
    const api = section.dataset.menuApi || 'https://xdkrnc3ra3.execute-api.us-east-2.amazonaws.com';
    const response = await fetch(api + '/gaslight/on-tap', {cache: 'no-store'});
    if (!response.ok) throw Error('Tap list unavailable');
    const {items} = await response.json();
    const rows = items.map(({name, brewery, style, abv, price}) => {
      const row = element('div', '', 'gl-tap-row');
      row.append(element('dt', name), element('dd', price));
      const details = [brewery, style, abv ? abv + '% ABV' : ''].filter(Boolean);
      if (details.length) row.append(element('dd', details.join(' · '), 'gl-tap-details'));
      return row;
    });
    list.replaceChildren(...rows);
    list.hidden = !rows.length;
    status.textContent = rows.length ? '' : 'Nothing is listed on tap right now.';
    print.disabled = false;
  } catch {
    status.textContent = 'The current tap list is unavailable. Please check with the bar.';
  }
}

void loadTaps();
