##############################################################
# Python Tkinter How To Animate Widgets
#############################################################

from tkinter import *

root = Tk()
root.title("Python Tkinter How To Animate Widgets")
root.iconbitmap("Python Tkinter How To Animate Widgets/icons/hulk.ico")
root.geometry("500x400")

# define some variables
count=0
size=26
#pos=100

# Contract the button
def contract():
    global count, size, pos
    if count <=10 and count > 0:
        size -=2
        # Configure button font size
        my_button.config(font=("Helvetica",size)) 
        my_button.pack_configure()
        # decreaser
        count -=1
        #pos -=20
        # set a timer
        root.after(10, contract)
        
#Expand the button
def expand():
    global count, size, pos
    if count < 10:
        size +=2
        # Configure button font size
        my_button.config(font=("Helvetica",size)) 
        my_button.pack_configure()
        # Increaser
        count +=1
        #pos +=20
        # set the timer
        root.after(10, expand)

    elif count == 10:
        contract()

# Create a button
my_button = Button(root,
    text="Click!",
    command=expand,
    font=("Helvetica", 24),
    fg="blue")

my_button.pack(pady=100)
root.mainloop()