from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required

app = Flask(__name__)

@app.route("/")
def home():
    pass

@app.route("/register", methods = ["POST", "GET"])
def register():
    pass

@app.route("/login", methods = ["POST", "GET"])
def login():
    pass

@app.route("/member_page")
def member_page():
    pass

@app.route("/logout")
def logout():
    pass