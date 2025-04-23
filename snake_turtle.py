# Import necessary modules
from turtle import *
import random
import time

delay = 0.1  # Game delay between movements

# Set up the game window
w = Screen()             # Background color
w.bgcolor("teal")        # Set the window size
w.setup(height=610,width=610)    # Turn off screen updates for smoother animation
w.tracer(0)

# Draw game boundary
line = Turtle()
line.penup()
line.pensize(10)
line.speed(0)
line.goto(295,-295)
line.pendown()
line.goto(295,300)
line.goto(-300,300)
line.goto(-300,-295)
line.goto(295,-295)

# Create the snake's head
head = Turtle(shape="circle")
head.speed(0)
head.penup()
head.color("white")

# Movement direction variable
direction = 0      # 0 = Stop, 1 = Up, 2 = Down, 3 = Right, 4 = Left, 5 = Quit

# Create the food
food = Turtle(shape="turtle")
food.penup()
food.goto(0,100)
food.speed(0)
clr = random.choice(["red","yellow","maroon","pink","lightblue"])
food.color(clr)

# Function to change the direction of the snake
def dire(x):
    global direction
    if x==1:
        direction=1
    if x==2:
        direction=2
    if x==3:
        direction=3
    if x==4:
        direction=4
    if x==5:
        direction=5

# Function to move the snake    
def move():
    x = head.xcor()
    y = head.ycor()
    if direction==1:   # Up
        head.sety(y+10)
    elif direction==2: # Down	 
        head.sety(y-10)
    elif direction==3: # Right
        head.setx(x+10)
    elif direction==4: # Left
        head.setx(x-10)  
    elif direction==0: # Stop
        head.setx(x)
    elif direction==5: # Quit
         print("exiting")

# Set up keyboard controls
w.listen()
w.onkeypress(lambda : dire(1),"w")
w.onkeypress(lambda : dire(2),"s")
w.onkeypress(lambda : dire(3),"d")
w.onkeypress(lambda : dire(4),"a")
w.onkeypress(lambda : dire(5),"q")

# Initialize body segments list
segmets = []
c = False  # Color toggle for body segments

# Main game loop
while True:
	# Check for collision with wall
    if head.xcor()>285 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-285:
        time.sleep(1)        
        head.home()
        direction=0
    
    # Check for collision with food    
    if head.distance(food)<15:
    	# Move food to new random location
        x = random.randint(-295,285)
        y = random.randint(-285,285)
        clr=random.choice(["red","yellow","maroon","pink","lightblue"])
        food.color(clr)
        food.goto(x,y)
        
        # Increase game speed
        delay-=0.001
        
        # Create new segment
        ns=Turtle(shape="circle")
        ns.hideturtle()
        segmets.append(ns)

        ns.penup()
        if c:
             ns.color("white")
             c=False
        else:
             ns.color("black")
             c=True
	
	# Update screen        
    w.update()
    
    # Move body segments
    for i in range(len(segmets)-1,0,-1):
                   x=segmets[i-1].xcor()
                   y=segmets[i-1].ycor()
                   segmets[i].showturtle()
                   segmets[i].goto(x,y)
                   
	# First segment follows the head                   
    if len(segmets)>0:
        segmets[0].showturtle()
        segmets[0].goto(head.xcor(),head.ycor())

     # Move the snake
    move()
    if direction==5:
         break
         
	# Check for collision with body         
    for i in segmets:
         if head.distance(i)<10:
        
            time.sleep(1)
            direction=0
            head.home()
            i.goto(1000,1000)
            segmets.clear
            c=False
            delay=0.1
    time.sleep(delay)

