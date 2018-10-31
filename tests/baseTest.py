
import unittest
from app import create_app
import json
from app.views.product import Products, SingleProduct
from app.views.sale import Sales
from app.views.user import Users, Signin, Logout
from app.models import dbconnect, droptables, createTables

class BaseTestClient(unittest.TestCase):
    '''the base test configurations for the entire application'''

    def setUp(self):
        '''creates the data required in the tests. also connects to the test database where the data will be stored'''
        self.app = create_app('testing').test_client()
        test = dbconnect()
        createTables()

        self.user_information = {
            "username":"Spongebob",
            "email": "spongebobsquarepants@bikinibottom.sea",
            "password": "CrustyKr1abs"
        }

        self.test_valid_product = {
            "name" : "hp",
            "description" : "elite",
            "category" : "computers",
            "quantity" : 10,
            "price" : 50000
            }

        self.test_empty_username= {
            "username":"",
            "email":"user@inlook.com",
            "password": "fdkff5A"
            }
        self.test_empty_email = {
            "username":"user",
            "email":"",
            "password": "fdkff5A"
            }
        self.test_empty_password = {
            "username":"user",
            "email":"solomarsha@outlook.com",
            "password": ""
            }
        self.test_invalid_password = {
            "username":"user",
            "email":"solomarsha@outlook.com",
            "password": "pass"
            }
        self.test_valid_input= {
            "username":"user",
            "email":"solomarsha@outlook.com",
            "password": "pass1Word"
            }
        self.test_login_success = {
            "username":"user",
            "email":"solomarsha@outlook.com",
            "password": "pass1Word"
            }


        self.registration_url = '/api/v2/auth/signup'
        self.login_url = '/api/v2/auth/login'
        self.sales_url = '/api/v2/sales'
        self.products_url = '/api/v2/products'
        self.single_product_url = '/api/v2/product/1'
        self.not_found_single_product_url = '/api/v2/product/100000'
        self.single_sale_url = 'api/v2/sale/1'
        self.not_found_single_sale_url = 'api/v2/sale/1000000'


    def register(self):
        '''registers the test client user'''
        test_register = self.app.post(self.registration_url, data= json.dumps(
                                        dict(self.user_information)),
                                        content_type = 'application/json')

        return json.loads(test_register.data.decode())["access_token"]

    def signin(self):
        '''signs the test client in so that we can run our tests'''
        test_signin = self.app.post(self.login_url, data = json.dumps(
                                    dict(self.user_information )),
                                    content_type='application/json')
        return json.loads(test_signin.data.decode())["access_token"]

    def tearDown(self):
        droptables()
        curtest.close()