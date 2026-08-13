from project import app, db
from flask import render_template
from project.models import Student

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

