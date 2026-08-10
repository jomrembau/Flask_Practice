from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField

class AddForm(FlaskForm):
    model = StringField("Laptop model")
    submit = SubmitField("Add Laptop")

class DelForm(FlaskForm):
    id=IntegerField("Laptop ID to remove: ")
    submit = SubmitField("Delete Laptop")