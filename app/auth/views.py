from flask import render_template
from . import auth
from .forms import RegisterForm
from app.models import User

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    email=form.email.data)
        user.save()
        return 'i am' + user.username
    return render_template('register.html', form=form)