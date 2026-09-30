/*
  site banner: gently dim and zoom the fixed background banner as page
  content scrolls up over it
*/

{
  const onLoad = () => {
    const hero = document.querySelector(".hero");
    const spacer = document.querySelector(".hero-spacer");
    if (!hero || !spacer) return;
    const image = hero.querySelector("img");

    // respect users who prefer less motion
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    let ticking = false;
    const update = () => {
      const progress = Math.min(window.scrollY / spacer.offsetHeight, 1);
      image.style.opacity = 1 - progress * 0.35;
      image.style.transform = `scale(${1 + progress * 0.05})`;
      ticking = false;
    };
    window.addEventListener(
      "scroll",
      () => {
        if (!ticking) window.requestAnimationFrame(update);
        ticking = true;
      },
      { passive: true }
    );
    update();
  };

  window.addEventListener("load", onLoad);
}
