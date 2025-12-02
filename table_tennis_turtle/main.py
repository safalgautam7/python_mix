from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from score import Scoreboard
Is_Game_Running =True
LEFT_POSITION=(-380,0)
RIGHT_POSITION=(380,0)
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

#objects
score=Scoreboard()
l_paddle=Paddle(LEFT_POSITION)
r_paddle=Paddle(RIGHT_POSITION)
ball=Ball()

screen.listen()
screen.onkey(lambda:r_paddle.move_right("Up"),key="Up")
screen.onkey(lambda:r_paddle.move_right("Down"),key="Down")
screen.onkey(lambda:l_paddle.move_left("w"),key="w")
screen.onkey(lambda:l_paddle.move_left("s"),key="s")


while Is_Game_Running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with left paddle
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_y()
    #Detect collision with right paddle
    if ball.distance(r_paddle)<50  and ball.xcor()>320 or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()
    #Detect if the ball is missed
    if ball.xcor()>=400:
        score.add_score_left()
        ball.reset()
    if ball.xcor()<=-400:
        ball.reset()
        score.add_score_right()
    if score.l_score>=11:
        score.winner("left")
        Is_Game_Running=False
    elif score.r_score>=11:
        score.winner("right")
        Is_Game_Running=False

    




screen.exitonclick()
