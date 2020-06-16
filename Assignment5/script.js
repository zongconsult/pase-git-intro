var PostID = document.getElementById("itemSelected").innerHTML;
var PostID1 = document.getElementById("item2").innerHTML;
var PostID2 = document.getElementById("item3").innerHTML;

// first Item
function selectItem() {
  // console.log(PostID);
}

function addSelected() {
  var newLi = document.createElement("li");
  newLi.appendChild(document.createTextNode(PostID));
  document.getElementById("userSelected").appendChild(newLi);
}

// Second Item
function selectItem1() {
  console.log(PostID1);
}

function addSelected1() {
  var newLi = document.createElement("li");
  newLi.appendChild(document.createTextNode(PostID1));
  document.getElementById("userSelected").appendChild(newLi);
}

// third Item
function selectItem2() {
  // console.log(PostID2);
}

function addSelected2() {
  var newLi = document.createElement("li");
  newLi.appendChild(document.createTextNode(PostID2));
  document.getElementById("userSelected").appendChild(newLi);
}

// Add the User Input

function addUserInput() {
  var newLi = document.createElement("li");

  //newLi = document.getElementById(inputItem).value;
  var userInput = document.getElementById("inputItem").value;
  newLi.appendChild(document.createTextNode(userInput));
  // display value on console
  console.log(newLi);

  document.getElementById("userSelected").appendChild(newLi);
}
