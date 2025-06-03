from turtle import  Turtle, Screen
import random, time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from court import Court

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("lightgreen")
screen.title("PONG PONG PONG")
screen.tracer(0)

r_paddle=Paddle((350, 0))
l_paddle=Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
Court()
Winning_score= 5
    
screen.listen()
screen.onkey(r_paddle.go_up, "Up") #controling right paddle 
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")  #controling left paddle 
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on: 
    time.sleep(0.1)
    screen.update() 
    ball.move()
    
    #Detect collison with wall 
    if ball.ycor() > 280 or ball.ycor() < -280: 
         ball.bounce_y()

    # Detect collison with right paddle
    if 320 < ball.xcor() < 350 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        
    # Detect collison with left paddle
    if -350 < ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        
    # Detect if ball misses r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if ball misses l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
    # Check winner     
    if scoreboard.l_score == Winning_score:
        scoreboard.game_over("Left Player Wins!")
        game_is_on = False

    if scoreboard.r_score == Winning_score:
        scoreboard.game_over("Right Player Wins!")
        game_is_on = False
         
screen.exitonclick()

