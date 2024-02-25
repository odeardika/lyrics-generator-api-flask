from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>lyrics generator api by ode ardika</h1>'