const calendar = document.querySelector('.gl-calendar');
const status = document.querySelector('#gl-no-shows');
const timeZone = 'America/New_York';
const day = new Intl.DateTimeFormat('en-US', {timeZone, weekday: 'short', month: 'short', day: 'numeric'});
const dateKey = new Intl.DateTimeFormat('en-CA', {timeZone, year: 'numeric', month: '2-digit', day: '2-digit'});
const clock = new Intl.DateTimeFormat('en-US', {timeZone, hour: 'numeric', minute: '2-digit'});

async function loadShows() {
  status.textContent = 'Loading upcoming shows…';
  try {
    const response = await fetch(new URL('./gaslight-shows.json', import.meta.url));
    if (!response.ok) throw Error('Calendar unavailable');
    const today = new Date();
    const shows = (await response.json()).filter(show => show.endsAt
      ? Date.parse(show.endsAt) > today.getTime()
      : dateKey.format(new Date(show.startsAt)) >= dateKey.format(today));

    for (const show of shows) {
      const start = new Date(show.startsAt);
      const row = document.createElement('li');
      const date = document.createElement('time');
      date.dateTime = show.startsAt;
      date.textContent = day.format(start);
      const copy = document.createElement('div');
      const title = document.createElement('h3');
      title.textContent = show.title;
      const details = document.createElement('p');
      const time = show.endsAt ? clock.formatRange(start, new Date(show.endsAt)) : clock.format(start);
      details.textContent = [time, show.details].filter(Boolean).join(' · ');
      copy.append(title, details);
      row.append(date, copy);
      const link = document.createElement('a');
      const url = show.ticketUrl ?? show.url;
      if (url && new URL(url).protocol === 'https:') {
        link.href = url;
        link.textContent = show.ticketUrl ? 'Get tickets' : 'Show details';
        link.setAttribute('aria-label', link.textContent + ' for ' + show.title);
        row.append(link);
      }
      calendar.append(row);
    }
    calendar.hidden = shows.length === 0;
    status.hidden = !calendar.hidden;
    status.textContent = 'No upcoming shows are listed right now.';
  } catch {
    status.textContent = 'The calendar is temporarily unavailable. Check Gaslight’s event links below.';
  }
}

void loadShows();
