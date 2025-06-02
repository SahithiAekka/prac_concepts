# Conditional statements , comaprision operators, modulo operator, nested if else, elif statements, logical operator 
# if condition:
#       do this 
# else:
#       do this 

#spacing and indentation is very very importnat 

# Comparator Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the roller coaster")
# else:
#     print("you are not allowed ")

# Modulo operator 
number_to_check= int(input("what is the number you wnat to chck?"))
if number_to_check % 2 == 0:
    print("even")
else:
    print("odd")


# # Nested if else 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("how old are you?"))
    if age <= 18:
        print("you have to pay 7$")
    else:
        print("you have to pay 12$")
else:
    print("Sorry you have to grow taller before you can ride.")


# elif statements 
# if condition1:
#       do A 
# elif condiition2:
#       do B
# else:
#     do C
# you can add as many as elif as you wnat 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("how old are you?"))
    if age <= 12:
        print("you have to pay 5$")
    elif age<=18:
        print("you have to pay 7$")
    elif age== 25:
        print("you are perfect")
    else:
        print("you have to pay 12$")
else:
    print("Sorry you have to grow taller before you can ride.")


# MULTIPLE IF 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adults tickets are $12.")
    wants_photo=input("Do you want a photo? It costs 3$ \nType Y for yes and N for no")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

# LOGICAL OPERATORS 
#**************************AND *************************************
#OR
#NOT 

