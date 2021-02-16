from turtle import Turtle

DISTANCE = 80


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('square')
        self.goto(position)
        self.color('white')
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()

    def up(self):
        new_y = self.ycor() + DISTANCE
        self.setpos(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - DISTANCE
        self.setpos(self.xcor(), new_y)
