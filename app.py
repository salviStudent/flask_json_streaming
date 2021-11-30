from flask import Flask
import json
from random_file_generator import random_list_generator

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data")
def data_stream():
    '''
    Streams random list data.
    '''
    # NOTE: first argument has to be a generator and the second argument has to
    # be mimetype='text/csv' for this to work correctly.
    return app.response_class(
        random_list_generator('test1.txt'),
        mimetype='text/csv')
    
