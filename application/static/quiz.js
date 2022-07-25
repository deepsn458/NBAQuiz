/*
When quiz page is loaded 3 second timer starts

    A POST request is sent to obtai the question, options, and btn_id
    If btn_id == 0:
        correct option is assigned to left button
    Else
        correct option is assigned to right button
    60 second timer is started 
    When submit button is pressed 
        A POST request is sent containing the name and value of the option
        Another request for a question,options, and btn_id will be sent
*/


$(document).ready(function() {
    //sets default value of timers
    localStorage.setItem('60_second', 60);

    //when page is loaded, function to start timer and display questions is called
    shortTimer();
    displayQuestions();

    
})

//60 second timer
function shortTimer() {
    const timer_id = setInterval(function(){
        let time = localStorage.getItem('60_second');
        //stops timer after 60 seconds and sends a request to redirect to the results page
        if (time == 0) {
            clearInterval(timer_id);
            return;
        }
        //updates timer
        $("#timer").html(time);
        time--;
        localStorage.setItem('60_second',time);
    }, 1000);
}

//Sends a request 
function displayQuestions() {
   console.log('ye');

}