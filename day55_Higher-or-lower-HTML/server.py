import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def request():
    return "<h1>Guess a number</h1> <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=50%>"


@app.route('/<number>')
def check_guess(number):
    random_number = random.randint(0, 10)
    if random_number == int(number):
        return (f"<h1>{number} is right! You got it</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=50%>")
    elif random_number < int(number):
        return (f"<h1>{number} is too high</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=50%>")
    else:
        return (f"<h1>{number} is too low</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=50%>")


if __name__ == "__main__":
    app.run(debug=True)
