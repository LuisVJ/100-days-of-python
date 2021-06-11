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
car_manager = CarManager()
car_manager.generate_cars()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if car_manager.move_cars(player):
        game_is_on = False

    if player.ycor() > FINISH_LINE_Y:
        # Level up
        scoreboard.update_score()
        player.reset_position()
        car_manager.increase_speed()

scoreboard.game_over()

screen.exitonclick()
