/* class Square {
  constructor(color, size) {
    this._color = color;
    this._size = size;
  }

  updateColor(color) {
    this._color = color;
  }

  updateSize(size) {
    this._size = size;
  }

  showMessAboutSize() {
    if (this._size < 10) return "Square is small!";
    return "Square is big!";
  }

  showInfAboutSquare() {
    return `Color is ${this._color}, size: ${this._size}`;
  }
}

const square1 = new Square("red", 8);
const square2 = new Square("yellow", 12);

console.log(square1.showMessAboutSize());
console.log(square2.showMessAboutSize()); */

/* ---------------------------------------------------- */

/* class Circle {
  constructor(radius) {
    this._radius = radius;
  }

  changeRadius(radius) {
    rhis._radius = radius;
  }

  showInfAboutСircle() {
    return `Radius is ${this._radius}.`;
  }
}

class CircleWithColor extends Circle {
  constructor(radius, color) {
    super(radius);
    this._color = color;
  }

  changeColor(color) {
    rhis._color = color;
  }

  showInfAboutСircle() {
    return `Radius is ${this._radius}, color: ${this._color}`;
  }
}

const circle1 = new Circle(14);
const circle2 = new CircleWithColor(14, "green");

console.log(circle1.showInfAboutСircle());
console.log(circle2.showInfAboutСircle()); */

/* ---------------------------------------------------- */

/* class Triangle {
  constructor(a, b, c, linesAmount) {
    if (a + b < c || a + c < b || c + b < a) return "Triangle doesn't exist!";

    this._a = a;
    this._b = b;
    this._c = c;
    this._linesAmount = linesAmount;
  }

  changeLinesAmount(linesAmount) {
    this._linesAmount = linesAmount;
  }

  showInfAboutTriangle() {
    return `Side a: ${this._a}, Side b: ${this._b}, Side c: ${this._c}, lines amount: ${this._linesAmount}`;
  }
}

const triangle1 = new Triangle(3, 4, 5, 1);
const triangle2 = new Triangle(6, 7, 10, 3);

console.log(triangle1.showInfAboutTriangle());
console.log(triangle2.showInfAboutTriangle()); */
