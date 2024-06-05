#!/usr/bin/python3
"""
This module defines a Flask web application with the following routes:
    /: Displays 'Helo HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays "C" followed by the value of the text variable,
        replacing undescores with spaces
    /python/<text>: Displays "Python" followed by a value in the text variable,
        replacing underscores with spaces
        If the text is not provided, the default text is 'is cool'.

This application is set to listen on 0.0.0.0, port 5000,
The strict_slashes option is set to False.
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


def c_text(text):
    """
    Displays "C " followed by the value of the text variable,
    replacing underscores with spaces, for the route /c/<text>.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays "Python " followed by the value of the text variable,
    replacing underscores with spaces, for the route /python/<text>.
    If no text is provided, the default value is "is cool".
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
