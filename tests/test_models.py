
import unittest
from flask import current_app
from app import create_app, db
from app.models import User

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user = User(username='chenke', password='123456')
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_generate_password(self):
        self.assertTrue(self.user.password_hash != '123456')

    def test_user_check_password(self):
        self.assertTrue(self.user.verify_password('123456'))