from flask import render_template, url_for, request, redirect, flash, Blueprint
# Forms

main = Blueprint('main', __name__)

# main page
@main.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


# start page 
@main.route("/start")
def start():
    return render_template("start.html")