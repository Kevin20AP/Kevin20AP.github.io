from turtle import Screen
from turtle_1 import Turtles
from turtle import Turtle# Your custom paddle class
import time
import random
from ball import Ball
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles
l_paddle = Turtles((-340, 0))
r_paddle = Turtles((340, 0))
scoreboard = Scoreboard()
scoreboard.update_score()
ball = Ball()


# Keyboard controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")





# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right paddle misses → left scores
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle misses → right scores
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()



