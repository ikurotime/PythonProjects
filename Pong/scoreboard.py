from turtle import Turtle

FONT_SIZE = 60


class Score(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.goto(cords)

        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'{self.score}', align='center', font=('Arial', FONT_SIZE, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=('Arial', FONT_SIZE, 'normal'))
