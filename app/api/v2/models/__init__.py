
import psycopg2
#frompsycopg2 import pool
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


#connection_pool = pool.SimpleConnectionPool(1,50, dbname='StoreManager' host='localhost' port=5432 user='postgres' password='Permafrost')
#connection_pool.putconn(connection)

# class ConnectionPool():
#     def __init__(self):
#         self.connection_pool = pool.SimpleConnectionPool(1,5, dbname='StoreManager' host='localhost' port=5432 user='postgres' password='Permafrost')
#
#     def __enter__(self):
#         return self.connection_pool.getconn()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         #we really shuld return the cnnection to the pool
#         pass===>wrong
#
# class ConnectionFromPool():
#     def __init__(self):
#         self.connection_pool = None
#
#     def __enter__(self):
#         self.connection= connection_pool.getconn()
#         return self.connection
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         #we really shuld return the cnnection to the pool
          #self.connection.commit() =====>dont forget to commit
#         connection_pool.putconn(self.connection)
