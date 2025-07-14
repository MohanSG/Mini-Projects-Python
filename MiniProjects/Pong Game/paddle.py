from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_x, starting_y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_x, starting_y)

    def Up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)