from sqlalchemy.orm import relationship

from project import db, app
from flask import render_template


class Students(db.Model):
    __tablename__ = "students"

    student_id = db.Column(db.Integer,
                           primary_key=True)
    student_name = db.Column(db.Text)
    class_section = db.Column(db.Text)
    course_id = db.Column(db.Integer,
                        db.ForeignKey("courses.course_id"))

    course = relationship("Course", back_populates="students")

    def __init__(self, student_name, class_section):
        self.student_name = student_name
        self.class_section = class_section


    def __repr__(self):
        return f" Student ID: {self.student_id} | Student Name: {self.student_name} | Class: {self.class_section}"


class Course(db.Model):
    __tablename__ = "courses"

    course_id = db.Column(db.Integer,
                          primary_key=True)
    course_name = db.Column(db.Text)
    students = relationship("Students",
                            back_populates="course")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")