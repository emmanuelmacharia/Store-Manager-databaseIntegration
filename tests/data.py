# DATA  FOR TESTING

user_information = {
            "username": "Spongebob",
            "email": "spongebobsquarepants@bikinibottom.sea",
            "password": "CrustyKr1abs"
        }

test_valid_product = {
            "name": "hp",
            "description": "elite",
            "category": "computers",
            "quantity": 10,
            "price": 50000
            }

test_empty_username = {
            "username": "",
            "email": "user@inlook.com",
            "password": "fdkff5A"
            }
test_empty_email = {
            "username": "user",
            "email": "",
            "password": "fdkff5A"
            }
test_empty_password = {
            "username": "user",
            "email": "solomarsha@outlook.com",
            "password": ""
            }
test_invalid_password = {
            "username": "user",
            "email": "solomarsha@outlook.com",
            "password": "pass"
            }
test_valid_input = {
            "username": "user",
            "email": "solomarsha@outlook.com",
            "password": "pass1Word"
            }
test_login_success = {
            "username": "user",
            "email": "solomarsha@outlook.com",
            "password": "pass1Word"
            }

registration_url = '/api/v2/auth/signup'
login_url = '/api/v2/auth/login'
sales_url = '/api/v2/sales'
products_url = '/api/v2/products'
single_product_url = '/api/v2/product/1'
not_found_single_product_url = '/api/v2/product/100000'
single_sale_url = 'api/v2/sale/1'
not_found_single_sale_url = 'api/v2/sale/1000000'
