from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-250, 270)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.write(f"Level: {self.current_level}", False, align="center", font=('Arial', 14 , 'normal'))
    
    def next_level(self):
        self.current_level +=1
        self.clear()
        self.updatescoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Arial', 14 , 'normal'))