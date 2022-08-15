document.addEventListener("DOMContentLoaded", function() {
    let buttons = document.querySelectorAll('button');

    buttons.forEach(function(button) {
        button.addEventListener("mouseover", function() {
            button.style.color = "goldenrod";
        })
        
    })
    buttons.forEach(function(button) {
        button.addEventListener("mouseout", function() {
            button.style.color = "white";
        })
    })
})