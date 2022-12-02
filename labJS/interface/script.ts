interface Animal {
  moving: string;
  voice: boolean;
  name: string;
  info: () => string;
}

class Cat implements Animal {
  moving: string;
  voice: boolean;
  age: number;
  name: string;

  constructor(name: string, voice: boolean, age: number, moving: string) {
    this.name = name;
    this.voice = voice;
    this.age = age;
    this.moving = moving;
  }

  info() {
    return `Cat called ${this.name}, age: ${this.age}, ${
      this.voice ? `can make voices` : `can't make voices`
    }, it can ${this.moving}`;
  }
}

class Bird implements Animal {
  moving: string;
  voice: boolean;
  name: string;
  canSing: boolean;

  constructor(name: string, voice: boolean, canSing: boolean, moving: string) {
    this.name = name;
    this.voice = voice;
    this.canSing = canSing;
    this.moving = moving;
  }

  info() {
    return `Bird called ${this.name}, ${
      this.canSing ? `can sing` : `can't sing`
    }, ${this.voice ? `can make voices` : `can't make voices`}, it can ${
      this.moving
    }`;
  }
}

class Fish implements Animal {
  moving: string;
  voice: boolean;
  name: string;
  depth: number;

  constructor(name: string, voice: boolean, depth: number, moving: string) {
    this.name = name;
    this.voice = voice;
    this.depth = depth;
    this.moving = moving;
  }

  info() {
    return `Fish called ${this.name}, it swims in depth: ${this.depth}, ${
      this.voice ? `can make voices` : `can't make voices`
    }, it can ${this.moving}`;
  }
}

const cat = new Cat("Barsik", true, 5, "walk");
const bird = new Bird("Kesha", true, true, "fly");
const fish = new Fish("Gold", false, 100, "swim");

console.log(cat.info());
console.log(bird.info());
console.log(fish.info());