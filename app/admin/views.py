from flask import render_template, redirect, redirect, url_for
from app.models import Blog
from . import admin

@admin.route('/blogs/add/', methods=['GET', 'POST'])
def add_blog():
    from .forms import BlogForm
    form = BlogForm()
    if form.validate_on_submit():
        Blog.from_form(form)
        return redirect(url_for('main.index'))
    return render_template('add_blog.html', form=form)

@admin.route('/blogs/')
def get_blogs():
    return render_template('admin_blogs.html')

