from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collisions with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collisions with paddle
    if (
        ball.distance(r_paddle) < 40 and ball.xcor() > 330
        or ball.distance(l_paddle) < 40 and ball.xcor() < -330
    ):
        ball.bounce_x()

    # Detect scoring
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()