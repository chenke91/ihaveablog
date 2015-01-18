from flask import Blueprint

main = Blueprint('main', __name__)

@main.before_app_request
def before_request():
    from flask import g
    from app.models import Category, User
    categories = Category.query.all()
    admin = User.get_admin()
    
    g.categories = categories
    g.admin = admin

from . import views, errors
