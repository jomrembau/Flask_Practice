from flask import render_template, url_for,redirect, flash
from project import db
from project.models import Students, Course
from project.students import student_blueprint
from project.students.forms import AddForm, DeleteForm


@student_blueprint.route("/add", methods=["GET","POST"])
def add_student():
    form = AddForm()

    form.course_id.choices = [
        (course.course_id, course.course_name)
        for course in Course.query.all()
    ]

    if form.validate_on_submit():
        student_name = form.student_name.data
        class_section = form.class_section.data
        course_id = form.course_id.data

        new_student = Students(student_name,class_section)
        new_student.course_id = course_id

        db.session.add(new_student)
        db.session.commit()

        flash('Student Successfully added.')

        return redirect(url_for("students.add_student"))

    return render_template("add.html", form=form)

@student_blueprint.route("/delete", methods=["GET","POST"])
def delete_student():
    form = DeleteForm()

    if form.validate_on_submit():
        student_id = form.student_id.data
        student = Students.query.get(student_id)
        db.session.delete(student)
        db.session.commit()

        flash('Student Successfully Deleted.')

        return redirect(url_for("students.delete_student"))

    return render_template("delete.html", form=form)

@student_blueprint.route("/student_list")
def student_list():
    students = Students.query.all()
    return render_template("list.html", students=students)


