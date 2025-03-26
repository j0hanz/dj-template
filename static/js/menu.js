document.addEventListener("DOMContentLoaded", function () {
  const menuButton = document.querySelector(
    '[data-bs-toggle="collapse"][data-bs-target="#navbarNav"]'
  );
  const menuIcon = menuButton.querySelector("svg:first-child");
  const closeIcon = menuButton.querySelector("svg:last-child");
  const navbarCollapse = document.getElementById("navbarNav");

  // Track if navbar is expanded
  let isNavbarExpanded = false;

  // Initial state
  menuIcon.classList.remove("d-none");
  closeIcon.classList.add("d-none");

  // Listen for Bootstrap collapse events
  navbarCollapse.addEventListener("show.bs.collapse", function () {
    menuIcon.classList.add("d-none");
    closeIcon.classList.remove("d-none");
    isNavbarExpanded = true;
  });

  navbarCollapse.addEventListener("hide.bs.collapse", function () {
    menuIcon.classList.remove("d-none");
    closeIcon.classList.add("d-none");
    isNavbarExpanded = false;
  });

  // Close navbar when clicking outside
  document.addEventListener("click", function (event) {
    // Only process if navbar is expanded
    if (!isNavbarExpanded) return;

    // Check if click is outside navbar and not on the toggle button
    const isClickInsideNavbar = navbarCollapse.contains(event.target);
    const isClickOnToggleButton = menuButton.contains(event.target);

    if (!isClickInsideNavbar && !isClickOnToggleButton) {
      // Get the Bootstrap collapse instance and hide it
      const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
      if (bsCollapse) {
        bsCollapse.hide();
      }
    }
  });
});
