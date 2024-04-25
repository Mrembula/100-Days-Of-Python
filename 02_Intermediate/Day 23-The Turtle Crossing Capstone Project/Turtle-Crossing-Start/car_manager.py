from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        car_position = random.randint(-240, 240)
        new_car.goto(320, car_position)
        if car_position % 5 == 0:
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)


        