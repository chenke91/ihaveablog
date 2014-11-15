import unittest
from flask import url_for
from app import create_app, db
from app.models import User

class BlogClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_login(self):
        response = self.client.post(url_for('auth.register'), data={
            'username': 'chenke111',
            'email': 'sette@qq.com',
            'password': '111111',
            'password2': '111111'
        })
        self.assertTrue(response.status_code == 302)