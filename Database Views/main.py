import os
from forms import AddForm, DelForm
from flask import Flask,render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.dirname(os.path.abspath(__file__))

app.config['SECRET_KEY'] = 'mysecretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Laptop(db.Model):
    __tablename__ = "laptop"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Text)

    def __init__(self,model):
        self.model = model

    def __repr__(self):
        return f"Laptop ID: {self.id} | Laptop model: {self.model}"


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/add",methods=["GET","POST"])
def add_to_list():
    form=AddForm()

    if form.validate_on_submit():
        model=form.model.data
        new_model = Laptop(model)

        db.session.add(new_model)
        db.session.commit()

        return redirect(url_for("laptop_list"))

    return render_template("add.html",form=form)

@app.route("/list")
def laptop_list():
    laptops = Laptop.query.all()
    return render_template("list.html", laptops=laptops)


@app.route("/delete",methods=["GET","POST"])
def delete_from_list():
    form=DelForm()

    if form.validate_on_submit():
        laptop_id = form.id.data
        laptop = Laptop.query.get(laptop_id)
        db.session.delete(laptop)
        db.commit()

        return redirect(url_for("laptop_list"))
    
    return render_template("delete.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)

