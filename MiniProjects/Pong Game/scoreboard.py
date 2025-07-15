from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.p1_score = 0
        self.p2_score = 0
        self.updatescoreboard()
        
    def updatescore(self, player):
        if player == "p1":
            self.p1_score += 1
        elif player == "p2":
            self.p2_score += 1
        self.clear()
        self.updatescoreboard()
    
    def updatescoreboard(self):
        self.write(f"{self.p1_score}          {self.p2_score}", False, align="center", font=("Courier", 22, "normal"))