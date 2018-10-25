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
        pass
    def delete(self):
        pass
