from turtle import Turtle

SPEED = 3


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.y_speed = SPEED
        self.x_speed = SPEED
        self.create_ball()

    def create_ball(self):
        self.shape('circle')
        self.setposition(0, 0)
        self.color('white')
        self.turtlesize(stretch_len=0.8, stretch_wid=0.8)
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.setpos(new_x, new_y)

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()
