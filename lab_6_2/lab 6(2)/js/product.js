class Product {

    #image;
    #title;
    #price;
    #currency;
    #button;
    
    constructor(props) {
        this.#image = props.image;
        this.#title = props.title;
        this.#price = props.price;
        this.#currency = props.currency;
        this.#button = props.button;
    }

    getImage() {
        return this.#image;
    }

    setImage(image) {
        this.#image = image;
    }

    getTitle() {
        return this.#title;
    }

    setTitle(title) {
        this.#title = title;
    }

    getPrice() {
        return this.#price;
    }

    setPrice(price) {
        this.#price = price;
    }

    getCurrency() {
        return this.#currency;
    }

    setCurrency(currency) {
        this.#currency = currency;
    }

    getButton() {
        return this.#button;
    }

    setButton(button) {
        this.#button = button;
    }
    
}