from flask import Flask,render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, DateTimeField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"

class InfoForm(FlaskForm):
    breed = StringField("Breed?", validators=[DataRequired()])
    neuter = BooleanField("neutered?")
    mood = RadioField("Mood?",
                      choices=[("mood_one","happy"),("mood_two","excited")])
    food_choice = SelectField("Pick Favorite food:", choices=[("ch","chicken"),("bf","beef"),("fish","Fish")])
    feedback = TextAreaField()
    submit = SubmitField("Submit")

@app.route("/",methods=["GET","POST"])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session["breed"] = form.breed.data
        session["neuter"] = form.neuter.data
        session["mood"] = form.mood.data
        session["food_choice"] = form.food_choice.data
        session["feedback"] = form.feedback.data

        return redirect(url_for("thankyou"))

    return render_template("index.html", form=form)

@app.route("/thankyou")
def thankyou():
    return  render_template("thankyou.html")



if __name__ == "__main__":
    app.run(debug=True)