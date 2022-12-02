class Button {

    #className;
    #text;
    #width;
    #height;
    #backgroundColor;

    constructor(props) {
        this.#className = props.className;
        this.#text = props.text;
        this.#width = props.width;
        this.#height = props.height;
        this.#backgroundColor = props.backgroundColor;
    }

    getClassName() {
        return this.#className;
    }

    setClassName(className) {
        this.#className = className;
    }

    getText() {
        return this.#text;
    }

    setText(text) {
        this.#text = text;
    }

    getWidth() {
        return this.#width;
    }

    setWidth(width) {
        this.#width = width;
    }

    getHeight() {
        return this.#height;
    }

    setHeight(height) {
        this.#height = height;
    }

    getBackgroundColor() {
        return this.#backgroundColor;
    }

    setBackgroundColor(backgroundColor) {
        this.#backgroundColor = backgroundColor;
    }

}