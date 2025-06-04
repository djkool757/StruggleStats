from datetime import datetime
import app 
from sqlalchemy import  Column, Integer, String, ForeignKey


print(app.db)
class User(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    username = app.db.Column(app.db.String(80), unique=True, nullable=False)
    email = app.db.Column(app.db.String(120), unique=True, nullable=False)
    password = app.db.Column(app.db.String(128), nullable=False)
    logs = app.db.relationship('Log', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    def save(self):
        app.db.session.add(self)
        app.db.session.commit()

class Section(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(100), nullable=False)
    categories = app.db.relationship('Category', backref='section', cascade='all, delete-orphan')

class Category(app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(100), nullable=False)
    section_id = app.db.Column(app.db.Integer, app.db.ForeignKey('section.id'))
