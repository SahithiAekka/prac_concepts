from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("deeppink")
        self.penup()
        self.hideturtle()
        self.l_score= 0
        self.r_score= 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align= "center", font=("Courier", 80))
        self.goto(100,200)
        self.write(self.r_score, align= "center", font=("Courier", 80))
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def game_over(self, winner):
        self.goto(0, 0)
        self.write(winner, align="center", font=("Courier", 40, "bold"))

        
    




