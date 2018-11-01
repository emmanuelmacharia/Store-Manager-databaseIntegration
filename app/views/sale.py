import re
import datetime

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
from ..views.product import Products

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument(
    "productname", required=True, help="The productname is  required", type=str
)
parser.add_argument(
    "price", required=True, help="The price is  required", type=int
    )
parser.add_argument(
    "quantity", required=True, help="The quantity is  required", type=int
)
parser.add_argument(
    "attendant", required=True,
    help="The attendant username is required", type=str
)


class Sales(Resource):
    """defines the endpoints for sales"""
    @jwt_required
    def get(self):
        all_sales = Sale.viewall(self)
        return all_sales

    @jwt_required
    def post(self):
        """Allows an attendant to create a new sales record"""
        args = parser.parse_args()
        productname = args.get("productname")
        quantity = args.get("quantity")
        price = args.get("price")
        attendant = args.get('attendant')
        conn = dbconnect()
        cur = conn.cursor()

        query = """SELECT * FROM products
                WHERE productname = %s; """
        cur.execute(query, (productname, ))
        record = cur.fetchone()
        if record is None:
            return jsonify(
                {
                    "message": "No product by that name in the inventory"
                },
                404,
            )
        elif quantity > int(record[4]):
            return (
                {
                    "message": """Request exeeds the quantity of the
                                {} in our inventory""".format(
                        productname
                    )
                },
                400,
            )
        else:
            date_sold = datetime.datetime.now()
            newsale = Sale(attendant, productname, quantity, price,
                           date_sold)
            Products.put(self)
            newsale.save()
            sale = newsale.serializer()
            return {"sale record": sale}, 201

    @jwt_required
    def delete(self):
        args = parser.parse_args()
        productname = args.get("productname")
        conn = dbconnect()
        cur = conn.cursor()
        item = cur.execute(
            "SELECT * FROM sales WHERE productname = %s;", (productname)
        )
        id = item[0]
        Sale.delete(id)
        return {
            "message": "{} has successfully been deleted"
            .format(productname)}, 200
