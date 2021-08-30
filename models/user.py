import sqlite3
from db import db

# What is A Model?
# - internal representation of an entity

class UserModel(db.Model):

    # UserModel extends db.Model - tells SQLAlchemy entity that this class are things we will be saving and retriving
    # from a database, creates mapping between database and objects

    # Tell SQLAlchemy the table name where the models will be stored.. ie Users
    __tablename__ = 'users'
    # What columns the table contains?
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'id': self.id, 'username': self.username}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
