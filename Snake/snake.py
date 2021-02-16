from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {'RIGHT': 0, 'UP': 90, 'LEFT': 180, 'DOWN': 270}


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        snek = Turtle("square")
        snek.color("white")
        snek.penup()
        snek.goto(position)
        self.segments.append(snek)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DIRECTIONS['DOWN']:
            self.head.setheading(DIRECTIONS['UP'])

    def down(self):
        if self.head.heading() != DIRECTIONS['UP']:
            self.head.setheading(DIRECTIONS['DOWN'])

    def left(self):
        if self.head.heading() != DIRECTIONS['RIGHT']:
            self.head.setheading(DIRECTIONS['LEFT'])

    def right(self):
        if self.head.heading() != DIRECTIONS['LEFT']:
            self.head.setheading(DIRECTIONS['RIGHT'])
