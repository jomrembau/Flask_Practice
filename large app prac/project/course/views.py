from flask import render_template, url_for,redirect, flash
from project import db
from project.models import Course
from project.course import course_blueprint
from project.course.forms import AddCourse, DeleteCourse


@course_blueprint.route("/add", methods=["GET","POST"])
def add_course():
    form = AddCourse()

    if form.validate_on_submit():
        course_name = form.course_name.data

        new_course = Course(course_name=course_name)

        db.session.add(new_course)
        db.session.commit()

        flash('Course Successfully added.')

        return redirect(url_for("students.add_student"))

    return render_template("add.html", form=form)

@course_blueprint.route("/delete", methods=["GET","POST"])
def delete_course():
    form = DeleteCourse()

    if form.validate_on_submit():
        course_id = form.course_id.data
        course = Course.query.get(course_id)
        db.session.delete(course)
        db.session.commit()

        flash('Course Successfully Removed.')

        return redirect(url_for("students.delete_student"))

    return render_template("delete.html", form=form)

@course_blueprint.route("/course_list")
def course_list():
    courses = Course.query.all()
    return render_template("list.html", courses=courses)


