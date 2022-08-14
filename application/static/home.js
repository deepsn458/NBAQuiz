
document.addEventListener("DOMContentLoaded", function() {

    //when document loads, quiz title starts to bob (change size)
    document.querySelector('h1').style.animationPlayState = 'running';
    //when the image of the button is hovered on, it will enlarge to 300px
    let button = document.querySelector('.button');
    button.addEventListener("mouseover", function() {
        button.style.color = "goldenrod";
    })
    button.addEventListener("mouseout", function() {
        button.style.color = "white";
    })
})
