from flask import Flask, render_template, redirect, url_for,request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signin", methods = ['POST'])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    return f'{account} & {password}'


app.run(debug=True)

