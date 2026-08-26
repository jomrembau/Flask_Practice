from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import  FileField, FileAllowed

from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")

class RegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("UserName", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired(), EqualTo("pass_confirm", message="Passwords must match!")])
    pass_confirm = PasswordField("Confirm Password", validators=[DataRequired()])

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already exists in our system. Use a different email!")

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already exists in our system. Enter a different Username!")