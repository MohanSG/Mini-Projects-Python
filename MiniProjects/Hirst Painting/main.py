from turtle import Turtle
import random
import heroes

t = Turtle()
t.screen.colormode(255)
t.speed('fastest')

def generate_colour():
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    colors = (color1, color2, color3)
    return colors

angle = 0
while angle < 360:
    t.pencolor(generate_colour())
    t.circle(100)
    angle +=6
    t.setheading(angle)
t.screen.mainloop()