#1##app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from sagar-m"

if __name__ == '__main__':
    app.run(host='102.33.3.2', port=9000)
