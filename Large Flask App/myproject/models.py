from myproject import db

class Laptop(db.Model):
    __tablename__ = "laptop"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Text)
    owner = db.Column(db.Integer)

    def __init__(self,model, owner="No owner"):
        self.model = model
        self.owner = owner

    def __repr__(self):
        return f"Laptop ID: {self.id} | Laptop model: {self.model} | Owner: {self.owner}"


@app.route("/")
def index():
    return render_template("index.html")

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
        db.session.commit()

        return redirect(url_for("laptop_list"))

    return render_template("delete.html",form=form)

@app.route("/owner",methods=["GET","POST"])
def add_owner():
    form=AddOwner()

    if form.validate_on_submit():
        laptop_id = form.id.data
        owner = form.owner.data

        laptop = db.session.get(Laptop, laptop_id)
        laptop.owner = owner
        db.session.commit()

        return redirect(url_for("laptop_list"))

    return render_template("owner.html",form=form)


if __name__ == "__main__":
    app.run(debug=True)
