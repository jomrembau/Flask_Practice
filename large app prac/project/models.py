from project import db

class Student(db.Model):
    __tablename__ = "students"
    student_id = db.Column(db.Integer, primary_key = True)
    student_name = db.Column(db.Text)
    class_section = db.Column(db.Text)

    def __init__(self, student_name, class_section ):
        self.student_name = student_name
        self.class_section = class_section

    def __repr__(self):
        return f"Student ID: {self.student_id} | Student Name: {self.student_name} | Class: {self.class_section}"

