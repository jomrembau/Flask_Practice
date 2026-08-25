from datetime import datetime, UTC
from companyblog import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

bcrypt = Bcrypt()

@login_manager.user_loader()
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(50), nullable=False, default="default_profile.png")
    email = db.Column(db.String(100), unique=True, index=True)
    username = db.Column(db.String(100),unique=True, index=True)
    password_hash = db.Column(db.String(128))

    posts = db.relationship("BlogPost", backref="author", lazy=True)

    def __init__(self, email,username,password):
        self.email=email
        self.username=username
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username: {self.username}"



class BlogPost(db.Model):
    users= db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    date = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Title: {self.title} -- Date: {self.date}"