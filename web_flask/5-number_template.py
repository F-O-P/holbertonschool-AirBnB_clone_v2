#!/usr/bin/python3
""" Starts a flask web app that returns a greeting """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """ function that returns greeting """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ function that returns a hbnb message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ function that return message, but with a C """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<hiss>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def parseltongue(hiss="is cool"):
    """ function that returnsss a python message """
    return 'Python {}'.format(hiss.replace('_', ' '))


@app.route('/number/<input>', strict_slashes=False)
def digis(input):
    """ function that displays a number if it is an integer """
    if input.isdigit():
        return '{} is a number'.format(input)


@app.route('/number_template/<int:input>', strict_slashes=False)
def html_template(input):
    """ function that displays a HTML page only if input is an integer """
    return render_template('5-number.html', number=input)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
