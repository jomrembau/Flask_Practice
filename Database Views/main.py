import os
# from forms import AddForm, DelForm
from flask import Flask,render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.dirname(os.path.abspath(__file__))

app.config['SECRET_KEY'] = 'mysecretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Puppy(db.Model):
    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy Id: {self.id} | Puppy Name: {self.name}"

if __name__ == "__main__":
    app.run(debug=True)
