from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.setpos(random.randint(-250, 250), random.randint(-250, 250))

    def move(self, move_increment):
        new_x = self.xcor() - (STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * move_increment))
        self.setx(new_x)

    def increase_level(self):
        self.level += 1
        self.move(self.level)

