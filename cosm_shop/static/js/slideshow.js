var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dot_v = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    dot_v[i].style.backgroundColor = "#C4C4C4";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  dot_v[slideIndex-1].style.backgroundColor = "#363941";
  setTimeout(showSlides, 5000); // Change image every 2 seconds
}