#############################################################
#  Python Tkinter Basic Search and Autofill
#############################################################

from tkinter import *


root = Tk()
root.title("Python Tkinter Basic Search and Autofill")
root.iconbitmap("Python Tkinter Basic Search and Autofill/icons/fire.ico")
root.geometry('500x300')

# Create Label
my_label = Label(root, text="Start Typing...",
    font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

root.mainloop()