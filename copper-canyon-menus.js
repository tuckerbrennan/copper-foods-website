(function () {
  "use strict";

  // Progressive enhancement: without JavaScript all three menus remain readable.
  const menuNames = ["lunch", "dinner", "drinks"];
  const sections = Object.fromEntries(
    menuNames.map(function (name) {
      return [name, document.getElementById(name)];
    })
  );
  const links = Array.from(document.querySelectorAll(".digital-menu-link"));
  const nav = document.getElementById("menu-navigation");

  if (!nav || menuNames.some(function (name) { return !sections[name]; })) return;

  function nameFromHash() {
    const hash = decodeURIComponent(window.location.hash.replace(/^#/, ""));
    return menuNames.includes(hash) ? hash : "lunch";
  }

  function revealMenu(name, scroll) {
    const active = menuNames.includes(name) ? name : "lunch";

    menuNames.forEach(function (option) {
      sections[option].hidden = option !== active;
    });

    links.forEach(function (link) {
      if (link.getAttribute("href") === "#" + active) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });

    if (scroll) {
      // The sticky header and selector stay visible as visitors switch menus.
      nav.scrollIntoView({
        block: "start",
        behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth"
      });
    }
  }

  revealMenu(nameFromHash(), false);

  document.addEventListener("click", function (event) {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;

    const name = link.getAttribute("href").slice(1);
    if (!menuNames.includes(name)) return;

    event.preventDefault();
    if (window.location.hash !== "#" + name) {
      window.location.hash = name;
    } else {
      revealMenu(name, true);
    }
  });

  window.addEventListener("hashchange", function () {
    revealMenu(nameFromHash(), true);
  });
})();
