

function toggleVisibility(elementId) {
  var element = document.getElementById(elementId);
  if (element.style.display === 'none') {
      element.style.display = 'block';
  } else {
      element.style.display = 'none';
  }
}

// Add event listeners to the buttons
document.getElementById("unapproved-btn").addEventListener("click", function() {
  toggleVisibility("unapproved-rents");
});

document.getElementById("unverified-btn").addEventListener("click", function() {
  toggleVisibility("unverified-cars");
});
