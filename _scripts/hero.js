/*
  homepage banner: pin it just below the header, and gently fade and zoom it
  as page content scrolls up over it
*/

{
  const onLoad = () => {
    const hero = document.querySelector(".hero");
    const header = document.querySelector("header");
    if (!hero || !header) return;
    const image = hero.querySelector("img");

    // keep banner just below the (sticky) header
    const setHeaderHeight = () =>
      document.documentElement.style.setProperty(
        "--header-height",
        header.offsetHeight + "px"
      );
    setHeaderHeight();
    window.addEventListener("resize", setHeaderHeight);

    // respect users who prefer less motion
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    let ticking = false;
    const update = () => {
      const progress = Math.min(window.scrollY / hero.offsetHeight, 1);
      image.style.opacity = 1 - progress * 0.6;
      image.style.transform = `scale(${1 + progress * 0.06})`;
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
