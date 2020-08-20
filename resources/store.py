from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):   # extend resource class

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "Store name '{}' does not exist.".format(name)}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "Store name '{}' already existed.".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': "An error occurred inserting the store name"}, 500
        return store.json(), 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': "Store name '{}' deleted".format(name)}
        return {'message': "Store name '{}' not exists.".format(name)}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}