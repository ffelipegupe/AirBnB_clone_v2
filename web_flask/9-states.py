#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import getitem
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_cities():
    """List all the states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """List all the states with the id """
    check = 0
    states = None
    states = storage.all(State).values()
    for state in states_all:
        if id in state.id:
            check = 1
            states = state
            break
    return render_template('9-states.html', states=states, check=check)


@app.teardown_appcontext
def db_closing(db):
    """ Method that remove the current SQLAlchemy Session after
    each request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
