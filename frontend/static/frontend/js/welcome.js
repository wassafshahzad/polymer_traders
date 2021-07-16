function setUserName() {
  let element = document.getElementById("username");
  element.innerHTML = getItemFromLocalStorage("username");
}

function clickButton() {
  let a = document.getElementById("route");
  a.setAttribute("page", "change");
}

document.addEventListener("DOMContentLoaded", function () {
  setUserName();
});
