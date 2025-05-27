# OOPS 
# Procedural programing - earliest method but the increase in complexity has made it hard to mantain 
# Object oreiented progarm -- SPlit a larger tasks into smaller tasks which are reusable 
# reusable modules  scalable , sipmlyfy the relationships
# trying to model a real world object  
# while trying to model a waiter you have to thk of two things : what the waiter HAS ------ ATTRIBUTE  = variable taht is attached to a articular object 

                                                            #    what the waiter DOES ----- METHODS = modeled by fucntion \
# we can genearate  multiple versions of the waiter like John , Betty using something called as a blueprint

# over here the          waiter(CLASS )               John, Betty  (OBJECTS )
                                                     
# from the blue print which is the class we can generate as many objects as we want                                                      

# object--> car = Carblueprint() <-- class = uses Pascal case             
# object has attributes like the oject car has speed as one of its attributres 

# Screen = Return the singleton screen object. If none exists at the moment, create a new one and return it, else return the existing one.- represents tkhw windopw in which turtel is going to show up 

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.width(6)
timmy.color("pink")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)

timmy.forward(20)
timmy.color('red')
timmy.circle(200)


import turtle as t
from random import random

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

my_screen= Screen()
print(my_screen.canvheight)

my_screen.exitonclick()
# this shows up the sceen and the code will only exit when you click on the screen 


# Object methods  --  


# Pythonn packages 
# prettytable packageeee 