from turtle import Turtle
import datetime
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
        self.write_file()

    def write_file(self):
        with open("data.txt", "a") as file:
            new_highscore = self.high_score
            now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"\nYour Highscore : {str(new_highscore)}\nDate : {now}\n")
            file.write("----------------------------------------------------")






