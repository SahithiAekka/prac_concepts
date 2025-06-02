#  More Turtle graphics, event listners, state and miltiple instances 
from turtle import Turtle, Screen, textinput
import random

# passing function as input to another fuction for example func_a(func_b) - you see how func_b doesn't have () 
# over here func_a is called a HIGHER ORDER FUNCTION 

#  ********** EVENT LISTNER **********
# Event listeners let you respond to user input, like key presses or mouse clicks. 
# These listeners are set up using specific functions that tell Turtle to "listen for" an event and then "do something" when it happens.

tim = Turtle()
# screen = turtle.Screen()

def move_forward():
    tim.forward(100)
    
def move_back():
    tim.backward(100)
    
def move_right():
    tim.right(10)
    
def move_left():
    tim.left(10)

screen = Screen()
screen.listen()
screen.onkey(move_forward, "f")   
screen.onkey(move_back,"b")
screen.onkey(move_right,"r")
screen.onkey(move_left,"l")

screen.exitonclick()

