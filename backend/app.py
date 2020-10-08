import os
from flask import Flask, request
import psycopg2

SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVER_PORT = os.getenv('SERVER_PORT', '5000')
REDIS_SERVER_HOST = os.getenv('REDIS_SERVER_HOST', 'localhost')
REDIS_SERVER_PORT = os.getenv('REDIS_SERVER_PORT', '6379')
POSTGRES_HOST= os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT= os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DATABASE= os.getenv('POSTGRES_DATABASE', 'fb-dev')
POSTGRES_USER=os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD', 'postgres')
DEBUG=os.getenv('DEBUG', True)

# dsn = "dbname={POSTGRES_DATABASE} user={POSTGRES_USER}"
dsn = f"host={POSTGRES_HOST} port={POSTGRES_PORT} dbname={POSTGRES_DATABASE} user={POSTGRES_USER} password={POSTGRES_PASSWORD}"
print (dsn)

pg_connection = psycopg2.connect(dsn=dsn)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello There!', 200


if __name__ == "__main__":
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG)
