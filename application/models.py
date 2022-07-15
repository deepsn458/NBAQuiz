from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# Users table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #statistics = db.relationship('Statistics', backref='player', lazy=True)
    #summary = db.relationship('Summary', backref='player', lazy=True)
    # Represents the User table's objects as strings
    def __repr__(self):
        return f"User('{self.username}')"

# User's summary for quiz

# User's total statistics

# Quiz database