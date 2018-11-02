"""Endpoints for the user methods """

import re
import datetime

from functools import wraps

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
    JWTManager,
)


from ..models.user import User
from ..utils import Validator

app = Flask(__name__)
api = Api(app)


blacklist = set()


class Users(Resource):
    """defines the get-all,post, and delete user methods"""

    def get(self):
        users = User.viewall()
        all_users = []
        for user in users:
            uservalue = {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'password': user[3],
                'admin_role': user[-1]
            }
        all_users.append(uservalue)
        return {'users': all_users}, 200

    def post(self):
        data = request.get_json()
        username = data["username"]
        email = data["email"]
        password = data["password"]

        validusername = Validator.username_valid(username)
        validemail = Validator.email_valid(email)
        validpassword = Validator.valid_password(password)
        
        if not validusername:
            return {"message": "Username cannot be null"}, 400
        elif validemail:
            return {"message": "user must have a valid email"}, 400
        elif validpassword:
            return{
                    "message": "user must have a valid password"
                }, 400
        else:
            hash = User.generate_hash(password)

        user_exist = User.viewone(email)
        if user_exist:
            return{
                "message":
                """Email exists,register with a different email, or sign in"""
                }, 400
        else:
            try:
                User(username, email, hash).save()
                return {"message": "new user created"}, 201
            except Exception as e:
                return e, 404

    def delete(self):
        data = request.get_json()
        id = data["id"]

        result = User(username, email, password)
        result.delete(id)


class Signin(Resource):
    """Allows the user to log into the system"""

    def post(self):
        """Endpoint for posting login information"""
        data = request.get_json(force=True)
        username = data["username"]
        email = data["email"]
        password = data["password"]
        validusername = Validator.username_valid(username)
        validemail = Validator.email_valid(email)
        validpassword = Validator.valid_password(password)
        
        if not validusername:
            return {"message": "Username cannot be null"}, 400
        elif validemail:
            return {"message": "user must have a valid email"}, 400
        elif validpassword:
            return{
                    "message": "user must have a valid password"
                }, 400
        else:
            hash = User.generate_hash(password)

        user_exist = User.viewone(email)

        if user_exist is False:
            return {"message": "user does not exist"}
        if User.verify_hash(password, hash) is True:
            ac_token = create_access_token(
                identity=email, expires_delta=datetime.timedelta(days=90)
            )
            return dict(
                message="User successfully logged in",
                status="Success",
                access_token=ac_token,
            )
        else:
            return (
                jsonify(
                    {"message":
                        "no user by that email, please check your credentials"}
                ),
                400,
            )

        return jsonify({"message": "signin successful"}), 200

    def get(self, email):
        """gets a user by id"""
        data = request.get_json()
        email = data["email"]
        return User(username, email, password).viewone(email)


class Logout(Resource):
    """logs the user out and destroys token"""

    @jwt_required
    def post(self):
        """Logs the user out by balcklisting the token"""
        blacklist = set()
        try:
            jti = get_raw_jwt()["jti"]
            blacklist.add(jti)
            return {"message": "User logged out"}, 200
        except Exception as e:
            return {'message': 'No Authorization header provided'}, e, 404
