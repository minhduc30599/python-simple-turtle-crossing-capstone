from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_change = random.randint(1, 8)
        if random_change == 1:
            car = Turtle(shape='square')
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            new_y = random.randint(-250, 250)
            car.goto(300, new_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.penup()
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def car_stop(self):
        self.speed = 0
