(function () {
  "use strict";

  const toggle = document.querySelector(".menu-toggle");
  const mobileNav = document.getElementById("mobile-navigation");

  function setMenuOpen(open) {
    if (!toggle || !mobileNav) return;
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
    mobileNav.hidden = !open;
  }

  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      setMenuOpen(toggle.getAttribute("aria-expanded") !== "true");
    });

    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        setMenuOpen(false);
      });
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setMenuOpen(false);
    });

    window.matchMedia("(min-width: 761px)").addEventListener("change", function (event) {
      if (event.matches) setMenuOpen(false);
    });
  }

  const year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
