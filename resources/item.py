from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="Required Field"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="All Items Require A Store ID"
                        )

    @jwt_required()
    def get(self, name):  # retrieve items from DB
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item Not Found'}, 404  # if row doesnt exist

    def post(self, name):  # Writing Item to DB
        if ItemModel.find_by_name(name):
            return {'message': "Item with name '{}' already exists.".format(name)}, 400
        # data = request.get_json()  # force-True - Do not need content type header. silent-True, returns None
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {'message': 'An Error Occurred'}, 500  # 500 is internal server error

        return item.json(), 201  # code 200 means successful, 201 means crated (200 is most popular code) ,
        # 202 means accepted, 202 delays creation

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item Deleted'}

    def put(self, name):  # Put can insert new item or update itm - doesnt duplicate
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:  # Try to insert, given item doesnt exist
            item = ItemModel(name, **data)  # create a new one
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}
        # Alternative : return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
