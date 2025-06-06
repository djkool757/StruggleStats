from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    subtopics = db.relationship('Subtopic', backref='category', cascade='all, delete-orphan')
    logs = db.relationship('Log', backref='category', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    subtopics = db.relationship('Subtopic', backref='category', cascade='all, delete-orphan')

class Subtopic(db.Model):
    __tablename__ = 'subtopics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    concepts = db.relationship('Concept', backref='subtopic', cascade='all, delete-orphan')

class Concept(db.Model):
    __tablename__ = 'concepts'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    subtopic_id = db.Column(db.Integer, db.ForeignKey('subtopics.id'), nullable=False)

class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    action = db.Column(db.String, nullable=False)  # e.g., 'create', 'update', 'delete'

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'category_id': self.category_id,
            'action': self.action
        }
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f'<Log {self.id} - {self.action} at {self.timestamp}>'
    def __str__(self):
        return f'Log(id={self.id}, timestamp={self.timestamp}, category_id={self.category_id}, action={self.action})'
    def __init__(self, category_id, action):
        self.category_id = category_id
        self.action = action
        self.timestamp = datetime.now()
