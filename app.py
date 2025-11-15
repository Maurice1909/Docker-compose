from flask import Flask
import redis 

app = Flask(__name__)
r = redis.Redis(host='db', port=6379)

@app.route('/')
def welcome():
    return 'Docker Containers Session!'

@app.route('/count')
def count():
    count = r.incr('hits')
    return f'This page has been viewed {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
