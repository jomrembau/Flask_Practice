from flask import Flask, render_template,session, url_for, redirect
from forms import  WelcomeForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"

@app.route("/", methods=["GET","POST"])
def index():
    form = WelcomeForm()

    if form.validate_on_submit():
        session["name"] = form.name.data
        session["feedback"] = form.feedback.data

        return redirect(url_for("registered"))

    return render_template("index.html", form=form)

@app.route("/registered", methods=["GET", "POST"])
def registered():
    return render_template("registered.html")

if __name__ == "__main__":
    app.run(debug=True)