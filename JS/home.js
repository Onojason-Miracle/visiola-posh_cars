document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.animated-text');
    elements.forEach((el, index) => {
        el.style.animationDelay = `${index * 2}s`; // Delay each element by 0.5s
    });
});