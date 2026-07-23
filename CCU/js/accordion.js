// Neon Swan accordion — toggles the .active state; the panel that follows
// each button is shown/hidden via the .accordion.active + .panel CSS rule.
var accordions = document.getElementsByClassName('accordion');

for (var i = 0; i < accordions.length; i++) {
  accordions[i].addEventListener('click', function () {
    this.classList.toggle('active');
  });
}
