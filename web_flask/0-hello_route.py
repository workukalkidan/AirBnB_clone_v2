#!/usr/bin/python3
"""
    Sript that starts a Flask web application
 """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """
        function to return Hello HBNB!
    """
    return "Hello HBNB!"
if __name__ == '__main__':
        app.run(host=100.26.156.58', port=5000)
