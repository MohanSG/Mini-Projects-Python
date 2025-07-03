from turtle import Turtle, Screen
import random

turtles = []
screen = Screen()
colors = ("blue", "green", "yellow", "orange", "red", "purple")

is_race_on = False
screen.setup(width=500, height=500)

for t in range(6):
    turtles.append(Turtle(shape="turtle"))

y = 190
for i in range(len(turtles)):
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-230, y)

    y -= 75

choice = screen.textinput("Turtle Race", "Place your bet!")
is_race_on = True

while(is_race_on):
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))

        if turtle.xcor() > 225:
            if turtle.pencolor() == choice:
                print(f"The {turtle.pencolor()} turtle won! You got it right!")
            else:
                print(f"The {turtle.pencolor()} turtle won! You got it wrong!")
            is_race_on = False

screen.mainloop()