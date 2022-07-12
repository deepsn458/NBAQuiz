from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Regexp, EqualTo, Length

# Registration Form
class RegistrationForm(FlaskForm):
    # Username: must be between 1 and 20 chars
    username = StringField('username', 
                            validators=[DataRequired(message='Enter a username'), 
                                        Length(min=1, max=20,message='username must be between 1 and 20 characters')])

    # Password: Must contain atleast 1 letter and 1 number
    password = PasswordField('password', 
                                validators=[DataRequired(message='Enter a password'), 
                                            Length(message='password must be between 1 and 20 characters',min=1, max=20),
                                            Regexp('[a-zA-Z]',message='Password must contain atleast 1 letter'),
                                            Regexp('[0-9]',message='Password must contain atleast 1 number')])
   
   # confirm password
    confirm_password = PasswordField('confirm password',
                                    validators=[DataRequired(message='Confirm password'), 
                                    EqualTo('password', message='Passwords must match')])

    # Submit
    submit = SubmitField('Register')


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