from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")


# Game loop
game_is_on = True
while game_is_on:
    screen.update()   # Manually update the screen
    time.sleep(0.1)   # Pause for a short moment
    snake.move()

screen.exitonclick()
