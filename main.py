import psycopg2
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='123',
    host = '127.0.0.1'

)
