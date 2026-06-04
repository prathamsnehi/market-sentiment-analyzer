import psycopg2

# def get_connection():
#     return psycopg2.connect(
#         dbname="test",
#         user="prath",
#         password="prath",
#         host="localhost",
#         port="5432"
#     )

async def create_pool():
    # a pool is used to use the same connection again and again securely
    return await asyncpg.create_pool(
        dbname="test",
        user="prath",
        password="prath",
        host="localhost",
        port="5432"
    )