
import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(80))     # 80 is limit the size
    password = db.Column(db.String(80))

    def __init__(self, username, password):  # id is keyword so use _id
        #self.id = _id
        self.username = username
        self.password = password

    # this is using User class, but not use self, can use like
    @classmethod
    def find_by_username(cls, username):   # find a username in database
        '''connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        query = "SELECT  * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))   # this is tuple, ',' must put
        row = result.fetchone()    # get just first row

        if row is not None: # column 1,2,3
            # user = cls(row[0], row[1], row[2])     # using User class itself
            user = cls(*row)                        # passing a set of argument or positional argument
        else:
            user = None

        connection.close()
        return user
        '''
        return cls.query.filter_by(username=username).first()
        # query build, first username - table name, second username - argument
    @classmethod
    def find_by_id(cls, _id):
        '''connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row is not None:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
        '''
        return cls.query.filter_by(id=_id).first()

    def save_to_database(self):    # will do post endpoint using SQL-Alchemy
        db.session.add(self)
        db.session.commit()