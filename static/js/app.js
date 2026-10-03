document.querySelectorAll(".coming-soon-button").forEach((button) => {
  button.addEventListener("click", () => {
    button.textContent = "Launching Soon";
  });
});

document.querySelectorAll(".task-list input").forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    const label = checkbox.closest("label");

    if (checkbox.checked) {
      label.style.opacity = "0.55";
      label.style.textDecoration = "line-through";
    } else {
      label.style.opacity = "1";
      label.style.textDecoration = "none";
    }
  });
});