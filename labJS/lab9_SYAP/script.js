// const obj = {
//   yes: 0,
//   no: 0,
// };

// for (let i = 0; i < 6; i++) {
//   const answer = confirm(`yes:, ${obj.yes}, no:, ${obj.no}`);
//   answer ? obj.yes++ : obj.no++;
// }

// alert(`Разница между yes и no: ${obj.yes - obj.no}`);

function a(a) {
  return function (b) {
    return function (c) {
      return a * b * c;
    };
  };
}

alert(`${a(3)(4)(6)}`);

/* const obj = {
  x: 0,
  y: 0,
};

for (let i = 0; i < 3; i++) {
  const response = prompt("Input your coordinates: ");

  switch (response) {
    case "left": {
      obj.x -= 10;
      break;
    }
    case "right": {
      obj.x += 10;
      break;
    }
    case "up": {
      obj.y += 10;
      break;
    }
    case "down": {
      obj.y -= 10;
      break;
    }
    default: {
      alert("incorrect input");
    }
  }
}

alert(`x: ${obj.x}, y: ${obj.y}`); */
