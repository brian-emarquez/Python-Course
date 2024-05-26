#  Python Tkinter How to Reset a Spinbox with Tkinter
#  Python Tkinter Cómo restablecer un Spinbox con Tkinter

from tkinter import *

root = Tk()
root.title("Python Tkinter How to Reset a Spinbox with Tkinter")
root.iconbitmap("Python Tkinter How to Reset a Spinbox with Tkinter/icons/h.ico")
root.geometry('500x350')

def reset():
    var = IntVar(root)
    var.set(0)
    my_spin.config(textvariable=var)

# set intvar
var = IntVar(root)
var.set(20)

# set stringvar
var2 = StringVar(root)
var2.set("john")

my_spin = Spinbox(root, 
    from_=0, to=100,
    font=("helvetica", 20),
    textvariable=var)

my_spin.pack(pady=20)

my_button = Button(root, text="reset spinner", command=reset)
my_button.pack(pady=20)

root.mainloop()