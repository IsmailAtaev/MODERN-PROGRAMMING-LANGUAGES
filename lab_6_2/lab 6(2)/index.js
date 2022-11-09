const products = [];

const buttonService = new ButtonService();
const productService = new ProductService();

const catalog = new Catalog(products);

const basket = document.querySelector(".wrapper__basket");
const auth = document.querySelector(".wrapper__auth");

const basketBtn = buttonService.createButton(basket, new Button({
    className: "basket",
    text: "Корзина",
    width: 100,
    height: 40,
    backgroundColor: "#007cff"
}));

const authBtn = buttonService.createButton(auth, new Button({
    className: "auth",
    text: "Авторизация",
    width: 100,
    height: 40,
    backgroundColor: "#007cff"
}));

const blockProducts = document.querySelector(".wrapper__products")

for(let i = 0; i < 5; i++) {
    const product = productService.createProduct(blockProducts, new Product({
        image: "./assets/macbook-pro.png",
        title: "MacBook Pro",
        price: 2500,
        currency: CURRENCY.USD,
        button: new Button({
            className: "in_basket",
            text: "В корзину",
            width: 100,
            height: 40,
            backgroundColor: "#007cff"
        })
    }));

    catalog.addProduct(product);
}

//3D-images

const allProducts = document.querySelectorAll(".product img")

allProducts.forEach(product => {
    product.addEventListener("mousemove", startRotate)
    product.addEventListener("mouseout", stopRotate)
})

function startRotate(event) {
    const halfHeight = event.target.offsetHeight / 2
    event.target.style.transform = "rotateX(" + -(event.offsetY - halfHeight) / 5 + "deg)" +
        "rotateY(" + (event.offsetX - halfHeight) / 5 + "deg)"
}

function stopRotate(event) {
    event.target.style.transform = "rotate(0)"
}

function parallax(event) {
    this.querySelectorAll('.layer').forEach(element => {
        element.style.transform = `translate(${event.clientX/50}px, ${event.clientY/50}px)`;
    });
}

document.addEventListener('mousemove', parallax);
