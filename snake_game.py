from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
turtle = Turtle()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake.create_snake()

is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.05)
    snake.move_snake()



screen.exitonclick()
