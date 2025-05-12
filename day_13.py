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