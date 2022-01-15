from turtle import Turtle, Screen, home
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreCard

screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = ScoreCard()


# display setup
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping - Pong")
screen.tracer(0)

# keyboard listeners
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    ball.move_ball()
    time.sleep(0.03)
    screen.update()

    # bounce contact with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # contact with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # contact with the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # when the right paddle misses the ball
    if ball.xcor() > 360:
        ball.reset_position()
        score.increase_l_score()

    # when the left paddle misses the ball
    if ball.xcor() < -360:
        ball.reset_position()
        score.increase_r_score()


screen.exitonclick()
