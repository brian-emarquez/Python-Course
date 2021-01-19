##########################################
# Python Tkinter On-Off Button Switch
########################################## 

from tkinter import *


root = Tk()
root.title('Python Tkinter On-Off Button Switch')
root.iconbitmap('Python Tkinter On-Off Button Switch/icons/avatar.ico')
root.geometry("1100x500")

# Keep track of the button state on/off
global is_on
is_on = True



my_label = Label(root, 
    text="The Swich Is on!", 
    fg="green", 
    font=("Helvetica",32))
my_label.pack(pady=20)

# Define our swith function
def switch():
    global is_on

    # Determin is on off
    if is_on:
        on_button.config(image=off)
        is_on = False
    else:
        on_button.config(image=on)
        is_on = True
    
# Define our Imaages
on = PhotoImage(file="Python Tkinter On-Off Button Switch/images/on.png")
off = PhotoImage(file="Python Tkinter On-Off Button Switch/images/off.png")

# Create A button
on_button = Button(root, image=on, bd=0, command=switch)
on_button.pack(pady=50)

root.mainloop()
