from application.models import Options, Questions
from flask import url_for, redirect, Blueprint
from application import db
import csv

database = Blueprint('database', __name__)

@database.route ("/loadquestions")
def loadquestions():
    with open ("/mnt/c/Users/laz3r/documents/CS50/84109373/NBAQuiz/application/Questions.csv","r") as questionsfile:
        reader = csv.DictReader(questionsfile)
        for question in reader:
            question = Questions(question_name=question['Question Name'], displayed=question['displayed'])
            db.session.add(question)
            db.session.commit()
    return redirect(url_for('main.home'))

@database.route ("/loadoptions")
def loadoptions():
    with open ("/mnt/c/Users/laz3r/documents/CS50/84109373/NBAQuiz/application/Options.csv","r") as optionsfile:
        reader = csv.DictReader(optionsfile)
        for option in reader:
            option = Options(option_name=option['option'], question_id=option['question_id'], correct_incorrect=option['correct_incorrect'])
            db.session.add(option)
            db.session.commit()
    return redirect(url_for('main.home'))
