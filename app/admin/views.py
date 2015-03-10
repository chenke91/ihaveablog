from flask import render_template, request, redirect, url_for
from flask.ext.login import login_required
from app.models import Blog
from app import avatars
from app.decorators import admin_required
from . import admin

@admin.route('/blogs/add/', methods=['GET', 'POST'])
@login_required
@admin_required
def add_blog():
    from .forms import BlogForm
    form = BlogForm()
    if form.validate_on_submit():
        filename = avatars.save(request.files['avatars'])
        file_url = avatars.url(filename)
        form.avatars.data = file_url
        Blog.from_form(form)
        return redirect(url_for('main.index'))
    return render_template('add_blog.html', form=form)

@admin.route('/blogs/edit/<int:id>/', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_blog(id):
    from .forms import EditBlogForm
    blog = Blog.query.get_or_404(id)
    form = EditBlogForm(title=blog.title,
        category=blog.category_id,
        summary=blog.summary,
        blog_body=blog.body)
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.category_id = form.category.data
        blog.summary = form.summary.data
        blog.body = form.blog_body.data
        blog.save()
        return redirect(url_for('main.get_blog', id=id))
    return render_template('edit_blog.html', form=form)

@admin.route('/blogs/')
@login_required
@admin_required
def get_blogs():
    blogs = Blog.query.all()
    return render_template('admin_blogs.html', blogs=blogs)

