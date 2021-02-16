from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_f():
    tim.forward(25)
def turn_r():
    tim.right(45)
def turn_l():
    tim.left(45)
def move_b():
    tim.back(25)
screen.listen()
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_f, "w")
screen.onkey(turn_r, "d")
screen.onkey(turn_l, "a")
screen.onkey(move_b, "s")
screen.onkey(clear, "c")



screen.exitonclick()