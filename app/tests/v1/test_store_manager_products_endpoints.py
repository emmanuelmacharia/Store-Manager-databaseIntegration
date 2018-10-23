import unittest
from app import create_app
import json



#remember to change the urls for these methods
class TestProductApis(unittest.TestCase):
    '''tests all the endpoints created for the store manager application'''
    def setUp(self):
        self.app = create_app('testing').test_client()
        self.test_valid_product = {"name" : "hp", "description" : "elite", "category" : "computers", "quantity" : 10, "price" : 50000}

    def register(self):
        '''registers the test client user'''
        test_register = self.app.post('api/v1/register', data= json.dumps(
                                        dict(username = 'Spongebob', email = 'spongebobsquarepants@bikinibottom.sea', password = 'CrustyKr1abs')),
                                        content_type = 'application/json')

        return json.loads(test_register.data.decode())["access_token"]

    def signin(self):
        '''signs the test client in so that we can run our tests'''
        test_signin = self.app.post('api/v1/login', data = json.dumps(
                                    dict(username = 'Spongebob', email = 'spongebobsquarepants@bikinibottom.sea', password = 'CrustyKr1abs')),
                                    content_type='application/json')
        return json.loads(test_signin.data.decode())["access_token"]


    def test_get_admin_products(self):
        '''Tests the get (view all) products method, asserts true if the test passes and gives a status code of 200'''
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v1/admin/products',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_attendant_products(self):
        '''Tests the get (view all) products method for the attendant, asserts true if the test passes and gives a status code of 200'''
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v1/attendant/products',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_products(self):
        '''Tests whether the admin can create a new product successfully; (POST method); asserts true if the test passes and gives a status code of 201'''
        #datapoint = {"name" : "hp", "description" : "elite", "category" : "computers", "quantity" : 10, "price" : 50000}
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v1/admin/products',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    data = json.dumps(self.test_valid_product),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_single_product(self):
        '''Tests for the get method to view a single product'''
        #datapoint ={"name" : "hp", "description" : "elite", "category" : "computers", "quantity" : 10, "price" : 50000}
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v1/admin/products',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    data = json.dumps(self.test_valid_product),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.get('api/v1/products/1',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_no_product_found(self):
        '''Tests for non existent items'''
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v1/products/100',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main(exit= False)
