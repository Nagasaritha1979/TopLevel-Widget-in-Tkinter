from tkinter import *
win=Tk()
win.geometry("200x200")
win.title("BLUE WINDOW")
win.config(bg="blue")


w1=Button(win,text="Green Window", command=lambda:open())
w1.pack(side=BOTTOM)

w5=Button(win,text="Close",command=win.destroy)
w5.pack(side=BOTTOM)

def open():
    child=Toplevel(win)
    child.geometry("200x200")
    child.title("GREEN WINDOW")
    child.config(bg="green")
    w2=Button(child,text="Red Window",command=lambda:open1())
    w2.pack(side=BOTTOM)
    w4=Button(child,text="Close",command=child.destroy)
    w4.pack(side=BOTTOM)
    
def open1():
    child2=Toplevel(win)
    child2.geometry("200x200")
    child2.title("RED WINDOW")
    child2.config(bg="red")
    w3=Button(child2,text="Close",command=child2.destroy)
    w3.pack(side=BOTTOM)

win.mainloop()    
