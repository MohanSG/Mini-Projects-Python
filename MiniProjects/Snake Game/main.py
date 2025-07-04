from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_bits = []
snake_length_unit = 0

x = 0
y = 0

for _ in range(3):
    t = Turtle("square")
    t.penup()
    t.color("white")
    t.goto(x, y)
    x -= 20
    snake_bits.append(t)


is_playing = True

while is_playing:
    for bit in snake_bits:
        bit.forward(20)

        if bit.xcor() > 570:
            is_playing = False
            
    screen.update()
    time.sleep(1)
        
screen.exitonclick()