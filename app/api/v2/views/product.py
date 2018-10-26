import re

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import  create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity;

from ..models.product import Product
from ..models.__init__ import dbconnect

app = Flask(__name__)
api = Api(app)

#productname,description, category, quantity, price
parser = reqparse.RequestParser()
parser.add_argument('productname', required=True, help = "The productname is  required", type=str)
parser.add_argument('description', required=True, help = "The description is  required", type=str)
parser.add_argument('price', required=True, help = "The price is  required", type=str)
parser.add_argument('category', required=True, help = "The category is  required", type=int)
parser.add_argument('quantity', required=True, help = "The quantity is  required", type=int)

class Products(Resource):
    '''defines the get, post, put and delete methods for products'''
    def post(self):
        args= Products.parser.parse_args()
        productname = args.get('productname')
        description = args.get('description')
        category = args.get('category')
        quantity = args.get('quantity')
        price = args.get('price')
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM products WHERE productname=%s"(productname))
        result = cur.fetchone()
        if result == None:
            created = Products.save(productname, description, category, quantity, price)
            return make_response(jsonify({'message': 'product successfully created', 'product':created}), 201)
        else:
            productname = result[0]
            description = result[1]
            category = result[2]
            quantity += result[3]
            price = result[-1]
            updated = cur.execute('UPDATE products SET %s WHERE productname = %s'(quantity, productname))
            cur.close()
            conn.commit()
            return make_response(jsonify({'message': 'product successfully updated', 'product':updated}), 201)


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
