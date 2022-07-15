from application.models import User
from flask import render_template, url_for, request, redirect, flash
# Forms
from application.forms import RegistrationForm, LoginForm
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
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
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/results")
def results():
    return render_template("results.html")

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