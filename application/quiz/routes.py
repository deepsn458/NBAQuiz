from flask import Blueprint, render_template, url_for, request, redirect, jsonify
from application.models import Questions, Options, Responses
from application import db
import random
from sqlalchemy.sql import func

Quiz = Blueprint('Quiz', __name__)

# actual quiz page
@Quiz.route("/quiz", methods=["GET", "POST"])
def quiz():
    # Retrieve a question at random from the 'Questions' table
    index = random.randint(1,20)
    q = Questions.query.filter_by(id=index, displayed=0).first()

    q.displayed = 1
    db.session.commit()

    # Selects the correct option for the question
    o1 = Options.query.filter_by(question_id=index, correct_incorrect=True).first()

    # Randomely selects an incorrect option for the questiom
    o2 =  Options.query.filter_by(question_id=index, correct_incorrect=False).order_by(func.random()).limit(1).first()
    btn_id = random.randint(0,1)

    # Updates 'Responses' table when option is chosen
    if request.method == "POST":
        option = Options.query.filter_by(id=request.form.get("response")).first()
        response = Responses(question_id=q.id, option_id=option.id, correct_incorrect=option.correct_incorrect)
        db.session.add(response)
        db.session.commit()

        # return the results page when timer runs out
        return redirect(url_for('Quiz.results'))
    else:
        return render_template("quiz.html", btn_id=btn_id, o1=o1, o2=o2, q=q)

@Quiz.route("/quiz/results")
def results():
    # displays the number of correct and incorrect answers
    total_correct = Responses.query.filter_by(correct_incorrect=True).count()
    total_incorrect = Responses.query.filter_by(correct_incorrect=False).count()
    # Clears the responses table for the next quiz
    db.session.query(Responses).delete()
    db.session.commit()


     # sets the displayed values for all the questions back to false
    for i in range(1,21):
        question = Questions.query.get(i)
        question.displayed = 0
        db.session.commit()
    return render_template("results.html", total_correct=total_correct, total_incorrect=total_incorrect)


@Quiz.route("/quiz/summary")
def summary():
    return render_template("summary.html")