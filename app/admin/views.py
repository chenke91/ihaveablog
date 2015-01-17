from flask import render_template
from . import admin

@admin.route('/blogs/add/')
def add_blog():
    return render_template('add_blog.html')

@admin.route('/blogs/')
def get_blogs():
    return render_template('admin_blogs.html')

