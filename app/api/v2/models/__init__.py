
import psycopg2
DATABASE_URL =(dbname='store-manager', host='localhost', port=5432, user=postgres, password='1234qwerty20')
conn = psycopg2.connect(DATABASE_URL)

if conn == True:
    print('connect')
