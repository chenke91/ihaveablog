from random import randint
from flask import render_template, request, current_app, jsonify
from app.models import Blog, User, Reply
from .forms import ReplyForm
from . import main

@main.route('/')
def index():
    args = request.args
    page = args.get('page', 1, type=int)
    blogs = Blog.get_blogs(page)
    admin = User.get_admin()
    return render_template('index.html', blogs=blogs)

@main.route('/blogs/<int:id>/', methods=['GET', 'POST'])
def get_blog(id):
    blog = Blog.query.filter_by(id=id).first_or_404()
    blog.read_count += 1
    blog.save()
    form = ReplyForm()
    if form.validate_on_submit():
        reply = Reply(body=form.body.data,
            username=form.username.data,
            email=form.email.data,
            avatar = randint(1, 5), 
            blog=blog)
        reply.save()
    return render_template('blog.html', blog=blog, form=form)

@main.route('/blogs/category/<int:id>/')
def category(id):
    args = request.args
    page = args.get('page', 1, type=int)
    blogs = Blog.get_blogs(page, category_id=id)
    return render_template('index.html', blogs=blogs)
