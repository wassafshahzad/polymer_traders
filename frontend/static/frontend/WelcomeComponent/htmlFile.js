class LoginPage extends HTMLElement{
    
    constructor(){
        super()
        this.attachShadow({mode: 'open'});
        const customPage = `
                        <div class="center">
                            <h2>Welcome,To Polymer Traders <span id = 'username' class='teal-text'></span> Wassaf </h2>
                        </div>
                    `
        let wrapper = this.htmlToElement(customPage)
        this.shadowRoot.append(wrapper)
    }

    htmlToElement(html) {
        var template = document.createElement('template');
        html = html.trim();
        template.innerHTML = html;
        return template.content.firstChild;
    }
    


}

customElements.define('login-page',LoginPage)