from flask import render_template,flash, request,redirect, url_for
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from ..email import mail_message
from app.auth import auth
from app.models import User

@auth.route('/login', methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid')
    return render_template('auth/login.html', form = form)