from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo, Length
from ..models import User
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms import ValidationError


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Required()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Enter your Username',validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(), Email()]) 
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Password must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')