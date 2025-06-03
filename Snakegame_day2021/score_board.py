from turtle import Turtle
from food import Food

ALIGNMNET= "center"
FONT = ("Arial", 20,"normal")
class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMNET , font= FONT)
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMNET , font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMNET, font= FONT)


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()