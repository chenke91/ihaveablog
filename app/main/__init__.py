from flask import Blueprint

main = Blueprint('main', __name__)

@main.before_app_request
def before_request():
    from flask import g
    from app.models import Category, User, Blog
    categories = Category.query.all()
    admin = User.get_admin()
    top_reads = Blog.get_top_read()
    top_replies = Blog.get_top_reply()
    
    g.categories = categories
    g.admin = admin
    g.top_reads = top_reads
    g.top_replies = top_replies

from . import views, errors
