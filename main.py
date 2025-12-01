from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
is_race_on=False


#TODO 1: move the turtle to the from the line 
colors=["red","orange","yellow","green","blue","purple"]
turtles=[]
y_start=150
x_start=240
for i in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.speed("slow")
    new_turtle.penup()
    new_turtle.goto(x=-(x_start),y=y_start)
    y_start-=50
    turtles.append(new_turtle)
    
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
    


screen.exitonclick()
