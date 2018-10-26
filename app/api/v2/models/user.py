
'''Handles all the user queries from the database'''


import json
from passlib.hash import pbkdf2_sha256 as sha256
from flask import Flask, jsonify, request
from .__init__ import dbconnect, createTables



class User:

    def save(username, email, hash, admin_role=False):
        '''takes the data input from the user and saves it into the database'''
        conn = dbconnect()
        cur = conn.cursor()
        query = "INSERT INTO users (username,email,password,admin_role) VALUES('%s, %s, %s %s');"
        data = (username,email,password,admin_role)
        cur.execute(qeury, data)
        conn.commit()
        cur.close()


    def viewall(self):
        '''queries the database to view all users'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM users;")
        cur.fetchall()
        cur.close()


    def ammend(id):
        '''method that updates data in the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "UPDATE users SET (%s) WHERE id=(%s)"
        data = (self.role, id)
        cur.execute(qeury, data)
        conn.commit()
        cur.close()

    def delete(self,id):
        '''method that deletes a record from the database'''
        conn= dbconnect()
        cur= conn.cursor()
        query = "DELETE FROM users WHERE id=(%s);"
        data = (id,)
        cur.execute(query,data)
        conn.commit()
        cur.close()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
