from turtle import Turtle
ALIGNMENT = "center"
FONT = ("score", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 255)

    def write_score(self):
        self.write(f"Score : {self.score}", False, ALIGNMENT, FONT)

    def increse_score(self):
        self.score += 1
        self.clear()
        self.write_score()
