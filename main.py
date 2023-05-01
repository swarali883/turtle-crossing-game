import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #collision with car
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            scoreboard.game_over()


    #detect successful crossing
    if tim.is_at_finish_line():
        tim.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()






screen.exitonclick()