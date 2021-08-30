from db import db


class ItemModel(db.Model):
    # ItemModel extends db.Model - tells SQLAlchemy entity that this class are things we will be saving and retrieving
    # from a database, creates mapping between database and objects

    # Tell SQLAlchemy the table name where the models will be stored.. ie Users
    __tablename__ = 'items'
    # What columns the table contains?
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):  # return json representation of model - A dictionary of item
        return {'id': self.id, 'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod  # Returns object of type item model
    def find_by_name(cls, name,):
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

