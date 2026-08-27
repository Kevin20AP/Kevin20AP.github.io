from turtle import Turtle, Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right ,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()
    # Move segments from tail to head


    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.increase_score()




screen.exitonclick()