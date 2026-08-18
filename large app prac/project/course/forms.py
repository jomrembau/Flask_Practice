from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddCourse(FlaskForm):
    course_name = StringField("Course Name")
    add_course = SubmitField("Add Course")

class DeleteCourse(FlaskForm):
    course_id = IntegerField("Course ID")
    delete_course = SubmitField("Remove Course")
