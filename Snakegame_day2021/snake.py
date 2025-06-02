from turtle import Turtle, Screen

STARTING_POSITIONS=[(0,0), (-20,0), (-40,0)]  # in python for constants 
MOVE_DISTANCE= 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self): #creating a snake body 
        for position in STARTING_POSITIONS:
            new_segment =Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
                
    def move(self): #moving the snake 
        for segment_num in range(len(self.segments)-1, 0, -1):
            new_x= self.segments[segment_num - 1].xcor()
            new_y= self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)   
    
    def up(self):
        self.segments[0].setheading(90)
    
    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)

     


