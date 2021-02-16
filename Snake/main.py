from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the SNEK")
screen.tracer(0)

my_snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(my_snake.up, "w")
screen.onkey(my_snake.down, "s")
screen.onkey(my_snake.left, "a")
screen.onkey(my_snake.right, "d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 20:
        food.refresh()
        my_snake.extend()
        score.increase_score()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        score.reset()
        my_snake.reset()
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            score.reset()
            my_snake.reset()
screen.exitonclick()
