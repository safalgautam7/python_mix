from turtle import Turtle 
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan4")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()
        
    def update_score(self):
        self.goto(-100,180)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,180)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))
    def add_score_right(self):
        self.r_score+=1
        self.clear()
        self.update_score()
    def add_score_left(self):
        self.l_score+=1
        self.clear()
        self.update_score()
    def winner(self,winner=None):
        self.l_score=0
        self.r_score=0
        self.update_score()
        self.goto(0,0)
        self.clear()
        self.color("red")
        self.write(f"The winner is player on the {winner}!!",align="center",font=("Courier",20,"normal"))