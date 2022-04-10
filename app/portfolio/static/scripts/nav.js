// Whole script is strict
"use strict";

var handburgerOpen = false;

function toggleState() {
    handburgerOpen = !handburgerOpen;
    updateStyle();
}

function updateStyle() {
    let handburgerContent = document.getElementById("handburgerContent");

    if (handburgerOpen) {
        handburgerContent.style.display = "flex";
        return
    }
    handburgerContent.style.display = "none";
}
