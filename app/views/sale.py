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

from ..models.sale import Sale
from ..models.product import Product
from ..models.__init__ import dbconnect

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument(
    "productname", required=True, help="The productname is  required", type=str
)
parser.add_argument("price", required=True, help="The price is  required", type=str)
parser.add_argument(
    "quantity", required=True, help="The quantity is  required", type=int
)


class Sales(Resource):
    """defines the endpoints for sales"""

    def get(self):
        all_sales = Sale().viewall()
        return {"message": "Here's a list of all sales made", "all_sales": all_sales}

    def post(self):
        """Allows an attendant to create a new sales record"""
        args = parser.parse_args()
        productname = args.get("productname")
        quantity = args.get("quantity")
        price = args.get("price")
        conn = dbconnect()
        cur = conn.cursor()

        query = "SELECT * FROM products WHERE productname = '%s'; " % (productname)
        cur.execute(query)
        record = cur.fetchone()
        if record == None:
            return (
                {
                    "message": "No product by that name in the inventory,check your input"
                },
                404,
            )
        elif quantity > int(record[4]):
            return (
                {
                    "message": "Request exeeds the quantity of the {} in our inventory".format(
                        productname
                    )
                },
                400,
            )
        else:
            newsale = Sale().save(productname, price, quantity)
            return make_response(
                jsonify({"message": "sale made successfully", "sale record": newsale}),
                201,
            )

    def delete(self):
        args = parser.parse_args()
        productname = args.get("productname")
        conn = dbconnect()
        cur = conn.cursor()
        item = cur.execute(
            "SELECT * FROM sales WHERE productname = '%s';" % (productname)
        )
        import pdb

        pdb.set_trace()
        id = item[0]
        Sale.delete(id)
        return {"message": "{} has successfully been deleted".format(productname)}, 200
