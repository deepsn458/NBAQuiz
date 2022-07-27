$(document).ready(function() {
    //sets default value of timers
    localStorage.setItem('60_second', 60);

    //when page is loaded, function to start timer and display questions is called
    shortTimer();
    displayQuestions();

    //When the button is clicked, Function to send the response to database and retrieve a new question is called
   $("button").click(function(){
    sendResponse(this.id);
    return false;
   })  
})

//60 second timer
function shortTimer() {
    const timer_id = setInterval(function(){
        let time = localStorage.getItem('60_second');
        //stops timer after 60 seconds and sends a request to redirect to the results page
        if (time == 0) {
            clearInterval(timer_id);
            $("#timer").html("Time is Up!")
            finishQuiz();
            return;
        }
        //updates timer
        $("#timer").html(time);
        time--;
        localStorage.setItem('60_second',time);
    }, 1000);
}

//Sends a request to retrieve a question
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

//Sends request to redirect to results page after timer runs out
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