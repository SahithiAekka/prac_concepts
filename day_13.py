# Debugging in Python 
# The first step of solving a problem is being able to describe the problem.

def my_function():
    for i in range(1, 20):  # 1. The for loop is iterating over numbers from 1 to 19 (inclusive of 1, exclusive of 20).
        if i == 20:         # 2. The function is meant to print "You got it" when i reaches the value 20.
            print("You got it")

my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#    - The for loop iterates through numbers from 1 to 19 (range(1, 20) gives 1 to 19).

# 2. When is the function meant to print "You got it"?
#    - The function is meant to print "You got it" when i is equal to 20.
#    - But this will never happen because the loop stops at 19 and never reaches 20.

# 3. What are your assumptions about the value of i?
#    - i takes values from 1 up to 19.
#    - i will **never** be 20 in this loop, so the condition `if i == 20` will never be True.

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])



# Playing computer 
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")
    
    
   
# ************************ TRY EXCEPT code***************************
try:
    age= int(input("How old are you? "))
except ValueError:
    print("You have typed in a an invalid number. Pl try again with a numerical response like 17")
    age=int(input("How old are you?? "))
    
if age < 18:
    print(f"You can't drive at the age of {age}")
    

# *******************************************  How to use a debugger **********************************************************************
# Breakpoint -- breaking line higlighted . puts a break on code at that particular line then you go to the debug run mode 
# step over button - execute code line by line  
# step into button - execute code line ny line , shows how built in function in python work. 
# ignore library function written by python  you can use step over button 
# step out - exit debugging mode 
# two tabs: thread and variables-- shows values of varibales in the code through out 
        #  console

# Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. 
# This is normally known as the debugger. In many ways, they are like print statements on steroids.

# Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

# There are a couple of things that are the same in most IDEs which you should be familiar with:

# Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). 
#              This line will be where the program pauses during debug run.

# Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.

# Step Into - This will enter into any other modules that your code references. e.g. 
#             If you use a function from the random module it will show you the original code for that 
#             function so you can better understand its functionality and how it relates to your problems.

# Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random