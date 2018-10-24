
import psycopg2
DATABASE_URL ="dbname='storemanager' host='localhost' port=5432 user='postgres' password='Permafrost'"
conn = psycopg2.connect(DATABASE_URL)

if conn == True:
    print(conn)

cur = conn.cursor()

def connect():
    pass

def disconnect():
    pass
