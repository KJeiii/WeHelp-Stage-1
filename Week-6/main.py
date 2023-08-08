from flask import Flask, render_template, redirect, url_for, request
from MySQLObj import MySQLtool

# ----- create Flask server -----
app = Flask(__name__)


# ----- connect to local MySQL and build customized MySQL object


# ----- create endpoints -----
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods = ["POST"])
def signup():
    # ----- get info using POST method from signup form -----
    name = request.form['name']
    account = request.form['account']
    password = request.form['password']

    # ----- use customized MySQLtool module to connecting, searching and creating new data -----
    # 1. build MySQL connnection
    db = MySQLtool(name, account, password)

    # 2. Searching db by username; if it has already existed, do not let it signup; otherwise, let it go.
    result = db.Search()
    num_of_same_username = result[0][0] #fetchall() return a list consisting tuple
    if num_of_same_username > 0 :
        return redirect("/error?message=帳號已經被註冊")
    db.Signup()
    return redirect(url_for("home"))

@app.route("/signin", methods = ["POST"])
def signin():
    pass

@app.route("/signout")
def signout():
    pass

@app.route("/member")
def member():
    pass

@app.route("/error")
def error():
    msg = request.args['message']
    return render_template("error.html", error_message = msg)

@app.route("/deleteMessage")
def delete_message():
    pass

app.run(debug=True, port="3000")