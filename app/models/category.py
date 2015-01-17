from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    blogs = db.relationship('Blog', backref='category', lazy='dynamic')

    @staticmethod
    def init_data():
        cate1 = Category(name='Python')
        cate2 = Category(name='PHP')
        cate3 = Category(name='Linux')
        db.session.add_all([cate3, cate2, cate1])
        db.session.commit()

    def __repr__(self):
        return '<Type: %r>' % self.name