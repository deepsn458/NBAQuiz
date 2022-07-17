from application.models import User, Questions, Options, Responses
from flask import render_template, url_for, request, redirect, flash
# Forms
from application.forms import RegistrationForm, LoginForm
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import csv
import random
from sqlalchemy.sql import func

# main page
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
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
        return redirect("/login")
    return render_template("register.html", form=form)

@app.route ("/temp")
def temp():
    with open ("Options.csv","r") as optionsfile:
        reader = csv.DictReader(optionsfile)
        for o in reader:
            if o['correct'] == 'Correct':
                o = Options(option_name=o['option'], correct_incorrect=True, question_id=o['question_id'])
            else:
                o = Options(option_name=o['option'], question_id=o['question_id']) 
            db.session.add(o)
            db.session.commit()
    return render_template("home.html")

    

@app.route("/login", methods=["GET", "POST"])
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
            return redirect("/")
        else:
            flash("Login Unsuccesful, check username and password")
    return render_template("login.html", form=form)

    return render_template("login.html")
# start page 
@app.route("/start")
def start():
    return render_template("start.html")

# actual quiz page
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    # Retrieve a question at random from the 'Questions' table
    index = random.randint(0,20)
    q = Questions.query.filter_by(id=index, displayed=False).first()
    # the same question won't be displayed again in the current quiz
    q.displayed = True

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
        return redirect("/results")
    else:
        return render_template("quiz.html", btn_id=btn_id, o1=o1, o2=o2, q=q)

@app.route("/results")
def results():
    # displays the number of correct and incorrect answers
    total_correct = Responses.query.filter_by(correct_incorrect=True).count()
    total_incorrect = Responses.query.filter_by(correct_incorrect=False).count()
    # Clears the responses table for the next quiz
    db.session.query(Responses).delete()
    db.session.commit()
    return render_template("results.html", total_correct=total_correct, total_incorrect=total_incorrect)

    # sets the displayed values for all the questions back to false
   # for i in range(20):
        #question = Questions.query.get(i)
        #question.displayed = False
       # db.session.commit()

@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")
    

@app.route("/logout")
def logout():
    logout_user()
    # returns user to login page
    return redirect("/login")
