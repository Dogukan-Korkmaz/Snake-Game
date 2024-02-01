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

    def write_score(self):
        self.goto(0, 255)
        self.write(f"Score : {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
