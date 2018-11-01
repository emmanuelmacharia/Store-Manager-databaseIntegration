
'''creates a connection with the database'''
import os
import psycopg2
from .database import queries, deletes
from instance.config import Configurations, Testing, Development
from flask import current_app


def dbconnect():
    '''connects to the database'''
    environment = os.getenv('TESTING_URL')
    conn = psycopg2.connect(environment)
    return (conn)


conn = dbconnect()
print(conn)


def createTables():
    '''creates all the tables in the database'''
    conn = dbconnect()
    cur = conn.cursor()

    for query in queries:
        cur.execute(query)
    conn.commit()
    cur.close()


def droptables():
    '''deletes all the tables; should only be called when testing'''
    testconn = dbconnect()
    cur = testconn.cursor()
    for deleter in deletes:
        cur.execute(deleter)
