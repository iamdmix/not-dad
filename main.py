import os
from flask import Flask

FLAG = "c0d{fake_flag}"

app = Flask(__name__)

@app.route('/')
def hello():
    return FLAG

app.run('0.0.0.0', 8080)