# Python Tkinter Transparent Windows
# Ventanas transparentes de Python Tkinter

from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Python Tkinter Transparent Windows")
root.iconbitmap("Python Tkinter Transparent Windows/icons/target.ico")
root.geometry("550x550")


root.attributes("-alpha", 0.7)

my_label = Label(root, text="Hello World!", font=("Helvetca", 20))
my_label.pack(pady=20)

# Create Slide Function
def slide(X):
    root.attributes('-alpha', my_slider.get())
    slider_label.config(text=my_slider.get())
    

# Create a slider
my_slider = ttk.Scale(root, from_=0.1, to=1.0, value=0.7, orient=HORIZONTAL, command=slide)
my_slider.pack(pady=20)

# Create Slide
def slide(X):
    root.attributes('-alpha', my_slider.get())
    slide_label.config(text=str(round(my_slider.get(), 2)))

# Create Label
slider_label = Label(root, text="")
slider_label.pack(pady=20)

# Create a label
slide_label=Label(root, text="")
slide_label.pack(pady=10)

# Make 1nd windows solid when clicked
def make_solid(E):
    new.attributes("-alpha", 1.0)


# Open new Windows
def new_windown():
    global new
    new = Toplevel()
    new.attributes("-alpha", 0.5)
    new.bind("<Button-1>", make_solid)


# Create new windows but button
new_window = Button(root, text="New Windows", command=new_windown)
new_window.pack(pady=12)




root.mainloop()