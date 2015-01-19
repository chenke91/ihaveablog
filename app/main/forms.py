from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length, Email

class ReplyForm(Form):
    username = StringField('昵称', validators=[Required('请输入用户名')])
    email = StringField('Email', validators=[Email()])
    body = StringField('评论', validators=[Required(), Length(1, 254)])
    submit = SubmitField('Submit')