from turtle import Turtle, Screen

STARTING_POSITIONS=[(0,0), (-20,0), (-40,0)]  # in python for constants 
MOVE_DISTANCE= 20
UP = 90
DOWN = 270 
RIGHT = 0 
LEFT = 180

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self): #creating a snake body 
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self,position):
        new_segment =Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1])

    def move(self): #moving the snake 
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x= self.segments[segment_num - 1].xcor()
            new_y= self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE) 
    
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    



     


