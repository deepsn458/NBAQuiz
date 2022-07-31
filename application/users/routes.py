from application.models import User, Options, Questions
from flask import render_template, url_for, request, redirect, flash, Blueprint
# Forms
from application.users.forms import RegistrationForm, LoginForm
from application import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import csv

users = Blueprint('users', __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    # if registration is successful, redirect to login page
    if form.validate_on_submit():
         #hashes password to store in database
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        #creates a new user
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()

        flash(f"Registration successful for {form.username.data}","success")
        return redirect(url_for('users.login'))
    return render_template("register.html", form=form)

@users.route ("/temp")
def temp():
    with open ("/mnt/c/Users/laz3r/documents/CS50/84109373/NBAQuiz/application/Questions.csv","r") as optionsfile:
        reader = csv.DictReader(optionsfile)
        for o in reader:
            o = Questions(question_name=o['Question Name'], displayed=o['displayed'])
            db.session.add(o)
            db.session.commit()
    return redirect(url_for('main.home'))

    

@users.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # if login is succesful, redirect to home page via post
    if form.validate_on_submit():
        # checks if username is correct
        user = User.query.filter_by(username=form.username.data).first()
        # checks if entered password matches user's actual password
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Welcome back {form.username.data}", "success")
            return redirect(url_for('main.home'))
        else:
            flash("Login Unsuccesful, check username and password")
    return render_template("login.html", form=form)


@users.route("/stats")
def stats():
    return render_template("stats.html")
    

@users.route("/logout")
def logout():
    logout_user()
    # returns user to login page
    return redirect(url_for('users.login'))