from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        r_xcor = random.randint(-275, 275)
        r_ycor = random.randint(-275, 275)
        self.goto(r_xcor, r_ycor)
