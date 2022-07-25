from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from application.models import User

# Registration Form
class RegistrationForm(FlaskForm):
    # Username: must be between 1 and 20 chars
    username = StringField('username', 
                            validators=[DataRequired(message='Enter a username'), 
                                        Length(min=1, max=20,message='username must be between 1 and 20 characters')])

    # Password: Must contain atleast 1 letter and 1 number
    password = PasswordField('password', 
                                validators=[DataRequired(message='Enter a password'), 
                                            Length(message='password must be between 1 and 20 characters',min=1, max=20)])
   
   # confirm password
    confirm_password = PasswordField('confirm password',
                                    validators=[DataRequired(message='Confirm password'), 
                                    EqualTo('password', message='Passwords must match')])

    # Submit
    submit = SubmitField('Register')

    #custom validator to check that username is unique
    def unique_username(self,username): 

        # gets the first user who already has the username
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username is already taken')


# Login Form
class LoginForm(FlaskForm):
    # Username
    username = StringField('username', validators=[DataRequired(message='Enter a username')])

    # Password
    password = PasswordField('password', validators=[DataRequired(message='Enter a password')])

    # Checkbox to stay logged in
    remember = BooleanField('remember me')

    # Submit
    submit = SubmitField('Login')
