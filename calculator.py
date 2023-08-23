from tkinter import *
import tkinter.font as fnt
from calculatorpro import calc


window=Tk()
window.title("CALCULATOR")
window.config(bg="grey")
a=window.winfo_screenheight()
b=window.winfo_screenwidth()                     
x=int((a/2)-(500/2))
y=int((b/2)-(500/2))
window.geometry("{}x{}+{}+{}".format(500,500,y,x))

font=fnt.Font(weight='bold')

label=Label(bg="black",width=50,height=4,text="Hello",fg="white",font=("courier",10))
label.pack()
def click(i):

    z=[bb,bm,bp,bd]
    g=label["text"]
    if label["text"]=="Hello":
        if (i==bb) or(i==bc) :
            label.config(text="")
        else:
            label.config(text=i["text"])
    elif i==be:
        label.config(text= str(calc(label["text"])))  
    elif i==bc:
        label.config(text="")
    elif i==bb:
        label.config(text=label["text"][:-1])
    else:
         label.config(text=label["text"]+i["text"])

        

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
bdo=Button(window,height=3,width=7,text=".",bg="white",command=lambda:click(bdo))
bdo.place(x=120,y=400)
bd=Button(window,height=3,width=17,text="/",bg="white",command=lambda:click(bd))
bd.place(x=190,y=400)
bp=Button(window,height=5,width=7,text="+",bg="white",command=lambda:click(bp))
bp.place(x=260,y=100)
bm=Button(window,height=5,width=7,text="-",bg="white",command=lambda:click(bm))
bm.place(x=260,y=200)
bi=Button(window,height=5,width=7,text="*",bg="white",command=lambda:click(bi))
bi.place(x=260,y=300)
be=Button(window,height=7,width=15,text="=",bg="lightgreen",command=lambda:click(be))
be.place(x=350,y=200)
bc=Button(window,height=7,width=15,text="clear",bg="#ffcccb",command=lambda:click(bc))
bc.place(x=350,y=340)
bb=Button(window,height=5,width=5,text="X\n<--",bg="lightblue",command=lambda:click(bb))
bb.place(x=350,y=100)

window.mainloop()
                   