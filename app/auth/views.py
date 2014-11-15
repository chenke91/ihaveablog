from flask import render_template, request, url_for, flash, redirect
from flask.ext.login import login_user

from . import auth
from .forms import RegisterForm, LoginFrom
from app.models import User

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    email=form.email.data)
        user.save()
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('密码错误')
    return render_template('login.html', form=form)
