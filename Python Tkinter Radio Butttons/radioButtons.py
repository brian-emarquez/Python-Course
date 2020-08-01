# Python Tkinter Radio Butttons

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Python')
root.iconbitmap('Python Tkinter Radio Butttons/icon.ico')

r = IntVar()
r.set("2")

MODES = [

    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),

]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="Click Me", command=lambda: clicked(pizza.get()))
myButton.pack()


root.mainloop()