import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="test",
        user="prath",
        password="prath",
        host="localhost",
        port="5432"
    )
