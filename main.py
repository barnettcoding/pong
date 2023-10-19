from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG!!!")
screen.tracer(0)
time_inc = .1


p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p2.go_up, "Up")
screen.onkey(p2.go_down, "Down")
screen.onkey(p1.go_down, "s")
screen.onkey(p1.go_up, "w")
game_is_on = True
from scoreboard import Scoreboard

while game_is_on:
    time.sleep(time_inc)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("top/bottom")
    if ball.xcor() > 320 and ball.distance(p2) < 50:
        ball.bounce("paddle")
        time_inc -=.01
    elif ball.xcor() > 380 and ball.distance(p2) > 50:
        scoreboard.p1_score += 1
        scoreboard.update_score()
        if scoreboard.p1_score >= 10:
            scoreboard.game_over(1)
            game_is_on = False
        time_inc = .1
        ball.reset()
        
    if ball.xcor() < -320 and ball.distance(p1) < 50:
        ball.bounce("paddle")
        time_inc -= .01
    elif ball.xcor() < -380 and ball.distance(p2) > 50:
        scoreboard.p2_score += 1
        scoreboard.update_score()
        if scoreboard.p2_score >= 10:
            scoreboard.game_over(2)
            game_is_on = False
        time_inc = .1
        ball.reset()
       


        
    




screen.exitonclick()