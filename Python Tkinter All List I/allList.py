##########################################################
#  Python Tkinter All List I
##########################################################

from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Python Tkinter All List I")
root.iconbitmap("Python Tkinter All List I/icons/drink.ico")
root.geometry('500x350')

# Define our Font
my_font = Font(
    family="Brush  Script MT Cursiva",
    size =30,
    weight="bold") 

my_frame = Frame(root)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",

)

my_list.pack()

# Create dummy list
stuff = ["Walk the Dog", "Buy Griceries", "Take a Nap", "Learn Tkinter", "Rule the wold"]

# add dummy list to list box
for item in stuff:
    my_list.insert(END, item)






root.mainloop()