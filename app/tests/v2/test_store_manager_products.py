
import unittest
from app import create_app
import json
from baseTest import BaseTestClient


class TestProducts(BaseTestClient):

    def test_get_all_products(self):
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v2/admin/products'
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 200)

    def test_post_products(self):
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v2/admin/products'
                                    'api/v2/admin/products',
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    data = json.dumps(self.test_valid_product),
                                    content_type = 'application/json'
                                    )
        self.assertEqual(response.status_code, 201)

    def test_single(self):
        test_user= self.register()
        test_user= self.signin()
        response = self.app.get('api/v2/products/1'
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json'
                                    )

        self.assertEqual(response.status_code, 200)

    def test_no_products_found(self):
        test_user= self.register()
        test_user= self.signin()
        response = self.app.post('api/v2/admin/products'
                            headers=dict(Authorization="Bearer " + self.signin()),
                            data = json.dumps(self.test_valid_product),
                            content_type = 'application/json'
                                    )
        response = self.app.get('api/v2/products/100'
                                    headers=dict(Authorization="Bearer " + self.signin()),
                                    content_type = 'application/json'
                                )
        self.assertEqual(response.status_code, 401)

    def test_validator_products(self):
        test_user= self.register()
        test_user= self.signin()
        pass

if __name__ == '__main__':
unittest.main(exit= False)
