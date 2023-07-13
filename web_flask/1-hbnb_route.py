#!/usr/bin/python3
""" Starts a flask web app that returns a greeting """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """ function that returns greeting """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that return message"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
