import random 
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

# Updated color list with more variety
Color = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta", "pink", "lime", "brown"]

turtle_position = turtle.pos()

i = 3
j = 0
geometric_side = 3

while i != 12:
    j = 0
    geometric_angle = 360 / geometric_side
    while j < i:
        turtle.color(random.choice(Color))
        turtle.forward(100)
        turtle.right(geometric_angle)
        j += 1
    i += 1
    geometric_side += 1

screen.exitonclick()
