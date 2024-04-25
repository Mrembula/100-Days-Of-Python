from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.screensize(800, 600, 'black')
screen.title('Pong Game')
play_game = True
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

while play_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()

    # Detect a ball bounce
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect if paddle missed the ball restart ball
    if ball.xcor() > 400:
        ball.reset()
        score.l_point()

    if ball.xcor() < -400:
        ball.reset()
        score.r_point()

screen.exitonclick()
