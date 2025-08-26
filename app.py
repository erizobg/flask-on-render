from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on Render!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}! Welcome to Flask on Render."
