from flask import render_template, request, current_app
from app.models import Blog, User
from . import main

@main.route('/')
def index():
    args = request.args
    page = args.get('page', 1, type=int)
    blogs = Blog.get_blogs(page)
    admin = User.get_admin()
    return render_template('index.html', blogs=blogs)

@main.route('/blogs/<int:id>/')
def get_blog(id):
    return render_template('blog.html')

@main.route('/blogs/category/<int:id>/')
def category(id):
    return str(id)