#!/usr/bin/python3
""" Starts a flask web app that returns a greeting """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('./states', strict_slashes=False)
def states():
    """ function that displays a HTML page with states """
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode="all")


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """ function that displays a HTML page with citys of a staet """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
        return render_template('9-states.html', states=state, mode='none')


@app.teardown_appcontext
def teardown(self):
    """ closes session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
