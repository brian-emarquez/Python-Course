# Python Tkinter Menu Bars
# Barras de menú de Pyhton Tkinter

from tkinter import *


root = Tk()
root.title('Python Tkinter Menu Bars!')
root.iconbitmap('Python Tkinter Menu Bars/menu.ico')
root.geometry("400x600") 

my_menu = Menu(root)
root.config(menu=my_menu)


def our_comand():
    my_label = Label(root, text="You Clicked A Dropdown Menu!").pack()

# create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New...", command=our_comand)
file_menu.add_separator() # Separador
file_menu.add_command(label="Exit", command=root.quit)

# create an edit menu item
edit_menu= Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_comand)
edit_menu.add_command(label="Copy", command=our_comand)

# create an Options menu item
options_menu= Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Find", command=our_comand)
options_menu.add_command(label="Find Next", command=our_comand)

root.mainloop()