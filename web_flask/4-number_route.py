#!/usr/bin/python3
""" Starts a Flask Web application comprising
    of three view functions
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Returns Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def home():
    """ Returns HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def home_c(text: str) -> str:
    """ Displays C followed by text

    Args:
        text(str): Text to append

    Returns:
        C + <text>
    """
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/number/<int:n>', strict_slashes=False)
def num(n: int) -> str:
    """ Displays n is number

    Args:
        n(int): Number to diplay

    Returns:
        n is number
    """
    return f"{n} is number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
