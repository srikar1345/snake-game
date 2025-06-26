from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.highscore=0
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
        
    def inc(self)  :
        self.clear()
        self.score+=1  
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))
    def update_scorebaord(self):
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"normal"))

        
        

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scorebaord()
