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
    /number/<n>: Displays 'n is a number', only if 'n' is an integer
    /number_template/<n>: Displays an HTML page with the H1 tag "Number: `n`"
        inside the BODY tag only if `n` is an integer

This application is set to listen on 0.0.0.0, port 5000,
The strict_slashes option is set to False.
"""


from flask import Flask, render_template

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


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """
    Displays "`n` is a number" only if n is an integer
    """
    try:
        int(n)
        return f"{n} is a number"
    except ValueError:
        return '', 404


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with the H1 tag "Number: `n`" inside the BODY tag,
    only if `n` is an integer, for the route /number_template/<n>.
    """
    try:
        int_n = int(n)
        return render_template('5-number.html', n=int_n)
    except ValueError:
        return '', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
