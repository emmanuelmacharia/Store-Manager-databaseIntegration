import re

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
)

from ..models.user import User
from .utils import user_valid

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    """defines the get-all,post, and delete user methods"""

    def get(self):
        return User.viewall(), 200

    def post(self):
        data = request.get_json(force=True)
        username = data["username"]
        email = data["email"]
        password = data["password"]

        result = user_valid(username, email, password)
        if result == True:
            hash = User.generate_hash(password)
        else:
            return "please enter data in the right format", 400

        try:
            new_user = User.save(username, email, hash, admin_role=False)
            ac_token = create_access_token(identity=data["email"])
            new_token = create_refresh_token(identity=data["email"])
            return (
                {
                    "message": "new user created",
                    "access_token": ac_token,
                    "refresh_token": new_token,
                },
                201,
            )
        except Exception as e:
            return {"message": "Hmmm...something here's afoot"}, e, 404

    def delete(self):
        id = parser.add_argument("id", type=int, help="id must be an integer")
        args = parser.parse_args()

        result = Products()
        result.delete(args)


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

        session = User.viewone(email)
        if session == False:
            return (
                {
                    "message": "Username, {}, email, {} or password dont seem to exist".format(
                        username, email
                    )
                },
                400,
            )

        if User.verify_hash(password, email) == True:
            ac_token = create_access_token(identity=email)
            new_token = create_refresh_token(identity=email)
            return (
                {
                    "message": "User successfully logged in",
                    "status": "Success",
                    "access_token": ac_token,
                    "refresh_token": new_token,
                },
                200,
            )
        else:
            return (
                {"message": "no user by that email, please check your credentials"},
                400,
            )
