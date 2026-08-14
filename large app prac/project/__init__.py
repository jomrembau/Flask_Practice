import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.dirname(os.path.abspath(__file__))

app.config['SECRET_KEY'] = 'mysecretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

Migrate(app,db)

from project import models