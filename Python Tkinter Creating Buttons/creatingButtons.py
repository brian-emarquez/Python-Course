# Python Tkinter Creating Buttons
# Python Tkinter Creación de botones

from tkinter import *
root=  Tk()

def myClick():
    myLabel = Label(root, text= "Look i click a button!")
    myLabel.pack()



myButton = Button(root, text="Click Me!", padx=50, command=myClick)
myButton.pack()

root.mainloop()