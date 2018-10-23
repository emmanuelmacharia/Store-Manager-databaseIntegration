import unittest
from app import create_app
import json

#remember to change the urls for these methods
class TestProductApis(unittest.TestCase):
    '''tests all the endpoints created for the store manager application'''
    def setUp(self):
        self.app = create_app('testing').test_client()
        self.test_valid_sale = {'saleid':1, 'productname': 'Hp', 'description': 'elite', 'quantity': 1, 'price': 5000}
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


    def test_get_admin_sales(self):
        '''Tests the get (view all) sales method for the admin, asserts true if the test passes and gives a status code of 200'''
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v1/admin/sales',
                                    headers=dict(Authorization="Bearer " + test_user),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_attendant_sales(self):
        test_user= self.register()
        test_user= self.signin()
        '''Tests the get (view all) sales method by the attendant for the attendant, assets true if the test passes and gives the status code of 200'''
        response = self.app.get('api/v1/attendant/sales',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_single_sale_found(self):
        '''Tests whether the sale with the id provided is there, returns status_code 404'''
        #newsale = {'saleid':1, 'productname': 'Hp', 'description': 'elite', 'quantity': 1, 'price': 5000}
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v1/attendant/sales',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    data = json.dumps(self.test_valid_sale), content_type = 'application/json')
        response = self.app.get('api/v1/admin/sales/1',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_post_sales(self):
        '''Tests whether the attendant can successfully create a new sale record (POST method); asserts true if the test passes and status code = 201'''
        #newsale = {'productname': 'Hp', 'description':'elite x', 'quantity': 1, 'price': 5000}
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v1/attendant/sales',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    data = json.dumps(self.test_valid_sale),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 201)


    def test_no_sale_found(self):
        '''Tests for non existent items'''
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v1/admin/sales/10',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 404)





if __name__ == '__main__':
    unittest.main(exit= False)
