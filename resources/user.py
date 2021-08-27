import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


# Resource - external representation of an entity

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Field is Required"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Field is Required"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):  # check if we have username existing in DB
            return {'message': 'User with that username already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message', 'User Created Successfully.'}, 201
