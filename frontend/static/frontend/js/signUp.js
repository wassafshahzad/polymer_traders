let obj = {};
let validKeyLength = 3;
let message = ["Logged In", "Signed Up"];
const PAGE_NAMES = { signUpUser: "signUpUser", loginUser: "loginUser" };
let key = PAGE_NAMES.signUpUser;

function onChangeInput({ target: { value, name } }) {
  obj[name] = value;
  validFrom();
}
function validFrom() {
  if (
    Object.keys(obj).length < validKeyLength ||
    !document.getElementsByClassName("invalid")
  ) {
    document.getElementById("submit").disabled = true;
  } else document.getElementById("submit").disabled = false;
}

function submitForm(event) {
  event.preventDefault();
  if (!document.getElementsByClassName("invalid").length > 0) {
    authService[key](JSON.stringify(obj)).then((resp) => {
      {
        setItemToLocalStorage("Token", resp["key"]);
        setItemToLocalStorage("username", obj["username"]);
        if (resp) {
          alert(`User ${message[validKeyLength - 2]}`);
          window.location.href = "/";
        }
      }
    });
  }
}

function onSwitchPage({ target }, id) {
  validKeyLength = validKeyLength === 3 ? 2 : 3;
  key = getKey(key);
  hideOrShowElement(document.getElementById("email"));
  showSubText(target, id);
  changeTitle();
  clearInputs();
}

function getKey(previousKey) {
  return key == PAGE_NAMES.signUpUser
    ? PAGE_NAMES.loginUser
    : PAGE_NAMES.signUpUser;
}

function changeTitle() {
  let nodes = Array.from(document.getElementsByClassName("title"));
  nodes.map((x) => hideOrShowElement(x));
}

function hideOrShowElement(element) {
  if (element.classList.contains("hide")) {
    element.classList.remove("hide");
  } else {
    element.classList.add("hide");
  }
}

function showSubText(target, id) {
  hideOrShowElement(target);
  hideOrShowElement(document.getElementById(id));
}

function clearInputs() {
  obj = {};
  Array.from(document.getElementsByTagName("input")).map((x) => {
    x.value = "";
    x.classList.remove("invalid");
  });
}
