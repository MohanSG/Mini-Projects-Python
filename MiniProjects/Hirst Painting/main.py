import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('cool-pic.png', 100)
colors_set = []
for color in colors:
    r = color.rgb.r 
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_set.append(new_color)

screen = Screen()
screen.setup(550, 550)
x = -240
y = -200

t = Turtle()
t.pensize(20)
t.penup()
t.teleport(x, y)
t.speed('fastest')
t.hideturtle()
t.screen.bgcolor("orange")
t.screen.colormode(255)

x_counter = 0
for _ in range(100):
    t.dot(20, random.choice(colors_set))
    t.forward(50)
    x_counter += 1

    if x_counter == 10:
        y += 50
        t.teleport(x, y)
        x_counter = 0
        
screen.mainloop()
