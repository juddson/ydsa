document.addEventListener("DOMContentLoaded", () => {
  const root = document.querySelector(".carousel");
  if (!root) return;

  const track = root.querySelector(".carousel__track");
  const slides = Array.from(root.querySelectorAll(".carousel__slide"));
  const prevBtn = root.querySelector(".carousel__btn--prev");
  const nextBtn = root.querySelector(".carousel__btn--next");
  const dotsWrap = root.querySelector(".carousel__dots");

  let index = 0;
  const last = slides.length - 1;

  // Build dots
  slides.forEach((_, i) => {
    const b = document.createElement("button");
    b.className = "carousel__dot";
    b.type = "button";
    b.role = "tab";
    b.setAttribute("aria-label", `Go to slide ${i + 1}`);
    b.addEventListener("click", () => goTo(i));
    dotsWrap.appendChild(b);
  });

  const dots = Array.from(dotsWrap.children);

  function update() {
    track.style.transform = `translateX(${-index * 100}%)`;
    slides.forEach((s, i) => s.classList.toggle("is-active", i === index));
    dots.forEach((d, i) => d.setAttribute("aria-selected", i === index ? "true" : "false"));
  }

  function goTo(i) {
    index = (i + slides.length) % slides.length;
    update();
  }

  prevBtn.addEventListener("click", () => goTo(index - 1));
  nextBtn.addEventListener("click", () => goTo(index + 1));

  // Keyboard support on arrows
  root.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") goTo(index - 1);
    if (e.key === "ArrowRight") goTo(index + 1);
  });

  // Optional: auto-advance every 5s, pause on hover
  let timer = setInterval(() => goTo(index + 1), 5000);
  root.addEventListener("mouseenter", () => clearInterval(timer));
  root.addEventListener("mouseleave", () => {
    timer = setInterval(() => goTo(index + 1), 5000);
  });

  update(); // initial
});
