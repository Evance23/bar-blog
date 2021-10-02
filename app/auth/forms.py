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