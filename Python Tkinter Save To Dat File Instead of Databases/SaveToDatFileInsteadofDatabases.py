##########################################################
# Python Tkinter Save To Dat File Instead of Databases
# Guardar en archivo Dat en lugar de bases de datos
##########################################################

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Save To Dat File Instead of Databases')
root.iconbitmap('Python Tkinter Save To Dat File Instead of Databases/icons/arrow.ico')
root.geometry("500x500")

# Creatinf a list of sizes
sizes = [
    "Small",
    "Medium",
    "Large"
]

# Create a lsit of colors
small_colors = [
    "Red",
    "Green",
    "Blue",
    "Black"
]
medium_colors = [
    "Red",
    "Green"]

large_colors = [
    "Blue",
    "Black"]

# show small_colors
def pick_color(e):
    if my_combo.get() == "Small":
        color_combo.config(value=small_colors)
        color_combo.current(0)

    if my_combo.get() == "Medium":
        color_combo.config(value=medium_colors)
        color_combo.current(0)

    if my_combo.get() == "Large":
        color_combo.config(value=large_colors)
        color_combo.current(0)

# Create a drop Box
my_combo = ttk.Combobox(root, value=sizes)
my_combo.current(0)
my_combo.pack(pady=20)

# bind the conbobox
my_combo.bind("<<ComboboxSelected>>", pick_color)

# Color combo box
color_combo = ttk.Combobox(root, value=[" "])
color_combo.current(0)
color_combo.pack(pady=20)

# List Boxes
my_frame = Frame(root)
my_frame.pack(pady=50)

# List boxes
my_list1 = Listbox(my_frame)
my_list2 = Listbox(my_frame)
my_list1.grid(row=0, column=0)
my_list2.grid(row=0, column=1, padx=20)

def list_color(e):
    my_list2.delete(0, END)

    if my_list1.get(ANCHOR) == "Small":
        for item in small_colors:
            my_list2.insert(END, item)

    if my_list1.get(ANCHOR) == "Medium":
        for item in medium_colors:
            my_list2.insert(END, item)

    if my_list1.get(ANCHOR) == "Large":
        for item in large_colors:
            my_list2.insert(END, item)

#add items to list1
for item in sizes:
    my_list1.insert(END, item)

# Bind the Listbox
my_list1.bind("<<ListboxSelect>>", list_color)

root.mainloop()