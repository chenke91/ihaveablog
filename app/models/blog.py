from datetime import datetime
from markdown import markdown
import bleach
from sqlalchemy import func
from flask import current_app
from app import db
from app.helpers import paginate
from ._base import SessionMixin
from .category import Category

class Blog(db.Model, SessionMixin):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(254))
    summary = db.Column(db.Text) #摘要
    summary_html = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    read_count = db.Column(db.Integer, default=0) #阅读次数
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    avatar = db.Column(db.String(128), default='/static/images/blog_avatars/default.png') #图片
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))
    replies = db.relationship('Reply', backref='blog', lazy='dynamic')

    @staticmethod
    def from_form(form):
        blog = Blog(title = form.title.data,
            summary = form.summary.data,
            body = form.blog_body.data,
            category_id = form.category.data,
            avatar = form.avatars.data
            )
        db.session.add(blog)
        db.session.commit()

    #文章列表
    @staticmethod
    def get_blogs(page, category_id=None):
        per_page = current_app.config.get('PER_PAGE')
        query = db.session.query(Blog.id, Blog.avatar, Blog.title, Blog.summary_html,
            Blog.timestamp, Blog.read_count, Category.name, Category.id).join(Category).\
            order_by(Blog.timestamp.desc())
        if category_id is not None:
            query = query.filter(Blog.category_id==category_id)
        blogs = paginate(query, page, per_page)
        return blogs

    #获取阅读最多的列表
    @staticmethod
    def get_top_read():
        top_read_count = current_app.config.get('TOP_READ')
        top_reads = db.session.query(Blog.id, Blog.title, Blog.read_count).\
            order_by(Blog.read_count.desc()).limit(top_read_count).all()
        return top_reads

    #评论最多列表
    @staticmethod
    def get_top_reply():
        top_reply_count = current_app.config.get('TOP_REPLY')
        top_replies = db.session.query(Blog.id, Blog.title, func.count(Reply.id).label('replies_count')).\
            outerjoin(Reply).order_by('replies_count desc').group_by(Blog.id).limit(top_reply_count).all()
        # raise Exception(top_replies)
        return top_replies

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))

    @staticmethod
    def on_change_summary(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p']
        target.summary_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))


    def __repr__(self):
        return '<Blog: %r>' % self.title

db.event.listen(Blog.body, 'set', Blog.on_changed_body)
db.event.listen(Blog.summary, 'set', Blog.on_change_summary)

class Reply(db.Model, SessionMixin):
    __tablename__ = 'replies'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(254))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    username = db.Column(db.String(32))
    email = db.Column(db.String(128))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
