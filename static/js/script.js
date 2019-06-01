const burger = document.querySelector('#hamburger');
const sideNav = document.querySelector('.side-nav');
const backArrowContainer = document.querySelector('.back-arrow');
const backArrow = document.querySelector('.back-arrow');
const navLinks = document.querySelectorAll('.nav-link');

burger.addEventListener('click', () => {
  sideNav.classList.add('side-nav-active');
  backArrow.classList.add('back-arrow-anim');
  navLinks.forEach((link, index) => {
    link.addEventListener('click', () => {
      sideNav.classList.remove('side-nav-active');
      backArrow.classList.remove('back-arrow-anim');
    });
    link.classList.add('nav-link-anim');
    link.style.animationDelay = index / navLinks.length + 's';
    link.style.transitionDelay = index / navLinks.length + 's';
  });
});

backArrowContainer.addEventListener('click', () => {
  sideNav.classList.remove('side-nav-active');
  backArrow.classList.remove('back-arrow-anim');
  navLinks.forEach((link, index) => {
    link.classList.remove('nav-link-anim');
  });
});
