let container = document.getElementsByClassName("container")[0];
for(let i = 0; i<8; i++){
  let odd = i % 2==0? 0: 1;
  let subContainer = document.createElement("div");
  subContainer.setAttribute("class","row");
  for(let j = 0; j<8; j++){
    let myTile = document.createElement("div");
    if((j+odd)%2==0) myTile.style.backgroundColor="black"
    myTile.setAttribute("class","col tile");
    subContainer.appendChild(myTile);
  }
  container.appendChild(subContainer);
}
