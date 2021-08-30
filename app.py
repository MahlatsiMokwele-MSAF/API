from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# SQLALCHEMY database exists at the root folder of our project
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Turns off Flask SQLALCHEMY_TRACK_MODIFICATIONS but does not turn off SQLALCHEMY SQLALCHEMY_TRACK_MODIFICATIONS tracker
app.config['PROPAGATE_EXCEPTIONS'] = True
# Allows flask extensions to raise their own exceptions
app.secret_key = 'jose'  # app.config['JWT_SECRET_KEY']
api = Api(app)

jwt = JWTManager(app)  # creates new end port : /auth. When called, we send username & password

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  # https://127.0.0.1:5000/item/car
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':  # if main, run the app. if not, don't run app
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
