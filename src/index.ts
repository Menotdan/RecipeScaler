function scaleClicked(event: MouseEvent) {
    console.log("weeee");
}

var scaleButton = document.getElementById("scale-button");
if (scaleButton == null) {
    console.error("Scale button not found.");
}
else {
    scaleButton.onclick = scaleClicked;
}