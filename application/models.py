from application import db, login_manager
from flask_login import UserMixin

# Quiz questions table
class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_name = db.Column(db.Text, nullable=False)
    displayed = db.Column(db.Integer)
    #to link each option to its question
    options = db.relationship('Options', backref='questions', lazy=True)
    # to retrieve question from responses table
    response = db.relationship('Responses', backref='questions', lazy=True)
    def __repr__(self):
        return f"Questions('{self.question_name}')"


#Quiz options table
class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option_name = db.Column(db.String(20), nullable=False)
    correct_incorrect = db.Column(db.Integer)
    #to link each option to its question
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'),
                            nullable=False)
    #to retrieve the selected option from responses table
    response = db.relationship('Responses', backref='options', lazy=True)
    def __repr__(self):
        return f"Options('{self.option_name}')"

# Quiz responses table
class Responses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'),
                            nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('options.id'),
                            nullable=False)
    #takes whether the chosen option was correct or not from the options table
    correct_incorrect= db.Column(db.Integer)


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
