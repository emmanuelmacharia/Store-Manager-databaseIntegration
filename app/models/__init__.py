
'''creates a connection with the database'''
import os
import psycopg2
from .database import queries
from instance.config import Configurations, Testing



def dbconnect():
    '''connects to the databse'''
    environment = os.getenv('APP_SETTINGS')
    print(environment)
    try:
        if environment == 'production' or environment == 'development':
            conn = psycopg2.connect(dbname=Configurations.DBNAME, 
                                    host = Configurations.HOST, port = Configurations.PORT,  
                                    user = Configurations.USER, password = Configurations.PASSWORD)
            return (conn)
        else: 
            testconn = psycopg2.connect(dbname=Testing.DBNAME,
                                    host = Configurations.HOST, port = Configurations.PORT,  
                                    user = Configurations.USER, password = Configurations.PASSWORD
                                    )
            return testconn
    except Exception as e:
        return ('failed to connect', e)


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
    from database import deletes
    testconn = dbconnect()
    cur = testconn.cursor()
    for deleter in deletes:
        cur.execute(deleter)