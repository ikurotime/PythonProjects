from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.setposition(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        if self.ycor() == FINISH_LINE_Y:
          self.goto(STARTING_POSITION)
