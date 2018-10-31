import unittest
from app import create_app
import json
from .baseTest import BaseTestClient

class TestSale(BaseTestClient):
    def test_get_admin_sales(self):
        '''Tests the get (view all) sales method for the admin, asserts true if the test passes and gives a status code of 200'''
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v2/sales',
                                    headers=dict(Authorization="Bearer " + test_user),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_attendant_sales(self):
        test_user= self.register()
        test_user= self.signin()
        '''Tests the get (view all) sales method by the attendant for the attendant, assets true if the test passes and gives the status code of 200'''
        response = self.app.get('api/v2/sales',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_single_sale_found(self):
        '''Tests whether the sale with the id provided is there, returns status_code 404'''
        #newsale = {'saleid':1, 'productname': 'Hp', 'description': 'elite', 'quantity': 1, 'price': 5000}
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v2/sales',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    data = json.dumps(self.test_valid_sale), content_type = 'application/json')
        response = self.app.get('api/v2/sales/1',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_post_sales(self):
        '''Tests whether the attendant can successfully create a new sale record (POST method); asserts true if the test passes and status code = 201'''
        #newsale = {'productname': 'Hp', 'description':'elite x', 'quantity': 1, 'price': 5000}
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v2/sales',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    data = json.dumps(self.test_valid_sale),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 201)


    def test_no_sale_found(self):
        '''Tests for non existent items'''
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v2/sales/10000',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json')
        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main(exit= False)
