import psycopg2

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '123',
    'host': '127.0.0.1' 
}

conn = psycopg2.connect(**db_params)
username = 'serg'