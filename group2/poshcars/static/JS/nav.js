document.addEventListener("DOMContentLoaded", function () {
    const iconBtn = document.querySelector(".iconBtn");
    const navbarLinks = document.querySelector(".navbar-links");
    const navBtn = document.querySelector(".nav-btn");

    iconBtn.addEventListener("click", function () {
      navbarLinks.classList.toggle("active");
      navBtn.classList.toggle("active");
    });
  });