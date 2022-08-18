# NBAQuiz
NBAQuiz is a web game made using JavaScript, the Flask microframework, and SQLite. Users answer as many NBA-related trivia questions as they can in 25 seconds.

## Video Demo: 

# Description
## Usage
visit http://www.quickfirenbaquiz.com 

## Gameplay
This section contains a short summary of the gameplay shown in the Video Demo.

Click "PLAY!" to navigate to the /start page. Once you click the "START!" button on the /start page, a question, two options, and a 25 second timer will be displayed. 

For each question click the option you think is correct and another question and set of options will be displayed. This will continue for 25 seconds or until all 50 questions have been answered

# Project Files
I used a package structure with blueprints instead of a single module to make the applicatio more organised, easier to debug, and to make it easy to expand the scope and features of my web application

## Blueprints
### Errors
Contains the routes that the user will be redirected to if they experience a 404, 403, or 500 error

### main
This contains the routes for the home page and the start page.

### quiz
This contains the routes for the main quiz page, the results page, and the summary page

### database
This contains the routes for loading in the questions and options to the database 
## Static
I separated the CSS and JS code from the HTML code to make the code cleaner and debugging easier

This contains the scss/css files, the Javascript files, and the images used

## Templates
This contains the templates used for all the routes, including the error handling routes

## others
### quiz database
The quiz database (quiz.db) consists of the questions, options, and responses table.
The questions and options are loaded in from the Questions.csv and the Options.csv files into the database by accessing the  /loadoptions and /loadquestions route.

I found it more convenient to enter the questions and options into excel and load them in as a csv file than to enter them directly into the database

# functionality
The main part of the web page (the quiz itself) works using /query route on the backend and the quiz.js file on the frontend.

The quiz page is loaded by accessing the /quiz route. Then asynchronous web requests using the Fetch API are made to retrieve each question/options from the database and to send each of the user's responses to the database.

## Javasript
The request for the first question is made using a GET request when the page loads. At the same time, a 25 second timer starts and is displayed on the screen. The 'correct' option is randomely assigned to either the left or right button and the 'wrong' option is assigned to the other button

Once the user selects an option, the question and the selected option is sent to the 'Responses' table through a POST request. Through the same request, another random set of questions and options is received.

The number of questions answered is also received. If all the questions are answered, the quiz is ended.

## Python
Upon receiving the GET or POST request, a question is chosen at random from the 'Questions' table. Two options linked to the question are retrieved from the 'Options' table. A random number between 0 and 1 is also chosen to determine which button the correct option should be assigned to. The question, options, random number, and the number of questions answered are returned as a dictionary.

When the user answers a question (a POST request is made), the question name and the option the user chose is parsed and added to the 'Responses' table in the database. Each response is marked as correct (1) or incorrect (0).

In the /results route, the number of correct and incorrect responses is tallied from the table.

To display each response in the /summary route, the 'Responses' table is loaded into a list where each row is loaded into a dictionary.








