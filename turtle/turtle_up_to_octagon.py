#drawing a square 
from turtle import Turtle,Screen
turtle=Turtle()
turtle.shape("arrow")
turtle.color("red")
##NOTE: drawing a square
# for i in range(0,4):
#     turtle.forward(100)#turtle moves forward by 90 steps
#     turtle.left(90)

##NOTE: drawing a dash line 
# for i in range(0,50):
    # turtle.forward(5)
    # turtle.penup()#no drawing when moving 
    # turtle.forward(5)
    # turtle.pendown()#drawing when moving
    
##NOTE: Draw a triangle,square,pentagon, hexagon, heptagon, octagon, nonagon and decagon
color = ["gray","gray0","gray10","gray20","gray30","gray40","gray50","gray60","gray70","gray80","gray90"]

turtle_position=turtle.pos()
for i in range (3):
    turtle.forward(100)
    turtle.right(120)
    
turtle.goto(turtle_position)

#NOTE: to draw a square 
for i in range(0,4):
    turtle.forward(100)#turtle moves forward by 90 steps
    turtle.right(90)
turtle.goto(turtle_position)

#NOTE: to draw a pentagon 
for i in range(5):
    turtle.forward(100)
    turtle.right(72)
turtle.goto(turtle_position)

#NOTE: to draw a hexagon
for i in range(6):
    turtle.forward(100)
    turtle.right(60)
turtle.goto(turtle_position)

#NOTE: to draw a heptagon
for i in range(7):
    turtle.forward(100)
    turtle.right(51.43)
turtle.goto(turtle_position)

#NOTE: to draw an octagon
for i in range(8):
    turtle.forward(100)
    turtle.right(45)
turtle.goto(turtle_position)

#NOTE: to draw a nonagon 
for i in range(9):
    turtle.forward(100)
    turtle.right(40)
turtle.goto(turtle_position)

for i in range(10):
    turtle.forward(100)
    turtle.right(36)

screen=Screen()
screen.exitonclick()