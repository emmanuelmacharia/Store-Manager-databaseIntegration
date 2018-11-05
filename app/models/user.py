"""Handles all the user queries from the database"""


import json
from passlib.hash import pbkdf2_sha256 as sha256
from flask import Flask, jsonify, request
from ..models import dbconnect

conn = dbconnect()
cur = conn.cursor()


class User:
    '''user models'''
    def __init__(self, username, email, password, admin_role=False):
        self.username = username
        self.email = email
        self.password = password
        self.admin_role = admin_role

    def serializer(self):
        return dict(
            username=self.username,
            email=self.email,
            password=self.password,
            role=self.admin_role
        )

    def createadmin(username, email, password, admin_role=True):
        '''creates an autoadmin role'''
        conn = dbconnect()
        cur = conn.cursor()
        user = User.viewone(email)
        if not user:
            password = User.generate_hash(password)
            cur.execute("""INSERT INTO users (username, email, password, admin_role)
            VALUES('%s', '%s', '%s', '%s');"""
                        % (username, email,
                            password, admin_role))
        conn.commit()
        cur.close()

    def save(self, admin_role=False):
        """takes the data input from the user and saves it into the database"""
        query = (
            """INSERT INTO users (username, email, password, admin_role)
            VALUES('%s', '%s', '%s', '%s');"""
            % (self.username, self.email, self.password, self.admin_role)
        )
        cur.execute(query)
        conn.commit()

    @staticmethod
    def viewall():
        """queries the database to view all users"""
        cur.execute("SELECT * FROM users;")
        users = cur.fetchall()
        cur.close()
        return users

    @staticmethod
    def viewone(email):
        cur.execute("SELECT * FROM users WHERE email = '%s';" % (email))
        result = cur.fetchone()
        if result is None:
            return False
        else:
            return {"User": "{}".format(email)}
        cur.close()

    def ammend(self, email, admin_role=False):
        """method that updates data in the database"""
        query = "UPDATE users SET (%s)\
                WHERE email=(%s)" % (self.admin_role, self.email)
        cur.execute(query)
        conn.commit()
        cur.close()

    def delete(self, id):
        """method that deletes a record from the database"""
        query = "DELETE FROM users WHERE id=(%s);" % (id,)
        cur.execute(query)
        conn.commit()
        cur.close()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
