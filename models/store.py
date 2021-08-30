from db import db
from models import item


class StoreModel(db.Model):
    # ItemModel extends db.Model - tells SQLAlchemy entity that this class are things we will be saving and retrieving
    # from a database, creates mapping between database and objects

    # Tell SQLAlchemy the table name where the models will be stored.. ie Users
    __tablename__ = 'stores'
    # What columns the table contains?
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy='dynamic') # Dont go into items table and create object for each item, yet

    def __init__(self, name):
        self.name = name

    def json(self):  # return json representation of model - A dictionary of item
        return {'id': self.id, 'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod  # Returns object of type item model
    def find_by_name(cls, name, ):
        return cls.query.filter_by(name=name).first()  # use cls because it is a class method
        # return ItemModel.query.filter_by(name=name)
        # SAME AS ABOVE: SELECT * FROM items WHERE name=name
        # return ItemModel.query.filter_by(name=name).first()
        # SAME AS ABOVE: SELECT * FROM items WHERE name=name LIMIT 1 - returns first row only

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # This method serves as an insert and as an update

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
