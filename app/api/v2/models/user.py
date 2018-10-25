
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
        query = "INSERT INTO users (username,email,password,admin_role) VALUES('%s, %s, %s %s');")
        data = (self.username, self.email, self.password, self.role)
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


    def ammend(self, id):
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
