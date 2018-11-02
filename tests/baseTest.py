import unittest
from app import create_app
import json
from app.views.product import Products, SingleProduct
from app.views.sale import Sales
from app.views.user import Users, Signin, Logout
from app.models import dbconnect, droptables, createTables
from .data import *


class BaseTest(unittest.TestCase):
    '''the base test configurations for the entire application'''
    def setUp(self):
        '''creates the data required in the tests.
        also connects to the test database where the data will be stored'''
        self.app = create_app('testing')
        self.app.test_client()
        conn = dbconnect()
        cur = conn.cursor()
        createTables()

    def register(self):
        '''registers a new user'''
        tester = self.app.post(
            registration_url, data.json.dumps(
                dict(
                    user_information
                )
            ), content_type='application/json'
        )
        return 'signed up'

    def login(self):
        '''log the test user in'''
        tester = self.app.post(
            login_url, data=json.dumps(dict(
                user_information
            )), content_type='application/json'
        )
        return json.loads(tester.data.decode())["access_token"]

    def tearDown(self):
        '''Terminates connection to database, and cursor'''
        droptables()
        self.cur.close()
