from flask_wtf import FlaskForm
from flask import session
from wtforms import StringField, SubmitField, TextAreaField

class WelcomeForm(FlaskForm):
    name = StringField("Enter Name: ")
    feedback = TextAreaField()
    submit = SubmitField()


