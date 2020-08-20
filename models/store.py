import sqlite3
from db import db
# create the class to store data
class StoreModel(db.Model):        # make the extend, SQLALchemy tell the class entity is here
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')     # list of model because many-to-one relationship, many items with same store_id

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [x.json() for x in self.items.all()]}

    # should stay class method, as it return as object of ItemModel
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()   # .query comes from db.Model that from the SQLAlchemy

    # can insert the data by using the object which created above
    #def insert(self):
    def save_to_db(self):   # insert itself
        db.session.add(self)       # session is instance that the collection of object to write the database
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
