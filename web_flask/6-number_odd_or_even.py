#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Web application """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_HBNB():
    """ Web application """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """ display "C" followed by the value of the text variable
    (replace underscore _ symbols with a space ) """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text='is cool'):
    """  Display Python , followed by the value of the text variable
    (replace underscore _ symbols with a space )
    The default value of text is is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numer_is(n):
    """ Display n is a number only if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numer_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_par(n):
    """ Display a HTML page only if n is an integer """
    if n % 2 == 0:
        module = 'even'
    else:
        module = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, module=module)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
