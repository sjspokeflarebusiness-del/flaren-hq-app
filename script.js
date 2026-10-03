const accessKey = "Flaren SJS";

const lockScreen = document.getElementById("lockScreen");
const dashboard = document.getElementById("dashboard");
const unlockForm = document.getElementById("unlockForm");
const passwordInput = document.getElementById("password");
const errorMessage = document.getElementById("errorMessage");
const lockButton = document.getElementById("lockButton");

function unlockDashboard() {
  lockScreen.classList.add("is-hidden");
  dashboard.hidden = false;
  sessionStorage.setItem("flarenControlUnlocked", "true");
  passwordInput.value = "";
}

function lockDashboard() {
  dashboard.hidden = true;
  lockScreen.classList.remove("is-hidden");
  sessionStorage.removeItem("flarenControlUnlocked");
  errorMessage.textContent = "";
  passwordInput.focus();
}

unlockForm.addEventListener("submit", (event) => {
  event.preventDefault();

  if (passwordInput.value === accessKey) {
    unlockDashboard();
  } else {
    errorMessage.textContent = "Incorrect access key. Try again.";
    passwordInput.value = "";
    passwordInput.focus();
  }
});

lockButton.addEventListener("click", lockDashboard);

if (sessionStorage.getItem("flarenControlUnlocked") === "true") {
  unlockDashboard();
}