from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from functools import wraps
from cs50 import SQL
import re

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///LearnEasy.db")


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/Login")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return render_template("Main.html")


@app.route("/Login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        # just for your reference we are printing in the terminal
        print("form values = ", dict(request.form))
        # whatever user has typed we are storing it in a variable
        username = request.form.get("Username")
        if len(username) == 0:
            return render_template("Login.html", mssg="Please enter username")
        # whatever password is typed we are storing it in a variable
        password = request.form.get("password")
        if len(password) == 0:
            return render_template("Login.html", mssg="Please enter password")
        # db quesry for selecting password where username(in db) is same as username typed by user
        # then storing it in a variable
        VerifyUser = db.execute(
            "SELECT ID,Password from People WHERE Username = ?", username)
        # just for your reference
        print(VerifyUser)
        # if there is no such username found
        if len(VerifyUser) == 0:
            return render_template("Login.html", mssg="Username doesn't exist")
        else:
            # store the password fetched from db in a variable
            # we are storing the password first in variable because originally it is a list
            dbpass = VerifyUser[0]["Password"]
            id = VerifyUser[0]["ID"]
            # password should match the value in the variable
            if password == dbpass:
                session['user_id'] = id
                return redirect("/Homepage")
            else:
                return render_template("Login.html", mssg="Password is wrong")
# this line if for the requesth method get
    return render_template("Login.html")


@app.route("/SignUp", methods=["GET", "POST"])
def SignUp():
    if request.method == "POST":
        print(dict(request.form))
        data = request.form
        username = data.get("Username")
        standard = data.get("standard")
        firstname = data.get("Firstname")
        email = data.get("email")
        profession = data.get("profession")
        lastname = data.get("lastname")
        password = data.get("password")
        confirm = data.get("confirm")
        age = data.get("age")
        mssg = ''
        for i in data:
            print(i)
            if len(data.get(i)) == 0:
                mssg = f"Please enter the value for {i}."
                return render_template("SignUp.html", mssg=mssg)

        if int(age) < 6:
            mssg = "Sorry you are not eligible"

        if re.search(r'[!@#$%^&*(),.?":{}|<>]', firstname):
            mssg = "Please enter valid name"

        if re.search(r'[!@#$%^&*(),.?":{}|<>]', lastname):
            mssg = "Please enter valid last name"

        # Check if the password contains at least one special character
        if not re.search(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            mssg = "Please enter valid password (Atleast 8 characters with digits)"
        # If all the conditions are met, the password is valid

        if confirm != password:
            mssg = "your password doesn't match"

        if mssg:
            return render_template("SignUp.html", mssg=mssg)
        # Check if username or email already exists
        existing_user = db.execute(
            "SELECT Username, Email FROM People WHERE Username=? OR Email=?", username, email)

        if existing_user:
            return render_template("SignUp.html", mssg="Username or email already exists")

        # Insert new user into the database
        data_inserted = db.execute("INSERT INTO People (FirstName, LastName, Email, Username, Password, Profession) VALUES (?, ?, ?, ?, ?, ?)",
                   firstname, lastname, email, username, password, profession)
        print(data_inserted)
        session['user_id'] = data_inserted
        return redirect("/Homepage")

    # GET method
    return render_template("SignUp.html")


@app.route("/Homepage")
@login_required
def Homepage():
    return render_template("Homepage.html")
