from flask import Flask, render_template, redirect, url_for, request, session
from MySQLObj import MySQLtool

# ----- create Flask server -----
app = Flask(__name__)
app.secret_key = "623762c54fa8b12dd34845ab69326520f4242be8363b80ba2240ca0a53877060"

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
    db = MySQLtool(name = name, account = account, password = password)

    # 2. Use Signup_Check and Signup methods; 
    # if it has already existed, do not let it signup; otherwise, let it go.
    if not db.Signup_check() :
        return redirect("/error?message=帳號已經被註冊")
    db.Signup()
    return redirect(url_for("home"))


@app.route("/signin", methods = ["POST"])
def signin():
    # ----- get info using POST method from signin form -----
    account = request.form['account']
    password = request.form['password']

    # ----- use customized MySQLtool module to connecting, searching and creating new data -----
    # 1. Build MySQL connnection
    db = MySQLtool(account = account, password = password)

    # 2. Use Signin() method : check whether username and password both matches data in db
    # if not match : redirect to error page
    # if match : redirect to member page
    result = db.Signin()
    if len(result) < 1 :
        return redirect('/error?message=帳號或密碼輸入錯誤')
    
    session['user_id'] = result[0]['id']
    session['name'] = result[0]['name']
    session['username'] = result[0]['username']    
    return redirect(url_for('member'))


@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for('home'))


@app.route("/member")
def member():
    try:
        id = session['user_id']
        name = session['name']
        db = MySQLtool()
        comments = db.Show_comment()
        return render_template("member.html", id = id, name = name, comments = comments)
    except:
        return redirect(url_for('home'))
    

@app.route("/error")
def error():
    msg = request.args['message']
    return render_template("error.html", error_message = msg)


@app.route("/createMessage", methods = ["POST"])
def create_message():
    comment = request.form['comment']

    # ----- use customized MySQLtool module to connecting, searching and creating new data -----
    # Build MySQL connnection and add new comment
    db = MySQLtool(id = session['user_id'], comment = comment)
    db.Create_comment()
    return redirect(url_for("member"))

@app.route("/deleteMessage", methods = ["POST"])
def delete_message():
    comment_id = request.json['comment_id']
    db = MySQLtool(comment_id = comment_id)
    db.Delete_comment()
    return redirect(url_for('member'))

app.run(debug=True, port="3000")