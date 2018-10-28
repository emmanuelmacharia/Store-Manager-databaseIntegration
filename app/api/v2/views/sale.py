import re

from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import  create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity;

from ..models.sale import Sale

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('productname', required=True, help = "The productname is  required", type=str)
parser.add_argument('price', required=True, help = "The price is  required", type=str)
parser.add_argument('category', required=True, help = "The category is  required", type=str)
parser.add_argument('quantity', required=True, help = "The quantity is  required", type=int)

class Sales(Resource):
    '''defines the endpoints for sales'''
    def get(self):
        all_sales = Sale.viewall()
        return {"message":"Here's a list of all sales made", "all_sales":all_sales}
    def post(self):
        pass
    def delete(self):
        args = parser.parse_args()
        productname = args.get('productname')
        conn = dbconnect()
        cur = conn.cursor()
        item = cur.execute("SELECT * FROM sales WHERE productname = '%s';" %(productname))
        import pdb; pdb.set_trace()
        id = item[0]
        Sale.delete(id)
        return {"message":"{} has successfully been deleted".format(productname)}, 200
