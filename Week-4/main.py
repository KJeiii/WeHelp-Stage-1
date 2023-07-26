from flask import Flask, render_template, redirect, url_for,request, session

# create web app
app = Flask(__name__)

# create session
app.secret_key = "623762c54fa8b12dd34845ab69326520f4242be8363b80ba2240ca0a53877060"

# create home page
@app.route("/")
def home():
    return render_template("index.html")

# create verification endpoint
@app.route("/signin", methods = ['POST'])
def signin():
    if request.method == "POST":
        account = request.form["account"]
        password = request.form["password"]

        if account == "" or password == "":
            return redirect(url_for("error_empty"))
        if account != "test" or password != "test":
            return redirect(url_for("error_incorrect"))
        if account == "test" or password == "test":
            session["SIGNED-IN"] = True
            return redirect(url_for("member"))
    return redirect(url_for("home"))
        
# create success page  
@app.route("/member")
def member():
    if session["SIGNED-IN"] == True:
        return render_template("member.html")
    return redirect(url_for("home"))

# create error_empty page
@app.route("/error")
def error_empty():
    msg = request.args.get("message", "Please enter account and password")
    return render_template("error.html", message = msg)


# create error_incorrect page
@app.route("/error/")
def error_incorrect():
    msg =request.args.get("message", "Account or password is incorrect")
    return render_template("error.html", message = msg)

# create signout endpoint
@app.route("/signout")
def signout():
    session["SIGNED-IN"] = False
    return redirect(url_for("home"))


# create calculator
@app.route("/square", methods = ["GET"])
def Calc():
    num = request.form["number"]
    num = num*num
    return render_template("cal-result.html", number = num)

app.run(port=3000, debug=True)

