import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(False)

score = Scoreboard()
turtle = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(turtle.move, 'Up')

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()
    if turtle.ycor() == 280:
        score.update_scoreboard()
    turtle.new_level()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()