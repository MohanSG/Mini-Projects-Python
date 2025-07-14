from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

p1 = Paddle(350, 0)
p2 = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkeypress(p1.Up, 'Up')
screen.onkeypress(p1.Down, 'Down')

screen.onkeypress(p2.Up, 'w')
screen.onkeypress(p2.Down, 's')


is_playing = True
while is_playing:
    screen.update() 
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280:
        ball.bounce()
    elif ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()