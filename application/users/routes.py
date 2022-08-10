from application.models import Options
from flask import render_template, url_for, request, redirect, flash, Blueprint
from application import db
import csv

users = Blueprint('users', __name__)

@users.route ("/temp")
def temp():
    with open ("/mnt/c/Users/laz3r/documents/CS50/84109373/NBAQuiz/application/Options.csv","r") as optionsfile:
        reader = csv.DictReader(optionsfile)
        for o in reader:
            o = Options(option_name=o['option'], correct_incorrect=o['correct_incorrect'], question_id=o['question_id'])
            db.session.add(o)
            db.session.commit()
    return redirect(url_for('main.home'))