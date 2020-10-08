import os
import redis

REDIS_SERVER_HOST = os.getenv('REDIS_SERVER_HOST', 'localhost')
REDIS_SERVER_PORT = os.getenv('REDIS_SERVER_PORT', '6379')

# r = redis.Redis(host='redis', port=6379, db=0)
client = redis.Redis(host=REDIS_SERVER_HOST, port=REDIS_SERVER_PORT, db=0)


def fibonacci(n: int) -> int:
    if n <= 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


while True:
    number = int(client.rpop('message')[1])
    result = fibonacci(number)