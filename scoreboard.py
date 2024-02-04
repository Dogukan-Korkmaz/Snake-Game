from turtle import Turtle
ALIGNMENT = "center"
FONT = ("score", 25, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score : {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()

    # def reset_pos(self):
    #     self.goto(0, 0)
    #     # self.write("GAME OVER", False, "center", FONT)
