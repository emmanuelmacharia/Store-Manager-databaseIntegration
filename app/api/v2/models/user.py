
'''Handles all the user queries from the database'''


import json
from __init__ import dbconnect, createTables



class User:
    def __init__(self, username, email, password):
        self.role = role
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        '''takes the data input from the user and saves it into the database'''
        conn = dbconnect()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username,email,password,role) VALUES('%s, %s, %s %s');",())
        conn.commit()
        cur.close()

    def login(self, username, email, password):


    def viewall(self):
        '''queries the database to view all users'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("SELECT * FROM users;")
        conn.commit()
        cur.close()

    def ammend(self, id):
        '''method that updates data in the database'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("UPDATE users SET {} WHERE id={};".format(,self.id))
        conn.commit()
        cur.close()

    def delete(self):
        '''method that deletes a record from the database'''
        conn= dbconnect()
        cur= conn.cursor()
        cur.execute("DELETE FROM users WHERE id=self.id;")
        conn.commit()
        cur.close()
