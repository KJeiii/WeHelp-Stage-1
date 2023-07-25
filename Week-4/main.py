from flask import Flask, render_template, redirect, url_for,request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signin", methods = ['POST'])
def signin():
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]

        if account == "" or password == "":
            msg = "Please enter account and password."
            return redirect(url_for("error", message=msg))
        if account != "test" or password != "test":
            msg = "Account or password is incorrect."
            return redirect(url_for("error", message=msg))
        if account == "test" or password == "test":
            return redirect(url_for("member"))
            
@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/error/<message>")
def error(message):
    return render_template("error.html", message=message)


app.run(debug=True)

