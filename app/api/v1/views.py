from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from .models import User, users
import re;
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, jwt_refresh_token_required, get_jwt_identity;

#from flask_jwt import JWT, jwt_required


app  = Flask(__name__)
api = Api(app)


products = {}

class AdminProducts(Resource):
    '''Endpoints for creating and viewing products in the application'''

    @jwt_required
    def get(self):
        '''Views all the products in the application'''
        return jsonify({'products':products})

    @jwt_required
    def post(self):
        '''Creates a new product in the store'''
        can_post = True
        if can_post:
            id = len(products)+1
            data = request.get_json()
            name = data['name']
            description = data['description']
            category = data['category']
            price = data['price']

            payload = {'name': name, 'description': description, 'category': category, 'price': price}

            if len(data) > 5 and 'name' and 'description' and 'category' and 'quantity' and 'price' not in data.keys() and 'quantity'.isint():
                return ('Can take only 5 arguments; name, description, category, quantity, price')

            for item in products.values():
                for i in item.values():
                    if i == data['name']:
                        product.values()['quantity'] += data['quantity']

            products[id] = payload

            return products, 201

        return 'User not allowed to create a product'

class AttendantProducts(Resource):

    '''endpoints for viewing all the products in the inventory by the attendant'''

    @jwt_required
    def get(self):
        '''Views all the products in the application'''
        attendant_products = AdminProducts.get(self)
        return attendant_products

class Product(Resource):
    '''Endpoint that allows a user to view a single product'''

    @jwt_required
    def get(self, id):
        '''view a single product'''
        if id in products:
            return products[id], 200
        return 'Not found', 404


sales ={}

class AttendantSales(Resource):
    '''endpoint for creating and viewing sales'''
    @jwt_required
    def get(self):
        '''views all sales made by the attendant'''
        return jsonify({'sales':sales})

    @jwt_required
    def post(self):
        '''Creates a new sale by the attendant'''
        id = len(sales)+1
        data = request.get_json()

        price = data['price']
        quantity = data['quantity']
        productname = data['productname']
        description = data['description']
        payload = { 'productname': productname, 'description':description, 'quantity': quantity , 'price': price }

        for item in payload.values():
            if item in products.values():
                for i in products.values():
                    if data['quantity'].isint() and products.values()['quantity'] >= data['quantity']:
                        products.values()['quantity'] - data['quantity']
                    else:
                        return 'the product {} is almost out / not in stock at the moment. please check the quantity of the product again.Only {} are left'.format(sales.values()['productname'], products.values()['quantity'])
            else:
                return "there's no {}. please check your input".format(sales.values()['productname'])

        sales[id] = payload


        return sales, 201


class AdminSale(Resource):

    '''Endpoints for viewing sales by Admin'''

    @jwt_required
    def get(self):
      '''views all sales made by the attendants'''
      allsales = AttendantSales.get(self)
      return allsales

class Sale(Resource):
    '''Endpoint for viewing a single sale'''

    @jwt_required
    def get(self, id):
        '''views single sale'''
        if id not in sales.keys():
            return 'Not Found', 404
        else:
            return sales[id] ,200

class Register(Resource):
    '''Endpoint for registation of a new user'''
    def post(self):
        '''creates a new user'''

        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']

        if username == '' :
            return {'message':'Username cannot be null'}, 400
        elif not re.search (r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)", email):
             return {'message':'user must have a valid email'},400
        elif len(password)<6 and re.search('[a-zA-Z0-9]+', password) is not True:
            return {'message':'user must have a valid password(at least 6 characters, with lowercase, uppercase and integers)'},400
        hash = User.generate_hash(password)
        try:
            new_user = User.register(username, email, hash)
            print(users)
            ac_token = create_access_token(identity = data['email'])
            new_token = create_refresh_token(identity = data['email'])
            return {'message': 'new user created','access_token':ac_token,'refresh_token':new_token}, 201
        except:
            return {'message':'Hmmm...something here\'s afoot'}, 404


class Login(Resource):
    '''Endpoint for logging in'''
    def post(self):
        '''Endpoint for posting login information'''
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        if not username :
            return {'message':'Username cannot be null'}, 400
        elif not re.search (r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)", email):
             return {'message':'user must have a valid email'},400
        elif len(password)<6 and re.search('[a-zA-Z0-9]+', password) is not True:
            return {'message':'user must have a valid password(at least 6 characters, with lowercase, uppercase and integers)'},400
        User.generate_hash(password)
        session = User.single_user(email)
        if session == 'Not found':
            return {'message': 'Username, {}, email, {} or password dont seem to exist'.format(username, email)}, 400
        if User.verify_hash(password, email) == True:
            ac_token = create_access_token(identity = email)
            new_token = create_refresh_token(identity = email)

            return {
                'message':'User successfully logged in',
                'status': 'Success',
                'access_token':ac_token,
                'refresh_token': new_token
            }, 200
        return {'message': 'no user by that email, please check your credentials'}, 400
