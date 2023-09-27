#My code creates three different sets of turtles. each set doing something differently.

# Draws several lines radiating out from the origin. 
import turtle
import random

#create StampTurtle class for the first two sets with turtle.Turtle as its parent
class StampTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    def __init__(self):
        super().__init__()
    #function to make the first two sets of turtle to go forward   
    def forward(self, dist):
        self.right(360)
        super().forward(dist)
        self.stamp()
    #same as forward but backwards this time, added a change of color for every turn the turtle makes    
    def backward(self, dist):
        super().backward(dist)
        self.stamp()
        self.right(360)
        self.color(random.choice(['red','green','blue','yellow', 'pink']))
#created a new class for two different turtles, using StampTurtle as the parent        
class NewTurtles(StampTurtle):
    def __init__(self):
        super().__init__()
        
    def forward(self, dist):
        self.right(random.randrange(360))
        super().forward(dist)
        self.stamp()     
#main function where we create each turtle and append them to their own list        
def main():
    # named constants
    screen_size = 500
    screen_startx = 60 # x coordinate of the left edge of the graphics window
    # Set up the window and its attributes
    wn = turtle.Screen()              
    wn.setup(screen_size, screen_size, screen_startx, 0)
    
    turtle_list = []
    num_turtles = 2
    num_stamp_turtles = 3
    new_turtles = 2
    new_turtle_list = []
    
    # Create a list of different colored turtles, each pointing
    #   in a different direction
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.right(random.randrange(350))
        t.color(random.choice(['red','green','blue','yellow']))
        t.speed(7)
        turtle_list.append(t)
    
    # Create a list of different colored stamp_turtles, each pointing
    #   in a different direction
    
    for _ in range(num_stamp_turtles):
        t = StampTurtle()
        t.right(random.randrange(350))
        t.speed(7)     
        turtle_list.append(t)
    #the new turtles are creates in the folowwing for loop   
    for _ in range(new_turtles):
        t = NewTurtles()
        t.pensize(2)
        t.shape('turtle')
        t.penup()
        t.goto(75,75)
        t.pendown()
        t.color(random.choice(['lightblue', 'pink']))
        t.right(random.randrange(350))
        t.speed(7)
        new_turtle_list.append(t)
    
    # Move each turtle outward from the origin ten times
    for t in turtle_list:
        for _ in range(10):
            t.backward(random.randrange(10,30))
            
    for t in new_turtle_list:
        for _ in range(15):
            t.forward(random.randrange(10,30))
            
    wn.exitonclick()

main()