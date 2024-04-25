import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

change_speed = 0.1
screen.title("Turtle Crossing game")

screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(change_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # collision player collides with any car
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            score.game_over()
            game_is_on = False

    # Player has reached the top
    if player.reached_top():
        score.score_increase()
        change_speed *= 0.6


screen.exitonclick()
