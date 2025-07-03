from turtle import Turtle, Screen

turtles = []
screen = Screen()
screen.screensize(500, 500)


for t in range(6):
    turtles.append(Turtle(shape="turtle"))

y = 190
for turtle in turtles:
    turtle.penup()
    turtle.goto(-248, y)

    y -= 75

screen.mainloop()