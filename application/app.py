from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Linux!</p>"

@app.route("/get")
def handle_get():
    return "<p>Received a GET request!</p>"

@app.route("/post")
def handle_post():
    return "<p>Received a POST request!</p>"

@app.route("/put")
def handle_put():
    return "<p>Received a PUT request!</p>"

app.run(host='0.0.0.0', port=5000)