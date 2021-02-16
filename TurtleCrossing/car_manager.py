from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.penup()
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.setpos(300,random.randint(-250,250))
            car.shape('square')
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)



