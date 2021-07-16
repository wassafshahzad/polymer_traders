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

  attributeChangedCallback(name, oldValue, newValue) {
    console.table(oldValue);
  }
}

customElements.define("router-element", Router);
