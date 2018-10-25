import re

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import  create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity;

from models import Products

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    '''defines the get, post, put and delete methods for products'''
    def post(self):
        pass
    def put(self):
        pass

    def get(self):
        return Products.viewall()

    def delete(self):
        data = request.get_json()
        id = data['id']

        if isinstance(id) == False:
            return {'message':'id can only be an integer'}, 400
        else:
            result = Products()
            result.delete(id)
