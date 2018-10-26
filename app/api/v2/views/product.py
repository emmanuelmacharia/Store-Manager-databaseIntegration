import re

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import  create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity;

from ..models.product import Products

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
class Products(Resource):
    '''defines the get, post, put and delete methods for products'''
    def post(self):
        pass

    def put(self):
        pass

    def get(self):
        return jsonify({"products":Products.viewall()}), 200

    def delete(self):
        id = parser.add_argument('id', type=int, help='id must be an integer')
        args = parser.parse_args()
        # data = request.get_json()
        # id = data['id']

        if isinstance(args, int) == False:
            return {'message':'id can only be an integer'}, 400
        else:
            result = Products()
            result.delete(args)
