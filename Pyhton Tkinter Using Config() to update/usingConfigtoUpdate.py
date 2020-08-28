# Python Tkinter Using.config() to update Widgets
# 

from tkinter import *

root = Tk()
root.title('Pyhton Tkinter Using Config() to update')
root.iconbitmap('Pyhton Tkinter Using Config() to update/avatar.ico')
root.geometry("400x600")


def something():
    my_label.config(text="This is new Text", font=("Helvetica", 8))
    root.config(bg="blue")
    my_button.config(text="You've been configged", state=DISABLED, pady=30)

global my_label
my_label = Label (root, text="This is my Text", font=("helvetica", 17))
my_label.pack(pady=10)

global my_button
my_button = Button(root, text="Click Me", command=something)
my_button.pack(pady=10)

root.mainloop()
