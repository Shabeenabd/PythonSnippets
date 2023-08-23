from turtle import *
import random
import time
delay=0.1
w=Screen()
w.bgcolor("teal")
w.setup(height=610,width=610)
w.tracer(0)
line=Turtle()
line.penup()
line.pensize(10)
line.speed(0)
line.goto(295,-295)
line.pendown()
line.goto(295,300)
line.goto(-300,300)
line.goto(-300,-295)
line.goto(295,-295)
head=Turtle(shape="circle")
head.speed(0)
head.penup()
head.color("white")
direction=0
food=Turtle(shape="turtle")
food.penup()
food.goto(0,100)
food.speed(0)
clr=random.choice(["red","yellow","maroon","pink","lightblue"])
food.color(clr)
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
    
def move():
    x=head.xcor()
    y=head.ycor()
    if direction==1:
        head.sety(y+10)
    elif direction==2:
        head.sety(y-10)
    elif direction==3:
        head.setx(x+10)
    elif direction==4:
        head.setx(x-10)  
    elif direction==0:
        head.setx(x)
    elif direction==5:
         print("exiting")

w.listen()
w.onkeypress(lambda : dire(1),"w")
w.onkeypress(lambda : dire(2),"s")
w.onkeypress(lambda : dire(3),"d")
w.onkeypress(lambda : dire(4),"a")
w.onkeypress(lambda : dire(5),"q")
segmets=[]
c=False
while True:

    if head.xcor()>285 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-285:
        
        time.sleep(1)
        
        head.home()
        
        direction=0
    if head.distance(food)<15:
        x=random.randint(-295,285)
        y=random.randint(-285,285)
        clr=random.choice(["red","yellow","maroon","pink","lightblue"])
        food.color(clr)
        food.goto(x,y)
        delay-=0.001
        
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
        
    w.update()
    for i in range(len(segmets)-1,0,-1):
                   x=segmets[i-1].xcor()
                   y=segmets[i-1].ycor()
                   segmets[i].showturtle()
                   segmets[i].goto(x,y)
    if len(segmets)>0:
        segmets[0].showturtle()
        segmets[0].goto(head.xcor(),head.ycor())

     
    move()
    if direction==5:
         break
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

