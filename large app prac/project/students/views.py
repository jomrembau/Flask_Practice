from flask import render_template, url_for,redirect, flash
from project import db
from project.models import Students
from project.students import student_blueprint
from project.students.forms import AddForm

@student_blueprint.route("/add", methods=["GET","POST"])
def add_student():
    form = AddForm()

    if form.validate_on_submit():
        student_name = form.student_name.data
        class_section = form.class_section.data

        new_student = Students(student_name,class_section)

        db.session.add(new_student)

        flash('Student Successfully added.')

        return redirect(url_for("students.add_student"))

    return render_template("add.html", form=form)

