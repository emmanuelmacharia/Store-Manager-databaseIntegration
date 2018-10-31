
'''Endpoints for the user methods '''

import re
import datetime

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt, JWTManager
)

from ..models.user import User
from ..utils import user_valid

app = Flask(__name__)
api = Api(app)




blacklist = set()

class Users(Resource):
    """defines the get-all,post, and delete user methods"""

    def get(self):
        return User().viewall(), 200

    def post(self):
        data = request.get_json(force=True)
        username = data["username"]
        email = data["email"]
        password = data["password"]

        result = user_valid(username, email, password)
        if result == True:
            hash = User().generate_hash(password)
        else:
            return jsonify({'message':'please enter data in the right format'}), 400

        try:
            User().save(username, email, hash, admin_role=False)
            return {"message": "new user created"},201
        except Exception as e:
            return {"message": "Hmmm...something here's afoot"}, e, 404

    def delete(self):
        data = request.get_json()
        id = data['id']

        result = User()
        result.delete(id)


class Signin(Resource):
    """Allows the user to log into the system"""

    def post(self):
        """Endpoint for posting login information"""
        data = request.get_json(force=True)
        username = data["username"]
        email = data["email"]
        password = data["password"]

        result = user_valid(username, email, password)

        if result == True:
            User.generate_hash(password)

        user_exist = User().viewone(email)

        if user_exist == False:
            return {'message':'user does not exist'}
        if User.verify_hash(password, email) == True:
            # ac_token = create_access_token(identity=email)
            ac_token = create_access_token(identity=email, expires_delta = datetime.timedelta(hours=1))
            return dict(
                    message= 'User successfully logged in',
                    status= 'Success',
                    access_token= ac_token
               )
        else:
            return jsonify({'message': 'no user by that email, please check your credentials'}), 400
        
        return jsonify({'message':'signin successful'}), 200

    def get(self, email):
        '''gets a user by id'''
        data = request.get_json()
        email= data['email']
        return User().viewone(email)
        

class Logout(Resource):
    '''logs the user out and destroys token'''
    @jwt_required
    def delete(self):
        '''Logs the user out by balcklisting the token'''
        blacklist = set()
        print(get_raw_jwt())
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return {'message':'User logged out'}, 200
        