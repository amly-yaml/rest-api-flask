
import os    # operation system can access environmental variable
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identify
from resources.items import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList

app = Flask(__name__)
# instead of sqlite, can be oracle, mysle, postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///mydatabase.db')  # 1st-Heroku postgres, 2nd-default sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # track the SQLalchemy
app.secret_key = "shwekyi"
api = Api(app)


jwt = JWT(app, authenticate, identify)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
    from db import db
    db.init_app(app)       # the flask app support with db
    app.run(debug=True)