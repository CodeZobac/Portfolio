var swiper = new Swiper(".swiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: 2,
  speed: 600,
  coverflowEffect: {
    rotate: 0,
    stretch: 0,
    depth: 100,
    modifier: 3,
    slideShadows: true,
  },
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: false,
  },
});

let currentSlide = 0;

function navigate(direction) {
  const slides = document.querySelectorAll(".slides > div");
  const totalSlides = slides.length;

  // Calcula o próximo slide
  currentSlide = (currentSlide + direction + totalSlides) % totalSlides;

  // Esconde todos os slides
  slides.forEach((slide) => {
    slide.style.display = "none";
  });

  // Mostra o slide atual
  slides[currentSlide].style.display = "block";
}

// Inicializa o carrossel
window.onload = () => {
  navigate(0); // Mostra o primeiro slide
};
