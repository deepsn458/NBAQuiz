from flask import Blueprint, render_template, url_for, request, redirect, jsonify, make_response
from application.models import Questions, Options, Responses
from application import db
import random
from sqlalchemy.sql import func

Quiz = Blueprint('Quiz', __name__)

# actual quiz page 
@Quiz.route("/quiz", methods=["GET", "POST"])
def quiz():
    # if page is accessed from start page, return the quiz page
    if request.method == "GET":
        return render_template("quiz.html")

    # if timer runs out, return the results page
    else:
        return redirect(url_for('Quiz.results'))


# Asynchronous queries for questions and options after button is clicked
@Quiz.route("/query", methods=["GET", "POST"])
def query():
    #number of questions
    question_count = Questions.query.count()
    #sends question to quiz page and retrieves the option
    if request.method == "POST":
        response = request.get_json()
        print(response['answer'])
        print(response['question'])
        
        #updates the 'Responses' table with the question and option
        q = Questions.query.filter_by(question_name=response['question']).first()
        o = Options.query.filter_by(option_name=response['answer']).first()
        resp = Responses(question_id=q.id, option_id=o.id, correct_incorrect=o.correct_incorrect)
        db.session.add(resp)
        db.session.commit()
    
    # int to check if all questions have been answered already
    response_count = 0

    # Finds a question that has not yet been displayed
    index = random.randint(1,question_count)
    q = Questions.query.get(index)
    while q.displayed == 1:
        index = random.randint(1,question_count)
        q = Questions.query.get(index)
        response_count +=1
        # if all questions are answered, redirects to the results with JS
        if (response_count == question_count):
            req = {
                "response_count": response_count,
                "question_count": question_count
            }
            print(response_count)
            response = make_response(jsonify(req), 200)
            return response
    q.displayed = 1
    db.session.commit()

    # Randomely selects an incorrect option for the questiom
    o2 =  Options.query.filter_by(question_id=index, correct_incorrect=0).order_by(func.random()).first()
    # Selects the correct option for the question
    o1 = Options.query.filter_by(question_id=index, correct_incorrect=1).first()
    # random number to decide which button correct answer should be on
    btn_id = random.randint(0,1)
    req = {
        "question": q.question_name,
        "correct": o1.option_name,
        "wrong":o2.option_name,
        "id":btn_id,
        "response_count": response_count,
        "question_count": question_count
    }
    response = make_response(jsonify(req), 200)
    return response
    

   
@Quiz.route("/quiz/results")
def results():
    # displays the number of correct and incorrect answers
    total_correct = Responses.query.filter_by(correct_incorrect=1).count()
    total_incorrect = Responses.query.filter_by(correct_incorrect=0).count()

    return render_template("results.html", total_correct=total_correct, total_incorrect=total_incorrect)

@Quiz.route("/quiz/summary")
def summary():
    #Table:
    #C1: Index
    #C2: Question
    #C3: Your response
    #C4: Current Response

    #Stores 'Responses' table in a list
    table = []

    #Each row in 'Responses' is stored in a dictionary
    row_count = Responses.query.count() + 1
    for i in range(1,row_count):
        response = Responses.query.get(i)
        row = {}
        row['index'] = i
        row['question'] = Questions.query.get(response.question_id).question_name
        row['user_answer'] = Options.query.get(response.option_id).option_name
        row['correct_answer'] = Options.query.filter_by(question_id=response.question_id, correct_incorrect=1).first().option_name
        table.append(row)
    return render_template("summary.html",table=table)