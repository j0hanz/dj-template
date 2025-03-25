document.addEventListener("DOMContentLoaded", function () {
  // Get the button and span elements
  const countButton = document.getElementById("countButton");
  // Get the span element
  const countSpan = document.getElementById("count");
  // Initialize count
  let count = 0;

  // Add event listener to button
  countButton.addEventListener("click", function () {
    count++;
    countSpan.textContent = count;
  });
});
