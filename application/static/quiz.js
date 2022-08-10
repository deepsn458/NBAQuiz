$(document).ready(function() {

    document.querySelector('.title').style.animationPlayState = 'paused';

    //when the buttons are hovered on, the inner text will change color to red
    let buttons = document.querySelectorAll('button');
    buttons.forEach(function(button) {
        button.addEventListener("mouseover", function() {
            button.style.color = "red";
        })     
    })
    buttons.forEach(function(button) {
        button.addEventListener("mouseout", function() {
            button.style.color = "black";
        })
    })
    
    //sets default value of timers
    localStorage.setItem('25_second', 25);

    //when page is loaded, function to start timer and display questions is called
    shortTimer();
    displayQuestions();

    //When the button is clicked, Function to send the response to database and retrieve a new question is called
   $("button").click(function(){
    sendResponse(this.id);
    return false;
   })  
})

//25 second timer
function shortTimer() {
    const timer_id = setInterval(function(){
        let time = localStorage.getItem('25_second');
        //stops timer after 25 seconds and sends a request to redirect to the results page
        if (time == 0) {
            clearInterval(timer_id);
            $("#timer").html("Time is Up!")
            finishQuiz();
            return;
        }

        //timer will turn red and bob in the last 5 seconds
        if (time <= 5) {
            document.querySelector('.title').style.color = "red";
            document.querySelector('.title').style.animationPlayState = 'running';
        }
        //updates timer
        $("#timer").html(time);
        time--;
        localStorage.setItem('25_second',time);
    }, 1000);
}

//Sends a request to retrieve a list of all the questions
function displayQuestions() {

   //sends request to quiz route
   fetch(`${window.origin}/query`)
 
    .then(function(response){
        if (response.status !== 200) {
            console.log(`Response status was not 200: ${response.status}`);
            return;
        }

        response.json().then(function (data) {
            //gets the question name 
            $("#question").html(data['question']);

            if (data['id'] == 0) {
                // Assigns the correct option to right button if the random number is 0
                $("#right").val(data['correct']);
                $("#right").html(data['correct']);

                $("#left").val(data['wrong']);
                $("#left").html(data['wrong']);
            }
            else {
                // Assigns the correct option to left button if the random number is 1
                $("#right").val(data['wrong']);
                $("#right").html(data['wrong']);
                $("#left").val(data['correct']);
                $("#left").html(data['correct']);
            }
        })
    })
}

// sends the user's response to the responses database and gets back a new question
function sendResponse(id) {
    console.log($(`#${id}`).val());
    fetch(`${window.origin}/query`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        //sends the question and the user's answer to the database
        body: JSON.stringify({
            question: $("#question").html(),
            answer: $(`#${id}`).val()
        })
    })

    .then(function(response){
        if(response.status !== 200) {
            console.log(`Response status was not 200: ${response.status}`);
            return;
        }

        response.json()
        .then(function(data){
            //if all questions have been answered, user is redirected to results page
            if (data['response_count'] == data['question_count']) {
                console.log("yuh");
                finishQuiz();
                return;
            }
            //gets the question name 
            $("#question").html(data['question']);

            if (data['id'] == 0) {
                // Assigns the correct option to right button if the random number is 0
                $("#right").val(data['correct']);
                $("#right").html(data['correct']);

                $("#left").val(data['wrong']);
                $("#left").html(data['wrong']);
            }
            else {
                // Assigns the correct option to left button if the random number is 1
                $("#right").val(data['wrong']);
                $("#right").html(data['wrong']);
                $("#left").val(data['correct']);
                $("#left").html(data['correct']);
            }
        })
    })
}

//Sends request to redirect to results page after timer runs out or if all questions have been answered
function finishQuiz() {
    fetch(`${window.origin}/quiz/results`)
    .then(function(response){
        if(response.status !== 200) {
            console.log(`Response status was not 200: ${response.status}`);
            return;
        }
        //redirects to the results route
        window.location = response.url;
    })
}