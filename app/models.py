from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from flask.ext.login import UserMixin
from app import db, login_manager


class SessionMixin(object):
    def to_dict(self, *columns):
        dct = {}
        for col in columns:
            value = getattr(self, col)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            dct[col] = value
        return dct

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

class User(db.Model, SessionMixin, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    intro = db.Column(db.String(254))
    blogs = db.relationship('Blog', backref='author', lazy='dynamic')

    @property
    def password(self):
        return AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(254))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Blog: %r>' % self.title

class Type(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    blogs = db.relationship('Blog', backref='type', lazy='dynamic')

    def __repr__(self):
        return '<Type: %r>' % self.name