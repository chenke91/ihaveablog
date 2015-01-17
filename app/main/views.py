from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/blogs/<int:id>/')
def get_blog(id):
    return render_template('blog.html')