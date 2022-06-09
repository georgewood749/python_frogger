from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setpos(-230, 260)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", False, "center", FONT)

