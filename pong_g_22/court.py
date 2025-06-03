from turtle import Turtle

class Court:

    def __init__(self):
        self.drawer = Turtle()
        self.drawer.color("black")
        self.drawer.pensize(3)
        self.drawer.hideturtle()
        self.drawer.speed("fastest")
        self.draw_outer_box()
        self.draw_net()

    def draw_outer_box(self):
        self.drawer.penup()
        self.drawer.goto(-390, 290)  # top-left corner
        self.drawer.pendown()
        for _ in range(2):
            self.drawer.forward(780)  # width
            self.drawer.right(90)
            self.drawer.forward(580)  # height
            self.drawer.right(90)

    def draw_net(self):
        self.drawer.penup()
        self.drawer.goto(0, 290)
        self.drawer.setheading(-90)
        self.drawer.pendown()
        for _ in range(29):  # dashed center line
            self.drawer.forward(10)
            self.drawer.penup()
            self.drawer.forward(10)
            self.drawer.pendown()