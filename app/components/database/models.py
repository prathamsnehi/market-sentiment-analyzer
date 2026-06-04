import asyncpg
from asyncpg.pool import Pool

# Table: Sentiment Analysis for a particular Ticker:
# id SERIAL PRIMARY KEY,
# symbol TEXT,
# sentiment_content TEXT,
# content_timestamp TIMESTAMP,
# sentiment_score DECIMAL, (between -1 and 1)

# model functions required:
# initialize_table
# insert_sentiment
# get_sentiment_score
# update_sentiment

async def initialize_table(pool: Pool):
    # taking a connection from the pool:
    async with pool.acquire() as connection:
        await connection.execute('''
            CREATE TABLE IF NOT EXISTS ticker_sentiments (
                id SERIAL PRIMARY KEY,
                symbol TEXT NOT NULL,
                sentiment_content TEXT,
                content_timestamp TIMESTAMP,
                sentiment_score DECIMAL
            );
        ''')
        print("Table initialized successfully")

async def insert_sentiment(pool: Pool, symbol: str, sentiment_content: str, content_timestamp: str, sentiment_score: float):
    async with pool.acquire() as connection:
        await connection.execute("""
            INSERT INTO ticker_sentiments (symbol, sentiment_content, content_timestamp, sentiment_score)
            VALUES ($1, $2, $3, $4)
        """, symbol, sentiment_content, content_timestamp, sentiment_score)
    print("Sentiment inserted successfully")

async def get_sentiment_score(pool: Pool, symbol: str):
    async with pool.acquire() as connection:
        result = await connection.fetch("""
            SELECT sentiment_score FROM ticker_sentiments WHERE symbol = $1
        """, symbol)
        return result

async def update_sentiment(pool: Pool, symbol: str, sentiment_content: str, sentiment_score: float, timestamp: str):
    async with pool.acquire() as connection:
        await connection.execute("""
            UPDATE ticker_sentiments SET sentiment_score = $1, content_timestamp = $2, sentiment_content = $3 WHERE symbol = $4
        """, sentiment_score, timestamp, sentiment_content, symbol)
        print("Sentiment updated successfully")