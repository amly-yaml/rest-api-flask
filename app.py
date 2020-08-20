from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identify
from resources.items import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'   # instead of sqlite, can be oracle, mysle, postgresql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # track the SQLalchemy
app.secret_key = "shwekyi"
api = Api(app)


@app.before_first_request   #effect the method below it, run the method before the first request into this app
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identify)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
    db.init_app(app)       # the flask app support with db
    app.run(debug=True)