import random
import turtle as t
screen = t.Screen()
turtle = t.Turtle()
t.colormode(255)
turtle.shape("turtle")
# Updated color list with more variety
Color = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta", "pink", "lime", "brown"]


directions=[0,90,100,270]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color= (r,g,b)
    return random_color
turtle_position = turtle.pos()
turtle.pensize(15)
for i  in range(200):
    turtle.color(random_color())
    turtle.speed("fastest")
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
    
screen.exitonclick()
