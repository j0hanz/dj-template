// Early theme detection - runs immediately
(function () {
  const storedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  // Set the theme based on stored preference or system preference
  if (storedTheme) {
    document.documentElement.setAttribute("data-bs-theme", storedTheme);
  } else if (prefersDark) {
    document.documentElement.setAttribute("data-bs-theme", "dark");
  }
})();

document.addEventListener("DOMContentLoaded", function () {
  const darkModeToggle = document.getElementById("darkModeToggle");
  const darkModeIcon = document.getElementById("darkModeIcon");
  const lightModeIcon = document.getElementById("lightModeIcon");

  // Check if the toggle button exists
  if (darkModeToggle) {
    updateIcons(document.documentElement.getAttribute("data-bs-theme"));
    // Toggle theme when button is clicked
    darkModeToggle.addEventListener("click", function () {
      const currentTheme =
        document.documentElement.getAttribute("data-bs-theme");
      const newTheme = currentTheme === "dark" ? "light" : "dark";
      setTheme(newTheme);
    });
  }

  // Function to set the theme and update local storage
  function setTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);
    updateIcons(theme);
  }

  // Function to update icons based on the current theme
  function updateIcons(theme) {
    if (theme === "dark") {
      darkModeIcon.classList.add("d-none");
      lightModeIcon.classList.remove("d-none");
    } else {
      darkModeIcon.classList.remove("d-none");
      lightModeIcon.classList.add("d-none");
    }
  }
});
