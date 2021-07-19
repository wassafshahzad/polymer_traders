function setUserName() {
  let element = document.getElementById("username");
  element.innerHTML = getItemFromLocalStorage("username");
}

function clickButton() {
  changePage("change");
}

document.addEventListener("DOMContentLoaded", function () {
  setUserName();
});
