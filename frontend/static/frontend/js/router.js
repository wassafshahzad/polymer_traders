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
  }

  connectedCallback() {
    this.shadowRoot.firstElementChild.addEventListener(
      "page-change",
      (event) => {
        console.log("caufght");
      }
    );
    console.log(this.getAttribute("page"));
  }
}

customElements.define("router-element", Router);
