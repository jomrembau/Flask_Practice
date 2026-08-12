from flask import Blueprint, render_template, redirect,url_for
from myproject import db
from myproject.owners.forms import AddForm

owners_blueprint = Blueprint("owners",__name__,
                             template_folder="templates/owners")


def add_to_list():
    form=AddForm()

    if form.validate_on_submit():
        model=form.model.data
        new_model = Laptop(model)

        db.session.add(new_model)
        db.session.commit()

        return redirect(url_for("laptop_list"))

    return render_template("add.html",form=form)