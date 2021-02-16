from turtle import  Turtle, Screen
import random

colors = ['firebrick','cornflower blue','olive drab','pale violet red','gold','dark orange','peru','plum','light slate gray']

tim = Turtle()
tim.shape('circle')
screen = Screen()
tim.speed(0)

for n in range(51):
    tim.color(random.choice(colors))
    tim.circle(100)
    tim.right(7)










screen.exitonclick()