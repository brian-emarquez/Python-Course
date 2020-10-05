# Python Tkinter Treeview II Add and Remove Records
# Vista de árbol de Python Tkinter

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Treeview II add Remove Records')
root.iconbitmap('Python Tkinter Treeview II add Remove Records/Icons/cocoa.ico')
root.geometry("500x600") 

my_tree = ttk.Treeview(root)

# Define Our Columns
my_tree["columns"] = ("Name", "ID", "Favorite Pizza")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Favorite Pizza", anchor=CENTER, width=140)
 
# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)


# Add Data
data = [

    ["John", 1, "Pepperoni"],
    ["Mary", 2, "Cheese"],
    ["Tim", 3, "Mushroom"],
    ["Erin", 4, "Ham"],
    ["Bob", 5, "Orion"]
]

count = 0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2] ))
    count +=1

'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("Jhon", 1, "Peperroni"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", "2", "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Tina", "3", "Ham"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Bob", "4", "Supreme"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Erin", "5", "Cheese"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Wes", "6", "Onion"))
'''
#add child
#my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
#my_tree.move("6", "0", "0")

# Pack to the screen
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

# Labels
n1 = Label(add_frame, text = "Name")
n1.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=1)

tl = Label(add_frame, text="Topping")
tl.grid(row=0, column=2)

# Entry Boxes
name_box = Entry(add_frame)
name_box.grid(row=1, column=0)

id_box = Entry(add_frame)
id_box.grid(row=1, column=1)

topping_box = Entry(add_frame)
topping_box.grid(row=1, column=2)

# Add Records
def add_records():
    global count
    
    my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()))
    count +=1

    # Clear the boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

# Buttons
add_rercord = Button(root, text="Add Record",command=add_records)
add_rercord.pack(pady=20)
root.mainloop()