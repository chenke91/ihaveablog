from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from flask.ext.login import UserMixin, AnonymousUserMixin
from app import db, login_manager
from ._base import SessionMixin
from .role import Role

class User(db.Model, SessionMixin, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    intro = db.Column(db.String(254))
    avatar = db.Column(db.String(254))
    github_addr = db.Column(db.String(254))
    role = db.Column(db.String(32), default=Role.NOMAL)
    blogs = db.relationship('Blog', backref='author', lazy='dynamic')

    @property
    def password(self):
        return AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_admin():
        user = User.query.filter_by(role=Role.ADMIN).first()
        return user

    @staticmethod
    def init_data():
        user = User(username='chenke91', email='chenke91@qq.com', password='123456',
                    intro='hello world', avatar='/test', github_addr='https://github.com/chenke91',
                    role=Role.ADMIN)
        user.save()

    def is_admin(self):
        if self.role == Role.ADMIN:
            return True
        return False

    def __repr__(self):
        return '<User: %r>' % self.username

class AnonymousUser(AnonymousUserMixin):
    def is_admin(self):
        return False

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.anonymous_user = AnonymousUser