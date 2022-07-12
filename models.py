from app import db

# Users table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    statistics = db.relationship('Statistics', backref='player', lazy=True)
    summary = db.relationship('Summary', backref='player', lazy=True)
    # Represents the User table's objects as strings
    def __repr__(self):
        return f"User('{self.username}')"