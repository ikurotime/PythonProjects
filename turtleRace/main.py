from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(500, 500)
tim = Turtle()
tom = Turtle()
tem = Turtle()
tam = Turtle()
bob = Turtle()

tim.name = 'Tim'
tom.name = 'Tom'
tem.name = 'Tem'
tam.name = 'Tam'
bob.name = 'Bob'

tim.color('green')
tom.color('red')
tem.color('steel blue')
tam.color('gold')
bob.color('orange')

turtles = [tim, tom, tam, tem, bob]

race_finished = False

for turtle in turtles:
    turtle.shape('turtle')

user_guess = screen.textinput("Turtle Race", "Who will win the race? Tim,Tam,Tem,Tom or Bob?:")


def set_pos(_turtle, x: float, y: float):
    _turtle.penup()
    _turtle.setpos(x, y)


def turtles_move(_turtle):
    n = [5, 10]
    _turtle.forward(random.choice(n))


def check_winner(_turtle):
    if _turtle.xcor() >= 300:
        return True


set_pos(tim, -320.0, 50.0)
set_pos(tom, -320.0, 25.0)
set_pos(tem, -320.0, 0.0)
set_pos(tam, -320.0, -25.0)
set_pos(bob, -320.0, -50.0)

while not race_finished:
    for turtle in turtles:
        race_finished = check_winner(turtle)
        if race_finished is True:
            break
        else:
            turtles_move(turtle)

for turtle in turtles:
    if turtle.xcor() >= 300.0:
        if user_guess == turtle.name:
            print(f"{turtle.name} reached the goal")
            print("You win!")
        else:
            print(f"{turtle.name} reached the goal")
            print("You lose")

screen.exitonclick()
