class Catalog {

    #catalog;

    constructor(catalog) {
        this.#catalog = catalog;
    }

    addProduct(product) {
        this.#catalog.push(product);
    }

    deleteProduct(number) {
        this.#catalog.splice(number - 1, 1);
    }

}