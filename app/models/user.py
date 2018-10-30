"""Handles all the user queries from the database"""


import json
from passlib.hash import pbkdf2_sha256 as sha256
from flask import Flask, jsonify, request
from ..models import dbconnect


class User:
    def save(self, username, email, hash, admin_role=False):
        """takes the data input from the user and saves it into the database"""
        conn = dbconnect()
        cur = conn.cursor()
        query = (
            "INSERT INTO users (username, email, password, admin_role) VALUES('%s', '%s', '%s', '%s');"
            % (username, email, hash, admin_role)
        )
        cur.execute(query)
        conn.commit()
        cur.close()

    def viewall(self):
        """queries the database to view all users"""
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        cur.fetchall()
        cur.close()

    def viewone(self, email):
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = '%s';" % (email))
        result = cur.fetchone()
        if result == None:
            return False
        else:
            return True
        cur.close()

    def ammend(self, email, admin_role=False):
        """method that updates data in the database"""
        conn = dbconnect()
        cur = conn.cursor()
        query = "UPDATE users SET (%s) WHERE email=(%s)" % (admin_role, email)
        cur.execute(query)
        conn.commit()
        cur.close()

    def delete(self, id):
        """method that deletes a record from the database"""
        conn = dbconnect()
        cur = conn.cursor()
        query = "DELETE FROM users WHERE id=(%s);"
        data = (id,)
        cur.execute(query, data)
        conn.commit()
        cur.close()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, email):
        conn = dbconnect()
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE email = '%s';" % (email)
        cur.execute(query)
        result = cur.fetchone()
        import pdb

        pdb.set_trace()
        cur.close()
        hash = result[-2]
        return sha256.verify(password, hash)
