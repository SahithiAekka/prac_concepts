# Functions 

# defining a function 
def my_func(): 
    print("This is an example of fuction")
    
# calling the function   
my_func()

#  reborg 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one_loop():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# def race():
#     one_loop()
#     one_loop()
#     one_loop()
#     one_loop()
#     one_loop()
#     one_loop()

# race()

# Indentation in python is very importnat espcially when it comes to loops 

sky = input("How is the sky like today? Cloudy?? Clear? Don't know?? ")

def fun_1():
    if sky == "Clear":
        print("The weather is lovely today")
    elif sky == "Cloudy":
        print("It seems to be rainy. Make sure to carry an umbrella")
    elif sky == "Don't know":
        print("Girl, I don't know no weather")
    else:
        print("Invalid input. Please enter Clear, Cloudy, or Don't know.")

fun_1()

# spaces or tab?? for indentation : They say spaces are better 

# While loop : loop that will continue going while the condition is true 

# Hurdles race
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# What you need to know
# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.
# Your program should also be valid for world Hurdles 1.

# Difficulty level



# Reborg maze 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not wall_in_front():
    move()
turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move() 
    elif not wall_in_front():
        move()
    else:
        turn_left()
