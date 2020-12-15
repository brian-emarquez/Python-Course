##########################################################
# Python Tkinter Dependent Drop Downs and List Boxes
# Cuadros de lista y desplegables dependientes de Python Tkinter
##########################################################

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Dependent Drop Downs and List Boxes')
root.iconbitmap('Python Tkinter Dependent Drop Downs and List Boxes/icons/arrow.ico')
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



root.mainloop()