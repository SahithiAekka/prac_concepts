from turtle import Turtle, Screen
import  time 
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("My Snake game")
screen.tracer(0)


# screen.update() updtaes the screen and makes it better looking 

snake = Snake()

flag = True
while flag:
    screen.update()
    time.sleep(0.1) # delay 0.1 sec and refresh the screen 
    
    snake.move()       


# Controlling the snake movement 

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


snake.move()

screen.onkey   





    
    


    













screen.exitonclick()
