# Local application imports
from .databases import db


class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    password = db.Column(db.String(120), index=True)
    user_type = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

    def save(self):
        """Save a model instance"""
        db.session.add(self)
        db.session.commit()
        return self
