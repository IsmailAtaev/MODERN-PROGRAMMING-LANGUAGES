const ballPosition = Math.random() * (90 - 10) + 10;

const ballNode = document.querySelector(".ball");
const field = document.querySelector(".field");
const board = document.querySelector(".board");

const fieldHeight = document
  .querySelector(".field")
  .getBoundingClientRect().height;

const zoneHeight = document
  .querySelector(".zone")
  .getBoundingClientRect().height;

ballNode.style.left = `${ballPosition}%`;

const ballCenter = [
  (ballNode.getBoundingClientRect().right +
    ballNode.getBoundingClientRect().x) /
    2,
  (ballNode.getBoundingClientRect().bottom +
    ballNode.getBoundingClientRect().y) /
    2,
];

function endpoints() {
  const diffX = ballCenter[0] - ballNode.getBoundingClientRect().left - 35;
  const diffY = ballNode.getBoundingClientRect().top - ballCenter[1];

  const coordinateX = 4 * diffX + ballCenter[0];
  const coordinateY = 4 * diffY;

  ballNode.style.transition = 0.2 + "s";
  ballNode.style.left = coordinateX + "px";
  ballNode.style.top = coordinateY + "px";

  if (
    board.getBoundingClientRect().left < coordinateX &&
    coordinateX < board.getBoundingClientRect().right &&
    board.getBoundingClientRect().top < coordinateY &&
    coordinateY < board.getBoundingClientRect().bottom
  )
    setTimeout(() => alert("Вы попали в мишень!"), 200);
}

ballNode.onmousedown = function (event) {
  let shiftX = event.clientX - ballNode.getBoundingClientRect().left;
  let shiftY = event.clientY - ballNode.getBoundingClientRect().top;

  let distance = null;

  document.body.append(ballNode);

  moveAt(event.pageX, event.pageY);

  function moveAt(pageX, pageY) {
    distance = Math.sqrt(
      Math.pow(pageX - ballCenter[0], 2) + Math.pow(pageY - ballCenter[1], 2)
    );

    if (
      fieldHeight > pageY - shiftY ||
      zoneHeight + fieldHeight - ballNode.width / 2 < pageY - shiftY ||
      pageX - shiftX > window.innerWidth - ballNode.width ||
      distance > 150
    )
      return null;

    ballNode.style.left = pageX - shiftX + "px";
    ballNode.style.top = pageY - shiftY + "px";
  }

  function onMouseMove(event) {
    moveAt(event.pageX, event.pageY);
  }

  document.addEventListener("mousemove", onMouseMove);

  ballNode.onmouseup = function () {
    endpoints(distance);

    document.removeEventListener("mousemove", onMouseMove);

    ballNode.onmouseup = null;
  };
};

ballNode.ondragstart = function () {
  return false;
};
