import colorgram
import random 
import turtle as turtle_module
from turtle import Screen

# # Extract 6 colors from an image.
# colors = colorgram.extract('dhirst.jpg', 6)
# rgb_colors=[]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(255, 255, 204),  (255, 192, 203),  (173, 216, 230),  (152, 251, 152),  (216, 191, 216),  (255, 204, 153)  ]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots= 100


for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    
    if dot_count%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




















screen = Screen()
screen.exitonclick()

