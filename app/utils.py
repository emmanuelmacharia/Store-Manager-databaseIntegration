import re
from flask import jsonify


class Validator:
    '''validates the input from user'''
    def username_valid(username):
        '''vlidates the usename feild'''
        if username == "":
            return {"message": "Username cannot be null"}, 400
        return True

    def email_valid(email):
        '''vlidates the email feild'''
        if not re.search(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)", email):
            return {"message": "user must have a valid email"}

    def valid_password(password):
        pass


def product_valid(productname, description, category, quantity, price):
    if productname == "" or description == "" or category == "":
        return (
            {
                "message": """productname,descriprion and category are
                            required texts, please check your input"""
            },
            400,
        )
    elif not isinstance(quantity, int) or isinstance(price, int) is not True:
        return {
            "message": "kindly check your input,\
             the price and quantity MUST be numbers"
        }
    elif re.findall(r'"(.*?)"', (productname, descriprion, category)):
        return {"message": "kindly look over your input"}
    elif isinstance(quantity, str) is True or isinstance(price, str):
        try:
            num_list = [quantity, price]
            for num in num_list:
                int(num)
            return num
        except Exception as e:
            return {"message": "price and quantity must be numbers"}, e
    else:
        return True
