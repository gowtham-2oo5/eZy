function displayOptions(value) {
  if (value === "radio") {
    const options = document.querySelector(".option");
    options.style.display = "block";
  }
}

function hideAlert() {
  const alert = document.querySelector(".alert");
  alert.style.display = "none";
}
