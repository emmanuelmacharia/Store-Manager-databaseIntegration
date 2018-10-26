
import psycopg2
from .database import queries


def dbconnect():
    '''connects to the databse'''
    try:
        conn = psycopg2.connect("""dbname='StoreManager'
                                host='localhost'
                                port=5432 user='postgres'
                                password='Permafrost'""")
        return (conn)
    except Exception as e:
        return ('failed to connect', e)

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
