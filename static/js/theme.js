// Early theme detection - runs immediately
(function () {
  const storedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

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

  if (darkModeToggle) {
    // Get current theme
    const currentTheme = document.documentElement.getAttribute("data-bs-theme");

    // Initialize icons based on current theme
    updateIcons(currentTheme);

    // Toggle theme when button is clicked
    darkModeToggle.addEventListener("click", function () {
      const currentTheme =
        document.documentElement.getAttribute("data-bs-theme");
      const newTheme = currentTheme === "dark" ? "light" : "dark";

      document.documentElement.setAttribute("data-bs-theme", newTheme);
      localStorage.setItem("theme", newTheme);
      updateIcons(newTheme);
    });
  }

  function updateIcons(theme) {
    // Update icons based on theme
    if (theme === "dark") {
      darkModeIcon.classList.add("d-none");
      lightModeIcon.classList.remove("d-none");
    } else {
      darkModeIcon.classList.remove("d-none");
      lightModeIcon.classList.add("d-none");
    }
  }
});
