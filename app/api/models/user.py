# Local application imports
from .databases import db


class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    full_names = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean, default=False)
    user_type = db.Column(db.String(120), default='user')

    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

    def save(self):
        """Save a model instance"""
        db.session.add(self)
        db.session.commit()
        return self
