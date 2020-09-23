# Python Tkinter spinboxes

from tkinter import *

root = Tk()

root.title('Learn To Code at Python Python Tkinter Spinboxes')
root.iconbitmap('Python Tkinter Spinboxes/panda.ico')
root.geometry("500x400")

def grab():
    my_label.configure(text=my_spin.get())

names = ("Brian", "Maria", "Jack")
#my_spin = Spinbox(root, from_=0, to=10, increment = 2, font=("Helvetica", 20))
my_spin = Spinbox(root, from_=0, values=names, to=10, font=("Helvetica", 20))
my_spin.pack(pady=20)

my_button = Button(root, text="Submit", command=grab)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
