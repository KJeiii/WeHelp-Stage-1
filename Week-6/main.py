from flask import Flask, render_template, redirect, url_for, request, session
from MySQLObj import MySQLtool

# ----- create Flask server -----
app = Flask(__name__)
app.secret_key = "623762c54fa8b12dd34845ab69326520f4242be8363b80ba2240ca0a53877060"

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
    # 1. Build MySQL connnection
    db = MySQLtool(name, account, password)

    # 2. Use Signup_Check and Signup methods; 
    # if it has already existed, do not let it signup; otherwise, let it go.
    if not db.Signup_check() :
        return redirect("/error?message=帳號已經被註冊")
    db.Signup()
    return redirect(url_for("home"))

@app.route("/signin", methods = ["POST"])
def signin():
    # ----- get info using POST method from signup form -----
    account = request.form['account']
    password = request.form['password']

    # ----- use customized MySQLtool module to connecting, searching and creating new data -----
    # 1. Build MySQL connnection
    db = MySQLtool("", account, password)

    # 2. Use Signin() method : check whether userbame and passwrod bote matches data in db
    result = db.Signin()
    if len(result) < 1 :
        return redirect('/error?message=帳號或密碼輸入錯誤')
    
    session['id'] = result[0][0]
    session['name'] = result[0][1]
    session['username'] = result[0][2]    
    return redirect(url_for('member'))



@app.route("/signout")
def signout():
    pass

@app.route("/member")
def member():
    name = session['name']
    return render_template("member.html", name = name)

@app.route("/error")
def error():
    msg = request.args['message']
    return render_template("error.html", error_message = msg)

@app.route("/deleteMessage")
def delete_message():
    pass

app.run(debug=True, port="3000")