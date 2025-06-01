import turtle
from turtle import Turtle, Screen
import random



# Alias modules
# import turtle as t

# installing modules -- gets installed into local virtual env
# import heroes



# tim =  Turtle()
# tom = Turtle()
# terry = Turtle()
#
# tim.shape("turtle")
# tim.color("plum")
# for i in range(0,4):
#     tim.forward(100)
#     tim.right(90)
#
#
#
# tom.pos()
# tom.shape("turtle")
# tom.color("purple")
# tom.goto(40,50)
#
#
# terry.shape("turtle")
# terry.color("red")
# terry.forward(250)
# terry.circle(50)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.right(50)
# timmy_the_turtle.forward(70)
# timmy_the_turtle.circle(30)




# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# GUI- Graphical User Interface

# drawing a dotted lien
j= Turtle()
# for i in range(15):
#     j.forward(20)
#     j.penup()
#     j.forward(20)
#     j.pendown()

# Creating all the shapes
# def draw_shape(num_sides):
#     angle= 360/ num_sides
#     for i in range (num_sides):
#         j.forward(100)
#         j.right(angle)
#
# for shape_side_n in range(3,12):
#     draw_shape(shape_side_n)


# # turtle doing a random walk
# # colors=["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan", "magenta", "turquoise", "gold", "brown", "gray", "navy", "violet", "lime", "maroon"]
# turtle.colormode(255)
# def random_color():
#     r= random.randint(0,255)
#     b= random.randint(0,255)
#     g=random.randint(0,255)
#     randomcolor=(r, g, b)
#     return randomcolor

# directions = [0, 90, 180, 270]
# j.pensize(15)
# j.speed("fastest")

# for _ in range(200):
#     j.color((random_color()))
#     j.forward(30)
#     j.setheading(random.choice(directions))


# tuple : data type in python that is similar to list with curved brackets . we can't change the contents of a tuple
#  once created it  is immutable . can't be changed . to change it you can put it in a list and  make it a list


# sipograph

turtle.colormode(255)
def random_color():
    r= random.randint(0,255)
    b= random.randint(0,255)
    g=random.randint(0,255)
    randomcolor=(r, g, b)
    return randomcolor

j.speed("fastest")

for i in range (0,72):
    j.color(random_color())
    j.circle(100)
    j.right(5)



screen = Screen()
screen.bgcolor("salmon")

screen.exitonclick()

# Turtle dashed line

