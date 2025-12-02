from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,paddle_position):
        super().__init__()
        self.define_paddle(paddle_position)
    def define_paddle(self,position):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)
        
    def move_right(self,keys=None):
        """ moves the right paddle"""
        if keys=="Up":
            new_y=self.ycor()+20
            self.goto(x=self.xcor(),y=new_y)
        if keys=="Down":
            new_y=self.ycor()-20
            self.goto(x=self.xcor(),y=new_y)
    def move_left(self,keys=None):
        if keys=="w":
            new_y=self.ycor()+20
            self.goto(x=self.xcor(),y=new_y)
        elif keys=="s":
            new_y=self.ycor()-20
            self.goto(x=self.xcor(),y=new_y)