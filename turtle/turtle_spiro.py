import random
import turtle as t
screen = t.Screen()
turtle = t.Turtle()
t.colormode(255)
turtle.shape("turtle")
turtle.speed("fastest")


directions=[0,90,100,270]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color= (r,g,b)
    return random_color
#drawing a spiral
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle.color(random_color())
        turtle.circle(60)
        current_heading=turtle.heading()
        turtle.setheading(current_heading+size_of_gap)
draw_spirograph(5)
    


screen.exitonclick()