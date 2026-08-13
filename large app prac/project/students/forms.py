from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    student_name = StringField("Student Name")
    class_section = StringField("Class")
    add_student = SubmitField("Add Student Name")


class DelForm(FlaskForm):
    student_id = IntegerField("Student ID")
    delete_student = SubmitField("Delete Student")