var Cat = /** @class */ (function () {
    function Cat(name, voice, age, moving) {
        this.name = name;
        this.voice = voice;
        this.age = age;
        this.moving = moving;
    }
    Cat.prototype.info = function () {
        return "Cat called ".concat(this.name, ", age: ").concat(this.age, ", ").concat(this.voice ? "can make voices" : "can't make voices", ", it can ").concat(this.moving);
    };
    return Cat;
}());
var Bird = /** @class */ (function () {
    function Bird(name, voice, canSing, moving) {
        this.name = name;
        this.voice = voice;
        this.canSing = canSing;
        this.moving = moving;
    }
    Bird.prototype.info = function () {
        return "Bird called ".concat(this.name, ", ").concat(this.canSing ? "can sing" : "can't sing", ", ").concat(this.voice ? "can make voices" : "can't make voices", ", it can ").concat(this.moving);
    };
    return Bird;
}());
var Fish = /** @class */ (function () {
    function Fish(name, voice, depth, moving) {
        this.name = name;
        this.voice = voice;
        this.depth = depth;
        this.moving = moving;
    }
    Fish.prototype.info = function () {
        return "Fish called ".concat(this.name, ", it swims in depth: ").concat(this.depth, ", ").concat(this.voice ? "can make voices" : "can't make voices", ", it can ").concat(this.moving);
    };
    return Fish;
}());
var cat = new Cat("Barsik", true, 5, "walk");
var bird = new Bird("Kesha", true, true, "fly");
var fish = new Fish("Gold", false, 100, "swim");
console.log(cat.info());
console.log(bird.info());
console.log(fish.info());
