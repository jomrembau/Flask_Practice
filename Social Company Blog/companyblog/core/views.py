from companyblog.core import core
from flask import render_template, request

@core.route("/")
def index():
    return render_template("index.html")

@core.route("/info")
def info():
    return render_template("info.html")