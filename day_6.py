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
