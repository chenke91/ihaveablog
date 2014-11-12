from flask import render_template
from . import auth
from .forms import RegisterForm

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)