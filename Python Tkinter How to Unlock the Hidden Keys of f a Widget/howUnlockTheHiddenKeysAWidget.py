# Python Tkinter How to Unlock the Hidden Keys of f a Widget
# Python Tkinter Cómo desbloquear las claves ocultas de un widget

from tkinter import *

root = Tk()
root.title("Python Tkinter How to Unlock the Hidden Keys of f a Widget")
root.iconbitmap("Python Tkinter How to Unlock the Hidden Keys of f a Widget/icons/target.ico")
root.geometry("550x550")

my_label = Label(root, text="My Label", font=("Helvetica", 15))
my_label.pack(pady=20)

my_entry = Entry(root)
my_entry.pack(pady=20)

#for key in my_label.keys():
for key in my_entry.keys():
    print (key)

print(my_label.keys())

print(my_label['text'])


root.mainloop()