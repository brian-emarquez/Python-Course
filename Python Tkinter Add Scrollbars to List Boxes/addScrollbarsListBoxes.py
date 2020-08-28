# Python Tkinter Add Scrollbars to List Boxes
# Python Tkinter agrega barras de desplazamiento a cuadros de lista

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python Tkinter Add Scrollbars to List Boxes')
root.iconbitmap('Python Tkinter Add Scrollbars to List Boxess/avatar.ico')
root.geometry("400x400")

# List Box

my_listbox = Listbox(root)
my_listbox.pack(pady=15)


# add item to listbox
my_listbox.insert(END, "This is an item")
my_listbox.insert(END, "Second Item")

# Add list of items
my_list = ["One", "Two", "Three"]

for item in my_list:
    my_listbox.insert(END, item)

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='')

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

my_button = Button(root, text="Delete", command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text="Select", command=select)
my_button2.pack(pady=10)

global my_label
my_label = Label(root, text="", )
my_label.pack(pady=5)

root.mainloop()
