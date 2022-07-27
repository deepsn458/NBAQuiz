from flask import render_template, url_for, request, redirect, flash, Blueprint
from application.models import Questions, Responses
from application import db
# Forms

main = Blueprint('main', __name__)

# main page
@main.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


# start page 
@main.route("/start")
def start():
    # Clears the responses table for the next quiz
    db.session.query(Responses).delete()
    db.session.commit()

    # sets the displayed values for all the questions back to false
    for i in range(1,21):
        question = Questions.query.get(i)
        question.displayed = 0
        db.session.commit()
    return render_template("start.html")