from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256 as sha256
import re



users = [{
        "username":"Spongebob",
        "email": "spongebobsquarepants@bikinibottom.sea",
        "password": sha256.hash("CrustyKr1abs")
    }
]

class User:
    '''models for the users who have registered'''
    def register(username, email, hash):
        '''registers a new user'''
        userid = len(users)+1
        payload = {'username' : username, 'email' : email, 'password' : hash}
        users.append(payload)
        #users[userid] = payload
        #return users[userid]
        return users



    def single_user(email):
        '''Finds a single user, if not found, should return 404'''
        result = next((user for user in users if user['email'] == email), False)
        if result == False:
             return 'Not found'
        return result

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, email):
        result = next((user for user in users if user['email'] == email), False)
        if result == False:
            return Falses
        return sha256.verify(password, result['password'])

    # def signin(self, username, email, password):
    #     for
