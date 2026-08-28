from flask import render_template, url_for, flash, redirect,request,Blueprint
from flask_login import login_user, current_user,logout_user, login_required
from companyblog import db
from companyblog.models import User, BlogPost
from companyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from companyblog.users.picture_handler import add_profile_pic

users = Blueprint("users",__name__)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

@users.route("/register", methods=["GET","POST"])
def register():
    form=RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Thank you for registering!")

        return redirect(url_for("users.login"))

    return render_template("register.html", form=form)

@users.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.validate_password(form.password.data):

            login_user(user)
            flash("You have successfully logged in")

            next = request.args.get("next")

            if next == None or not next[0] == "/":
                next = url_for("core.index")

            return redirect(next)

    return render_template("login.html", form=form)