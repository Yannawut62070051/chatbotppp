
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Test Deploy</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)