from flask import Flask, render_template, redirect, url_for

# ----- create Flask server -----
app = Flask(__name__)


# ----- connect to local MySQL and build customized MySQL object


# ----- create endpoints -----
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods = ["POST"])
def signup():
    pass

@app.route("/signin", methods = ["POST"])
def signin():
    pass

@app.route("/signout")
def signout():
    pass

@app.route("/member")
def member():
    pass

@app.route("/deleteMessage")
def delete_message():
    pass

app.run(debug=True)