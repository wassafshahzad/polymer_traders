class Router extends HTMLElement {
  static get observedAttributes() {
    return ["page"];
  }

  constructor() {
    super();
    let divWrapper = document.createElement("div");
    let slotWrapper = document.createElement("slot");
    slotWrapper.setAttribute("name", "my-pages");
    divWrapper.append(slotWrapper);
    this.attachShadow({ mode: "open" });
    this.shadowRoot.append(divWrapper);
    let style = document.createElement("style");
    style.innerHTML = ".hide { display: none; }";
    this.shadowRoot.appendChild(style);
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (name == "page" && oldValue) {
      this.handlePageChange(oldValue, newValue);
    }
  }

  handlePageChange(oldValue, newValue) {
    document.getElementById(oldValue).classList.add("hide");
    document.getElementById(newValue).classList.remove("hide");
  }
}

function changePage(newPage) {
  document
    .getElementsByTagName("router-element")[0]
    .setAttribute("page", newPage);
}

customElements.define("router-element", Router);
