from turtle import Turtle, Screen
import random
tim = Turtle()
tim.getscreen().bgcolor('white')
sides = 3
colors = ['firebrick','cornflower blue','olive drab','pale violet red','gold','dark orange','peru','plum','light slate gray']
tim.pensize(15)
tim.speed(0)
tim.shape('circle')
directions = [0, 90, 180, 270]

def walk():
  tim.forward(30)
for n in range(200):
    tim.color(random.choice(colors))
    walk()
    tim.right(random.choice(directions))










screen = Screen()
screen.exitonclick()
