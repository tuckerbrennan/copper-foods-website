(function () {
  "use strict";

  const lightbox = document.getElementById("cc-lightbox");
  if (!lightbox) return;

  const image = lightbox.querySelector("img");
  const closeButton = lightbox.querySelector(".cc-lightbox-close");
  const photos = document.querySelectorAll(".cc-gallery-tile");
  let returnFocusTo = null;

  function closeLightbox() {
    lightbox.hidden = true;
    image.removeAttribute("src");
    document.body.style.overflow = "";
    if (returnFocusTo) returnFocusTo.focus();
    returnFocusTo = null;
  }

  function openLightbox(button) {
    returnFocusTo = button;
    image.onerror = function () {
      const fallback = button.dataset.fallback;
      if (fallback && image.src !== fallback) {
        image.onerror = null;
        image.src = fallback;
        image.alt = "Temporary illustrative image; original Copper Canyon photo unavailable";
      }
    };
    image.src = button.dataset.image;
    image.alt = button.dataset.alt || "Gallery photograph";
    lightbox.hidden = false;
    document.body.style.overflow = "hidden";
    closeButton.focus();
  }

  photos.forEach(function (button) {
    button.addEventListener("click", function () {
      openLightbox(button);
    });
  });

  closeButton.addEventListener("click", closeLightbox);
  lightbox.addEventListener("click", function (event) {
    if (event.target === lightbox) closeLightbox();
  });

  document.addEventListener("keydown", function (event) {
    if (lightbox.hidden) return;
    if (event.key === "Escape") closeLightbox();
    if (event.key === "Tab") {
      // The close button is the only focusable element within the modal.
      event.preventDefault();
      closeButton.focus();
    }
  });
})();
