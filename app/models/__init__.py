from .user import User
from .blog import Blog, Reply
from .category import Category

def init_data():
    from app import db
    db.drop_all()
    db.create_all()
    User.init_data()
    Category.init_data()
    return 'ok'