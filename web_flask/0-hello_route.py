"""
A simple Flask web application that greets with 'Hello HBNB'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that returns a greeting message.

    Returns:
        str: Greeting message 'Hello HBNB!'
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
