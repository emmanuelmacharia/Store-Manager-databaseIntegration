import re
# from views import User, Product, sale

def user_valid(username, email, password):
    if username == '' :
        return {'message':'Username cannot be null'}, 400
    elif not re.search (r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)", email):
         return {'message':'user must have a valid email'},400
    elif len(password)<6 and re.search('[a-zA-Z0-9]+', password) is not True:
        return {'message':'user must have a valid password(at least 6 characters, with lowercase, uppercase and integers)'},400
    else:
        return True
