class ProductService {

    #buttonService = new ButtonService();

    createProduct(parent, product) {
        this.product = document.createElement("div");

        this.product.className = "product";
        this.product.innerHTML = 
                    `<img src=${product.getImage() ?? "./assets/default.png"}></img>
                     <h2>${product.getTitle() ?? "Без названия"}</h2>
                     <h3>${product.getPrice() ?? "Цена не указана"} ${product.getCurrency() ?? "$"}</h3>`;

        this.#buttonService.createButton(this.product, new Button({
            className: product.getButton().getClassName(),
            text: product.getButton().getText(),
            width: product.getButton().getWidth(),
            height: product.getButton().getHeight(),
            backgroundColor: product.getButton().getBackgroundColor()
        }));
        
        parent.append(this.product);

        return this.product;
    }

    deleteProduct(product) {
        product.parentNode.removeChild(product);
    }

}