from datetime import datetime
from app import db
from ._base import SessionMixin

class Blog(db.Model, SessionMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(254))
    summary = db.Column(db.Text) #摘要
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    read_count = db.Column(db.Integer, default=0) #阅读次数
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    avatar = db.Column(db.String(128)) #图片
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))
    replies = db.relationship('Reply', backref='blog', lazy='dynamic')

    def __repr__(self):
        return '<Blog: %r>' % self.title

class Reply(db.Model, SessionMixin):
    __tablename__ = 'replies'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(254))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(32))
    email = db.Column(db.String(128))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
