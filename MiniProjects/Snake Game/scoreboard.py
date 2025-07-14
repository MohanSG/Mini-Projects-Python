from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.write(f"Score: {self.score}", move=True, align="center", font=('Arial', 8, 'normal'))
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color('white')
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 14 , 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=('Arial', 14 , 'normal'))