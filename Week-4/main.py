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
            msg = "Please enter account and password."
            return redirect(url_for("error", message=msg))
        if account != "test" or password != "test":
            msg = "Account or password is incorrect."
            return redirect(url_for("error", message=msg))
        if account == "test" or password == "test":
            session["SIGNED-IN"] = True
            return redirect(url_for("member"))
        
# create success page  
@app.route("/member")
def member():
    if session["SIGNED-IN"] == True:
        return render_template("member.html")
    return redirect(url_for("home"))

# create error page
@app.route("/error/<message>")
def error(message):
    return render_template("error.html", message=message)

# create signout endpoint
@app.route("/signout")
def signout():
    session["SIGNED-IN"] = False
    return redirect(url_for("home"))


app.run(debug=True)

