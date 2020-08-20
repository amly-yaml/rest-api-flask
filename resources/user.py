# this class is going to store the user data such as id, username and password to login and signup
# this is the sign up
import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
# add the ability to retrieve the user object


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be black.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be black.")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']) is not None:
            return {'message': "This username '{}' is already existed.".format(data['username'])}

        '''connection = sqlite3.connect('mydatabase.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()

        connection.close()
        '''
        user = UserModel(**data)
        user.save_to_database()

        return {'message': "User register successfully"}, 201