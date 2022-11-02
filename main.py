import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        scoreboard.get_point()
        cars.increase_speed()

    for car in cars.cars:
        if player.distance(car) < 32:
            scoreboard.end_game()
            cars.car_stop()
            time.sleep(5)
            game_is_on = False
