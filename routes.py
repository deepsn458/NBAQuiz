from models import User

# main page
@app.route("/", methods=["GET", "POST"])
def home():

    #if user is not logged in, return the home.html
    if request.method == 'GET':
        return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    # if registration is successful, redirect to login page
    if form.validate_on_submit():
        flash("Registration successful!","success")
        return redirect("/login")
    return render_template("register.html", form=form)
        

    

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # if login is succesful, redirect to home page via post
    if form.validate_on_submit():
        flash(f"Welcome back {form.username.data}", "success")
        return redirect("/")
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