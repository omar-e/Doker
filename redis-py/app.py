from flask import Flask
import os
import redis

app = Flask(__name__)
redis_host=os.getenv('REDIS_HOST','redis')
redis_port=int(os.getenv('REDIS_PORT', 6379))
client = redis.Redis(host=redis_host, port=redis_port)
@app.route('/')
def hello_world():
    return 'CoderCo Containers Session!'

@app.route('/count')
def count_visitors():
    count = client.incr('visitor_count')
    return f'You are Visitor number: {count} times'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)