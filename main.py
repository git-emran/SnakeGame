from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

#Snake class
snake = Snake()
#Food class
food = Food()
#Score board
scoreboard = Scoreboard()

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
    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()

    # Detect collision with Tail
    for segment in snake.segments[1:]:
        if segment.distance(segment) < 10:
            scoreboard.game_over()




screen.exitonclick()
