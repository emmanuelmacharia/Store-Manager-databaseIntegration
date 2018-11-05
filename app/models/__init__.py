
'''creates a connection with the database'''
import os
import psycopg2
from .database import queries, deletes
from instance.config import Configurations, Testing, app_configurations


def dbconnect():
    '''connects to the databse'''
    environment = os.getenv('APP_SETTINGS')
    if environment == 'testing':
        conn = psycopg2.connect(Testing.DATABASE_URI)
    else:
        conn = psycopg2.connect(Configurations.DATABASE_URI)

    return conn

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
