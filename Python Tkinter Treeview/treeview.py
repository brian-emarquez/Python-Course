# Python Tkinter Treeview
# Vista de árbol de Python Tkinter

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Treeview')
root.iconbitmap('Python Tkinter Treeview/Icons/cocoa.ico')
root.geometry("500x500") 

my_tree = ttk.Treeview(root)

# Define Our Columns
my_tree["columns"] = ("Name", "ID", "Favorite Pizza")

# Formate Our Columns
my_tree.column("#0", width=120, minwidth=25)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("Id", anchor=CENTER, width=80)
my_tree.column("Favorite Pizza", anchor=CENTER, width=120)

# Create Headings
my_tree.heading("#0", text="Label", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)






root.mainloop()