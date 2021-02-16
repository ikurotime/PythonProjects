from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-270,270)
        self.write(arg=f'Level: {self.score}',align='left',font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(arg=f'Level: {self.score}',align='left',font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER',align='center',font=FONT)
