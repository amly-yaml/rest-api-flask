import sqlite3
from db import db
# create the class to store data
class ItemModel(db.Model):        # make the extend, SQLALchemy tell the class entity is here
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))   # precision=2 is two decimal places

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')    # single store, there could be more than one item related to the same store

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    # should stay class method, as it return as object of ItemModel
    @classmethod
    def find_by_name(cls, name):
        '''connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()
        if row is not None:
            return cls(row[0], row[1])  # name, price argument which give a item object
                    # cls(*row)
        '''
        return cls.query.filter_by(name=name).first()   # .query comes from db.Model that from the SQLAlchemy

    # can insert the data by using the object which created above
    #def insert(self):
    def save_to_db(self):   # insert itself
        '''connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()
        '''
        # this method perform both insert and update method
        # so that update function does not need anymore
        db.session.add(self)       # session is instance that the collection of object to write the database
        db.session.commit()

    '''def update(self):
        connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (self.name, self.price))  # pirority is important in SQL

        connection.commit()
        connection.close()
    '''

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
