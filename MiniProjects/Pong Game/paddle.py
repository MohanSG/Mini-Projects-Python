from turtle import Turtle
PADDLE_SPEED = 20

class Paddle(Turtle):
    def __init__(self, starting_x, starting_y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_x, starting_y)

    def Up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)

    def Down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)