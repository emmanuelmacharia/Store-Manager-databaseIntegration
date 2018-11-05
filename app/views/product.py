""" Handles the Product views """
import re

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
)

from ..models.product import Product
from ..models.user import User
from ..models.__init__ import dbconnect

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument(
    "productname", required=True, help="The productname is  required", type=str
)
parser.add_argument(
    "description", required=True, help="The description is  required", type=str
)
parser.add_argument(
    "price", required=True, help="The price is  required", type=str
    )
parser.add_argument(
    "category", required=True, help="The category is  required", type=str
)
parser.add_argument(
    "quantity", required=True, help="The quantity is  required", type=int
)


class Products(Resource):
    """defines the get, post, put and delete methods for products"""
    # @jwt_required
    def post(self):
        # user = User.viewone(get_jwt_identity())
        # if user is not True:
        #     return {'message': 'Not authorized. Only admins can access this'}
        args = parser.parse_args()
        productname = args.get("productname")
        description = args.get("description")
        category = args.get("category")
        quantity = args.get("quantity")
        price = args.get("price")
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM products
                    WHERE productname= %s """, (productname, ))
        dup = cur.fetchall()
        print(dup)
        if len(dup) < 1:
            Product(productname, description,
                    category, quantity, price).save()
            return{"product": 'created'}, 201
        else:
            return {'message': 'product already exists'}, 400

    @jwt_required
    def put(self):
        user = User.viewone(get_jwt_identity())
        if user is not True:
            return {'message': 'Not authorized. Only admins can access this'}
        args = parser.parse_args()
        productname = args.get("productname").strip()
        description = args.get("description")
        category = args.get("category")
        quantity = args.get("quantity")
        price = args.get("price")
        Product(productname, description, category, quantity, price)
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM products
                    WHERE productname= %s""", (productname, ))
        result = cur.fetchone()
        if not result:
            return {
                "message": "product does not exist, please check your input"
                }, 400
        updated = Product.ammend(productname, description,
                                 category, quantity, price)
        return {'message': 'updated'}, 202

    @jwt_required
    def get(self):
        """Allows a user to get all products in the inventory"""
        all_products = Product.viewall(self)
        return all_products


class SingleProduct(Resource):
    """Endpoints pertaining to methods that couldnt be in the Products class"""
    @jwt_required
    def get(self, id):
        """Allows a user to view one single product"""
        return Product.viewone(id)

    @jwt_required
    def delete(self, id):
        """Allows a admin to delete a product from the inventory"""
        user = User.viewone(get_jwt_identity())
        if user is not True:
            return {'message': 'Not authorized. Only admins can access this'}
        return Product.delete(id)
