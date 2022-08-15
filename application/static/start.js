//when the image of the button is hovered on, it will enlarge button
document.addEventListener("DOMContentLoaded", function() {
    let button = document.querySelector('.button');

    button.addEventListener("mouseover", function() {
        button.style.color = "goldenrod";
    })
    button.addEventListener("mouseout", function() {
        button.style.color = "white";
    })
})