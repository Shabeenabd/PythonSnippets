#--------------importing libraries
from tkinter import *
import tkinter.font as fnt
from calculatorpro import calc

#--------------creating a GUI window
window=Tk()
#--------------setting window title
window.title("CALCULATOR")
#--------------setting window background color
window.config(bg="grey")
#---------------getting window height and weight measures
a=window.winfo_screenheight()
b=window.winfo_screenwidth()    
#----------------aligning window to the center
x=int((a/2)-(500/2))
y=int((b/2)-(500/2))
window.geometry("{}x{}+{}+{}".format(500,500,y,x))

#----------selecting font
font=fnt.Font(weight='bold')
#-----------craeting the output screen
label=Label(bg="black",width=50,height=4,text="Hello",fg="white",font=("courier",10))
#-----------adding the output screen on the window
label.pack()

#-----------function to do calculation /computing
def click(i):
    #---------grouping similar buttons 
    z=[bb,bm,bp,bd]
    g=label["text
    #----------changing output screen text
    if label["text"]=="Hello":
    #-----------clearing screen
        if (i==bb) or(i==bc) :
            label.config(text="")
        else:
            label.config(text=i["text"])
    #-----------by pressing "equals" button ,passing  the string value to the calculation function and receiving output and showing to the screen
    elif i==be:
        label.config(text= str(calc(label["text"])))  
    elif i==bc:
    #-----------to clear the output screen
        label.config(text="")
    elif i==bb:
    #----------to clear the last value
        label.config(text=label["text"][:-1])
    else:
    #-----------to append the clicked value to the string
         label.config(text=label["text"]+i["text"])

        
#--------------creating  buttons with numbers and operators
#--------------adding on to the window
#--------------defining functions on clicking the button
#--------------setting button height,width,xposition,yposition,background colour
#--------------number from 0 to 9
b7=Button(window,height=5,width=7,text="7",bg="white",command=lambda:click(b7))
b7.place(x=50,y=100)
b8=Button(window,height=5,width=7,text="8",bg="white",command=lambda:click(b8))
b8.place(x=120,y=100)
b9=Button(window,height=5,width=7,text="9",bg="white",command=lambda:click(b9))
b9.place(x=190,y=100)
b4=Button(window,height=5,width=7,text="4",bg="white",command=lambda:click(b4))
b4.place(x=50,y=200)
b5=Button(window,height=5,width=7,text="5",bg="white",command=lambda:click(b5))
b5.place(x=120,y=200)
b6=Button(window,height=5,width=7,text="6",bg="white",command=lambda:click(b6))
b6.place(x=190,y=200)
b1=Button(window,height=5,width=7,text="1",bg="white",command=lambda:click(b1))
b1.place(x=50,y=300)
b2=Button(window,height=5,width=7,text="2",bg="white",command=lambda:click(b2))
b2.place(x=120,y=300)
b3=Button(window,height=5,width=7,text="3",bg="white",command=lambda:click(b3))
b3.place(x=190,y=300)
b0=Button(window,height=3,width=7,text="0",bg="white",command=lambda:click(b0))
b0.place(x=50,y=400)
#-------------dot button
bdo=Button(window,height=3,width=7,text=".",bg="white",command=lambda:click(bdo))
bdo.place(x=120,y=400)
#--------------division operator button
bd=Button(window,height=3,width=17,text="/",bg="white",command=lambda:click(bd))
bd.place(x=190,y=400)
#--------------addition operator bitton
bp=Button(window,height=5,width=7,text="+",bg="white",command=lambda:click(bp))
bp.place(x=260,y=100)
#-------------substraction operator button
bm=Button(window,height=5,width=7,text="-",bg="white",command=lambda:click(bm))
bm.place(x=260,y=200
#--------------multiplication operator button
bi=Button(window,height=5,width=7,text="*",bg="white",command=lambda:click(bi))
bi.place(x=260,y=300)
#----------------equal to button
be=Button(window,height=7,width=15,text="=",bg="lightgreen",command=lambda:click(be))
be.place(x=350,y=200)
#--------------clear button to clear the screen
bc=Button(window,height=7,width=15,text="clear",bg="#ffcccb",command=lambda:click(bc))
bc.place(x=350,y=340)
#--------------clear button to clear the last element
bb=Button(window,height=5,width=5,text="X\n<--",bg="lightblue",command=lambda:click(bb))
bb.place(x=350,y=100)

#--------------looping the code to show the window
window.mainloop()
                   
