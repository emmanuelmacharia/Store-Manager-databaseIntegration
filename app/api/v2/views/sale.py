import re

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import  create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity;

from ..models.sale import Sale

app = Flask(__name__)
api = Api(app)

class Sales(Resource):
    '''defines the endpoints for sales'''
    def get(self):
        pass
    def post(self):
        pass
    def delete(self):
        pass
