var shoppingList = ["Laptop", "Charger", "Headset"];
console.log(shoppingList);
var yourList = [];

function inputItem() {
  var yourInput = prompt("Enter your item");
  if (yourInput) {
    yourList.push(yourInput);
    console.log(yourList);
  }
}
inputItem();

while ((UseInput = confirm("Do you want to continue"))) {
  inputItem();
}
