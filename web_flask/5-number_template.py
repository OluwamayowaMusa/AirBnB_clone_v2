#!/usr/bin/python3
""" Starts a Flask Web application comprising
    of view functions
"""
from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def home_python(text: str) -> str:
    """ Displays Python followed by text

    Args:
        text(str): Text to append

    Returns:
        Python + <text>
    """
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def home_number(n: int) -> str:
    """ Displays n is a number

    Args:
        n(int): Number to display

    Returns:
        n is number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def home_number_template(n: int) -> str:
    """ Displays n using a template

    Args:
        n(int): Number to display

    Returns:
        Template
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
