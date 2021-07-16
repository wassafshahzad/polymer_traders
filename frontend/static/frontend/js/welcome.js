function setUserName() {
  let element = document.getElementById("username");
  element.innerHTML = getItemFromLocalStorage("username");
}

document.addEventListener("DOMContentLoaded", function () {
  setUserName();
});
