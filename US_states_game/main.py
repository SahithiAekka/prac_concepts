import turtle
import pandas

data = pandas.read_csv("50_states.csv")
new_state = data["state"].to_list()
guessed_states=[]


# print(new_state)

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)
# screen.listen()
# turtle.onscreenclick(get_mouse_click_coor)

while len(guessed_states) <50: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats another state's name? ").title()

#title case - will let you accept all answers 
# check if the answer is one the states in all the states 
# if they got it writ create a turtle then how to write it on the screen in turtle game 

    if answer_state== "Exit":
        missing_states=[]
        for state in new_state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if answer_state in new_state:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state== answer_state]
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(answer_state)

# item is a methon on panda series, it will fetch the value without any index 




screen.exitonclick()

