from .user import User
from .blog import Blog, Reply
from .category import Category

def init_data():
    User.init_data()
    Category.init_data()
    return 'ok'