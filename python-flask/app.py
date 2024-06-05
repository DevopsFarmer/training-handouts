from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    return f'Hello, World! from {hostname}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
