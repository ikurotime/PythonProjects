from flask import Flask
import random
app = Flask(__name__)
random_number = random.randint(0,9)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Higher or lower...</h1>' \
           '<h3 style="text-align: center">Guess a number between 0 and 9</h3>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=500>'


@app.route('/<int:number>')
def guess(number):
    if number > random_number:
        return '<h1 style="text-align: center">Too high!!</h1>' \
               '<p style="text-align: center">Try again!</p>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < random_number:
        return '<h1 style="text-align: center">Too low...</h1>' \
               '<p style="text-align: center">Try again!</p>' \
               '<img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="text-align: center">You find me!</h1>' \
               '<p style="text-align: center">Nice job!</p>' \
               '<img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug= True)
