import random
from turtle import Turtle, Screen, textinput

screen = Screen()
screen.setup(width=550, height=400)
user_bet= textinput("Make your bet","Which turtle do you think will win the race?? ")


turtle_colors =["red", "blue", "green", "orange", "purple", "pink"]
turtle_object =[]

for index, t_color in enumerate(turtle_colors):
    t = Turtle(shape="turtle")
    t.color(t_color)
    # print(t_color)
    # print(t.color())
    t.penup()
    t.goto(x=-230, y=-100 + index * 40)
    turtle_object.append(t)

# print(turtle_object)
# make sure variables are local. RAM storage minimal which makes it efficient , make sure arguments are minimal 

# # if user_bet:
# #     is_race_on = True

flag = True   
while flag: 
    for race_turtle in turtle_object:  
        race_turtle.forward(random.randint(0,10))
        # if race_turtle.pos()
        value_x=race_turtle.pos()[0]
        # print(value_x)
        if value_x >= 250:
            flag = False
            winner_name= race_turtle.color()[0]
            break
        
        
# print(f"Race completed. the winner is {winner_name}")

if user_bet == winner_name:
    print(f"You guessed it right. The winner is {winner_name}")
else:
    print(f"You lost the bet. The winner is {winner_name}")




# enumerate() is a built-in Python function that lets you loop over a list while keeping track of the index (position) of each item.


    

screen.exitonclick()
