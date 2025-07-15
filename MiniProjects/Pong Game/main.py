from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

p1 = Paddle(-350, 0)
p2 = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(p1.Up, 'w')
screen.onkeypress(p1.Down, 's')

screen.onkeypress(p2.Up, 'Up')
screen.onkeypress(p2.Down, 'Down')


is_playing = True
while is_playing:
    screen.update() 
    time.sleep(ball.ball_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(p1) < 50 and ball.xcor() < -320 or ball.distance(p2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.updatescore("p1")
    elif ball.xcor() < -380:
        ball.restart()
        scoreboard.updatescore("p2")
        
        

screen.exitonclick()