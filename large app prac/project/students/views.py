from flask import render_template, url_for, redirect, flash
from project import db
from project.models import Student
from project.students import students_blueprint
from project.students.forms import AddForm

@students_blueprint.route("/add", methods=["GET", "POST"])
def add_to_list():
    form = AddForm()

    if form.validate_on_submit():
        student_name = form.student_name.data
        class_section = form.class_section.data
        new_student = Student(student_name, class_section)

        db.session.add(new_student)
        db.session.commit()

        flash("Student added successfully!", "success")

        return redirect(url_for("students.add_to_list"))

    return render_template("add_student.html", form=form)
