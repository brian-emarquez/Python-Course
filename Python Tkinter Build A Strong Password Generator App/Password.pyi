# Build A Strong Password Generator App

from tkinter import *
from random import randint

root = Tk()
root.title('Build A Strong Password Generator App') # titulo
root.iconbitmap('Python Tkinter Build A Strong Password Generator App/icons/camel.ico')
root.geometry("500x300")

my_password = chr(randint(33,126))

# Generate random strong pass
def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ''
    
    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    # output password to thescrenn
    pw_entry.insert(0, my_password)

#Copy to clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

lf = LabelFrame(root, text="How Many Character?")
lf.pack(pady=20)

# Creat entry box to design number of character
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#Create entry box fir our returned password
pw_entry = Entry(root, text='', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20) 

# Create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# create our buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0,column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboad", command=clipper)
clip_button.grid(row=0,column=1, padx=10)

root.mainloop()