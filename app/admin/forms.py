from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField, SubmitField
from wtforms.validators import Required
from app import db
from app.models import Category

def get_category():
    categories = db.session.query(Category.id, Category.name).all()
    res = map(lambda x: (str(x[0]),x[1]), categories)
    return list(res)

class BlogForm(Form):
    title = StringField('标题', validators=[Required('请输入标题')])
    category = SelectField('栏目', choices=get_category())
    avatars = FileField('选择图片', validators=[Required('请上传图片')])
    summary = TextAreaField('摘要', validators=[Required('请输入摘要')])
    blog_body = TextAreaField('文章', validators=[Required('请输入文章正文')])
    submit = SubmitField('Submit')