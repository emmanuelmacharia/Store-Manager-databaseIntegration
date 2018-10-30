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
parser.add_argument("price", required=True, help="The price is  required", type=str)
parser.add_argument(
    "category", required=True, help="The category is  required", type=str
)
parser.add_argument(
    "quantity", required=True, help="The quantity is  required", type=int
)


class Products(Resource):
    """defines the get, post, put and delete methods for products"""
    @jwt_required
    def post(self):
        args = parser.parse_args()
        productname = args.get("productname")
        description = args.get("description")
        category = args.get("category")
        quantity = args.get("quantity")
        price = args.get("price")
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM products WHERE productname='%s';" % (productname)
        )
        dup = cur.fetchall()
        if dup == None:
            created = Product().save(productname, description, category, quantity, price)
            return jsonify({'product':created})
        else:
            return Product.modifyquantity(quantity, productname), 202

    @jwt_required
    def put(self):
        args = parser.parse_args()
        productname = args.get("productname")
        description = args.get("description")
        category = args.get("category")
        quantity = args.get("quantity")
        price = args.get("price")
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE productname= %s;" % (productname))
        result = cur.fetchone()
        if result == None:
            return {"message": "product does not exist, please check your input"}, 400
        else:
            productname = result[1]
            description = result[2]
            category = result[3]
            quantity += int(result[4])
            price = result[-1]
            # pars = [productname, description, category, quantity, price]
            updated = cur.execute(
                "UPDATE products SET quantity = %s WHERE productname = '%s';"
                % (quantity, productname)
            )
            cur.close()
            conn.commit()
            return make_response(
                jsonify(
                    {"message": "product successfully updated", "product": product}
                ),
                202,
            )
    @jwt_required
    def get(self):
        """Allows a user to get all products in the inventory"""
        all_products = Product().viewall()
        return all_products

    @jwt_required
    def delete(self):
        """Allows a admin to delete a product from the inventory"""
        args = parser.parse_args()
        productname = args.get("productname")
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE productname = '%s';" % (productname))

        item = cur.fetchone()
        if item == None:
            {"message": "the product requested does not exist"}, 404
        else:
            id = item[0]
            return Product.delete(id)

        # id = parser.add_argument('id', type=int, help='id must be an integer')
        # args = parser.parse_args()
        # if isinstance(args, int) == False:
        #     return {'message':'id can only be an integer'}, 400
        # else:
        #     result = Products()
        #     result.delete(args)


class SingleProduct(Resource):
    """Endpoints pertaining to methods that couldnt be in the Products class"""
    @jwt_required
    def get(self, id):
        """Allows a user to view one single product"""
        return Product().viewone(id)
