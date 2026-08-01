from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<name>")
def welcome(name):
    return render_template("welcome.html", name=name)

@app.route("/login", methods=("GET","POST"))
def login():
    return render_template("login.html")

@app.route("/welcome")
def authenticated():
    email = request.args.get("email")
    print("EMail", email)
    return render_template("authenticated.html", email=email)

if __name__ == "__main__":
    app.run(debug=True)