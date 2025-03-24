document.addEventListener("DOMContentLoaded", function () {
  const countButton = document.getElementById("countButton");
  const countSpan = document.getElementById("count");
  let count = 0;

  countButton.addEventListener("click", function () {
    count++;
    countSpan.textContent = count;
  });
});
