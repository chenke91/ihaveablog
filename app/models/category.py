from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    blogs = db.relationship('Blog', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Type: %r>' % self.name