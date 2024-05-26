#  Python tkinter How to Disable or Delete a Menu item
#  Python tkinter Cómo deshabilitar o eliminar un elemento del menú

from tkinter import *

root = Tk()
root.title("Python Tkinter How to Disable or Delete a Menu item")
root.iconbitmap("Python Tkinter How to Disable or Delete a Menu item/icons/cat_blacK.ico")
root.geometry('500x500')

def new():
    pass

def open():
    pass

# Disable the New Menue Item
def disable_new():
    file_menu.entryconfig("New", state="disabled")

# Enable the new Menu Item
def enable_new():
    file_menu.entryconfig("New", state="normal")

def delete_new():
    file_menu.delete("New")

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#ass menu Items
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Add dropdown items
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open)

disable_button = Button(root, text="Disable New", command=disable_new)
disable_button.pack(pady=50)

enable_button = Button(root, text="Enable New", command=enable_new)
enable_button.pack(pady=10)

delete_new_button = Button(root, text="Delete New", command=delete_new)
delete_new_button.pack(pady=10)

root.mainloop()