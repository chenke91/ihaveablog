#coding=utf-8

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email, Length, EqualTo
from app.models import User

class RegisterForm(Form):
    username = StringField('用户名', validators=[Required('请输入用户名')])
    email = StringField('邮箱',
        validators=[Required('请输入邮箱地址'), Email('邮箱格式不正确')])
    password = PasswordField('密码',
        validators=[Required('请输入密码'), Length(6, 20, '密码长度为6~20'),
                    EqualTo('password2', '两次输入不一致')])
    password2 = PasswordField('重复密码',
        validators=[Required('请重复密码'), Length(6, 20, '密码长度为6~20')])
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).count():
            raise ValueError('用户名已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).count():
            raise ValueError('邮箱已注册')

class LoginFrom(Form):
    email = StringField('邮箱',
        validators=[Required('请输入邮箱地址'), Email('邮箱格式不正确')])
    password = PasswordField('密码',
        validators=[Required('请输入密码'), Length(6, 20, '密码长度为6~20')])
    submit = SubmitField('登陆')