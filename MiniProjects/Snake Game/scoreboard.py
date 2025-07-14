from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.write(f"Score: {self.score}", move=True, align="center", font=('Arial', 8, 'normal'))
        self.hideturtle()
        self.color('white')
        self.write("Score: ", True, align="center")  
        self.write(f"{self.score}", True)