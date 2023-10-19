from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Arial", 40, "normal"))

    def game_over(self, winner):
        self.goto(0,0)
        self.write(f"GAME OVER. PLAYER {winner} WINS!!", align="center", font=("Arial", 30, "normal"))