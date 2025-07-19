import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
carmanager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
game_loop = 0
while game_is_on:
    time.sleep(0.1)
    if game_loop % 6 == 0:
        carmanager.spawn_car()

    carmanager.move_cars()

    if player.reached_finish_line():
        player.back_to_start()
        carmanager.increase_speed()
        score.next_level()

    for car in carmanager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            score.game_over()

    game_loop += 1
    screen.update()

screen.exitonclick()