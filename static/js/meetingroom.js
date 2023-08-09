document.addEventListener("DOMContentLoaded", function () {
  const items = document.querySelectorAll(".item");
  const classList = ["item", "item--medium", "item--large"];

  for (let i = 0; i < items.length; i += 3) {
    for (let j = 0; j < 3; j++) {
      const currentClass = classList[j];
      if (items[i + j]) {
        items[i + j].classList.add(currentClass); // Add class-a to 1st, class-b to 2nd, class-c to 3rd in each set of 3
      }
    }
  }
});
