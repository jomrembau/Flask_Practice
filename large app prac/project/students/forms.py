from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField, SelectField

class AddForm(FlaskForm):
    student_name = StringField("Student Name")
    class_section = StringField("Class")
    course_id = SelectField(
        "Course",
        coerce=int
    )

    add_student = SubmitField("Add Student")


class DeleteForm(FlaskForm):
    student_id = IntegerField("Student ID")
    delete_student = SubmitField("Delete Student")