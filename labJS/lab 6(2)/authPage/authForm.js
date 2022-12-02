const basket = document.querySelector(".wrapper__basket");
const main = document.querySelector(".wrapper__main");

const buttonService = new ButtonService();

const basketBtn = buttonService.createButton(basket, new Button({
    className: "basket",
    text: "Корзина",
    width: 100,
    height: 40,
    backgroundColor: "#007cff"
}));

const mainBtn = buttonService.createButton(main, new Button({
    className: "main",
    text: "Главная страница",
    width: 150,
    height: 40,
    backgroundColor: "#007cff"
}));

function parallax(event) {
    this.querySelectorAll('.layer').forEach(element => {
        element.style.transform = `translate(${event.clientX/50}px, ${event.clientY/50}px)`;
    });
}

document.addEventListener('mousemove', parallax);