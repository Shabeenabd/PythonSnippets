# Importing libraries
from tkinter import *
import tkinter.font as fnt
try:
	from custom_eval import eval
except Exception as e:
	print("using default eval function",e)

# Creating a GUI window
window = Tk()

window.title("CALCULATOR")   # Setting window title
window.config(bg="grey")     # Setting window background color

# Getting window height and weight measures
height = window.winfo_screenheight()
width = window.winfo_screenwidth()    

# Aligning window to the center
x = int((height/2)-(500/2))
y = int((width/2)-(500/2))
window.geometry("{}x{}+{}+{}".format(500,500,y,x))

font = fnt.Font(weight='bold')  # Selecting font
label = Label(bg="black",width=50,height=4,text="Hello",fg="white",font=("courier",10))    # Creating the output screen
label.pack()   # Adding the output screen on the window

# Function to do calculation /computing
def click(i):
    # Grouping similar buttons 
#    z=[b_clr_last,b_sub,b_add,b_div]
 #   g=label["text"]
    # Changing output screen text
    if label["text"]=="Hello":
    # Clearing screen
        if (i==b_clr_last) or(i==b_clr) :
            label.config(text="")
        elif i==b_quit :
        	label.config(text="Fuck Off")
        	window.destroy()    
        else:
            label.config(text=i["text"])
    # By pressing "equals" button ,passing  the string value to the calculation function and receiving output and showing to the screen
    elif i==b_eq:
        label.config(text= str(eval(label["text"])))  
    elif i==b_clr:
    # To clear the output screen
        label.config(text="")
    elif i==b_clr_last:
    # To clear the last value
        label.config(text=label["text"][:-1])
    elif i==b_quit    :
    # To show some special value
        label.config(text="Fuck Off")
        window.destroy()
    else:
    # To append the clicked value to the string
         label.config(text=label["text"]+i["text"])

        
# Creating  buttons with numbers and operators and defining functions on clicking the button
# Setting button height,width,xposition,yposition,background colour
# buttins from 0 to 9
b7 = Button(window,height=5,width=7,text="7",bg="white",command=lambda:click(b7))
b7.place(x=50,y=100)
b8 = Button(window,height=5,width=7,text="8",bg="white",command=lambda:click(b8))
b8.place(x=120,y=100)
b9 = Button(window,height=5,width=7,text="9",bg="white",command=lambda:click(b9))
b9.place(x=190,y=100)
b4 = Button(window,height=5,width=7,text="4",bg="white",command=lambda:click(b4))
b4.place(x=50,y=200)
b5 = Button(window,height=5,width=7,text="5",bg="white",command=lambda:click(b5))
b5.place(x=120,y=200)
b6 = Button(window,height=5,width=7,text="6",bg="white",command=lambda:click(b6))
b6.place(x=190,y=200)
b1 = Button(window,height=5,width=7,text="1",bg="white",command=lambda:click(b1))
b1.place(x=50,y=300)
b2 = Button(window,height=5,width=7,text="2",bg="white",command=lambda:click(b2))
b2.place(x=120,y=300)
b3 = Button(window,height=5,width=7,text="3",bg="white",command=lambda:click(b3))
b3.place(x=190,y=300)
b0 = Button(window,height=3,width=7,text="0",bg="white",command=lambda:click(b0))
b0.place(x=50,y=400)
# Dot button
b_dot = Button(window,height=3,width=7,text=".",bg="white",command=lambda:click(b_dot))
b_dot.place(x=120,y=400)
# Division operator button
b_div = Button(window,height=3,width=16,text="/",bg="white",command=lambda:click(b_div))
b_div.place(x=190,y=400)
# Addition operator b_multton
b_add = Button(window,height=5,width=7,text="+",bg="white",command=lambda:click(b_add))
b_add.place(x=260,y=100)
# Substraction operator button
b_sub = Button(window,height=5,width=7,text="-",bg="white",command=lambda:click(b_sub))
b_sub.place(x=260,y=200)
# Multiplication operator button
b_mul = Button(window,height=5,width=7,text="*",bg="white",command=lambda:click(b_mul))
b_mul.place(x=260,y=300)
# Equal to button
b_eq = Button(window,height=5,width=7,text="=",bg="lightgreen",command=lambda:click(b_eq))
b_eq.place(x=350,y=200)
# Clear button to clear the screen
b_clr = Button(window,height=5,width=7,text="clear",bg="#c42e23",command=lambda:click(b_clr))
b_clr.place(x=350,y=300)
# clear button to clear the last element
b_clr_last = Button(window,height=5,width=5,text="X\n<--",bg="#535a73",command=lambda:click(b_clr_last))
b_clr_last.place(x=350,y=100)
# extra functional button
b_quit = Button(window,height=3,width=7,text="quit",bg="#008080",command=lambda:click(b_quit))
b_quit.place(x=350,y=400)

# Looping the code to show the window
window.mainloop()                
