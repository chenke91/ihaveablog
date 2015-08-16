from flask import render_template, request, redirect, url_for, g, jsonify, flash
from flask.ext.login import login_required
from app.models import Blog, Category
from app import avatars
from app.decorators import admin_required
from . import admin

@admin.route('/blogs/add/', methods=['GET', 'POST'])
@login_required
@admin_required
def add_blog():
    from .forms import BlogForm
    form = BlogForm()
    g.open_article = True
    if form.validate_on_submit():
        try:
            filename = avatars.save(request.files['avatars'])
        except Exception as e:
            flash('上传失败,请检查文件格式')
            return render_template('admin/add_blog.html', form=form)
        file_url = avatars.url(filename)
        form.avatars.data = file_url
        Blog.from_form(form)
        return redirect(url_for('main.index'))
    return render_template('admin/add_blog.html', form=form)

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
    return render_template('admin/edit_blog.html', form=form)

@admin.route('/blogs/')
@login_required
@admin_required
def get_blogs():
    g.open_article = True
    return render_template('admin/blogs.html')

@admin.route('/api/categories/')
@login_required
@admin_required
def categories():
    categories = Category.query.all()
    data = [cate.to_dict() for cate in categories]
    res = {'data': data}
    return jsonify(res)

@admin.route('/api/blogs/')
@login_required
@admin_required
def blogs():
    blogs = Blog.query.all()
    data = [blog.to_dict() for blog in blogs]
    res = {'data': data}
    return jsonify(res)

