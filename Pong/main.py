from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
l_score = Score((-100, 220))
r_score = Score((100, 220))
ball = Ball()

game_is_finished = False
screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

while not game_is_finished:
    screen.update()
    time.sleep(0.01)

    ball.move()
    # If the ball touches the top and bottom edges of the screen, it bounces
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    #
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        l_score.update_score()
        ball.refresh()
        ball.move()
    if ball.xcor() < -400:
        r_score.update_score()
        ball.refresh()
        ball.move()
    if l_score.score > 9 or r_score.score > 9:
        game_is_finished = True
        r_score.game_over()

screen.exitonclick()
