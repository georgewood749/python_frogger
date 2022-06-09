import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("dark gray")
screen.tracer(0)

player = Player()
cars = []
scoreboard = Scoreboard()

for _ in range(20):
    car = CarManager()
    cars.append(car)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    for car in cars:
        car.move(car.level)
        if car.xcor() < -300:
            car.setx(300)

    if player.ycor() >= 290:
        player.setpos(0, -280)
        scoreboard.next_level()
        for car in cars:
            car.increase_level()

    for car in cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
