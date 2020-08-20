# extract the data from the database using the ItemModel class

from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):   # it users OOP
    parser = reqparse.RequestParser()  # initial the object can use the parser request
    # parser argument is only just for price passed in
    parser.add_argument('price',  # this is argument for json payload
        type=float,
        required=True,
        help="This field cannot be left black!")
    parser.add_argument('store_id',  # this is argument for json payload
                        type=int,
                        required=True,
                        help="Every item need the store id")

    # this is 'READ'
    @jwt_required()     # going to authenticate-login before the get method
    def get(self, name):    # get http, get only the specific item which is in the list of items
        # item = next(filter(lambda x: x['name'] == name, items), None) # going to filter the list of items that is in memory database
        # return {'item': item},  200 if item else 404   # 200 if item is not None else 404
        item = ItemModel.find_by_name(name)    # this is doing by the database
        if item is not None:
            return item.json()
        return {'message': "The item name '{}' does not exist.".format(name)}

    # separate method for using both get and post method
    # @classmethod
    # def find_by_name(cls, name):

    # this is post http that is the new 'create' for the items list,
    def post(self, name):      # error checking first
        if ItemModel.find_by_name(name) is not None:  # can also call Item.find_by_name(name)
            return {"Message": "An Item with the name {} already exit".format(name)}, 400

        data = Item.parser.parse_args()
        # item = {"name": name, "price": data["price"]}  # item dictionary
        item = ItemModel(name, data['price'], data['store_id'])   # item object

        try:
            item.save_to_db()
        except Exception:
            return {'message': "Insertion error occurred."}, 500 # internal server error

        return item.json(), 201

    # separate method to use for both post and put method
    # @classmethod
    # def insert(cls, item):


    # this is 'UPDATE'
    def put(self, name):
        data = Item.parser.parse_args()  # to parse the arguemts that come through JSON payload and put valid one in data
        # data = request.get_json()  # as creation the item, this line must put
        item = ItemModel.find_by_name(name)  # find the original name in database
        # updated_item = {'name': name, 'price': data['price']}  # updated item dictionary
        #updated_item = ItemModel(name, data['price'])      # updated item in object, ItemModel
        if item is None:    # not same, so none
            item = ItemModel(name, data['price'], data['store_id'])
            '''try:
                updated_item.insert()     # add new item in the database
            except:
                return {'message': "An error occurred in the insertion the item."}
                '''
            # items.append(item)       # add or put the new item in the list of items
        else:        # if user name same with the items list name, just update the price

            item.price = data['price']
            '''try:
                item.update()     # just update the data price
            except:
                return {'message': "An error occurred in the updated the item."}
            '''
        item.save_to_db()
        return item.json()    # return the item which is user request

    # this is 'DELETE'
    def delete(self, name):   # delete function
        # global method variable is the items variable in that block is also the outer items variable
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        # return {'message': "Item name '{}' deleted".format(name)}
        '''connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {'message': "Item name '{}' deleted".format(name)}
        '''
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': "Item name '{}' deleted".format(name)}
        return {'message': "Item name '{}' not found".format(name)}

        # items=[] and global items is same
        # return {'message': "Item name '{}' deleted".format(name)}

class ItemList(Resource):   # get all the items in the list
    def get(self):
        '''connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()
        return {'items': items}    # in front 'items' is key value
        '''
        return {'items': [x.json() for x in ItemModel.query.all()]}
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
