# Creating Input fields

# Python Tkinter Positioning
from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "hello " + e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack()



myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()


root.mainloop()