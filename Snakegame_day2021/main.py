from turtle import Screen
import  time 
from snake import Snake
from food import Food
from score_board import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Pink")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

flag = True
while flag:
    screen.update()
    time.sleep(0.1) # delay 0.1 sec and refresh the screen 
    snake.move()  
    
    # Detecting food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    # Detecting wall 
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280 :
        flag = False
        scoreboard.game_over()
    
    # Detecting collosion with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

        
   
        

# distance() : distance method in turtle compares the distance from this turtle to whatever it is that you put inside the paranthesis 
 





  




screen.exitonclick()
