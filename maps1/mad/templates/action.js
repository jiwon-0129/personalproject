var cols = document.querySelectorAll(".choice");

for (var i = 0; i < cols.length; i++) {
  cols[i].addEventListener("onmouseover", onmouseover);
}
cols[1].style.color = "red";

function onmouseover(e) {
  window.alert(this.innerHTML);
}