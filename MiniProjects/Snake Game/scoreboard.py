from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.set_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=('Arial', 14 , 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score_file()

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=('Arial', 14 , 'normal'))
    
    def update_high_score_file(self):
        with open("./data.txt", mode="w") as file:
            file.write(str(self.high_score))
    
    def set_high_score(self):
        with open("./data.txt", mode="r") as file:
            self.high_score = int(file.read())