# Pyhton Tkinter Creating input Fields

from tkinter import *
root=  Tk()

def myClick():
    myLabel = Label(root, text= "Look i click a button!")
    myLabel.pack()



myButton = Button(root, text="Click Me!", padx=50, command=myClick)
myButton.pack()

root.mainloop()