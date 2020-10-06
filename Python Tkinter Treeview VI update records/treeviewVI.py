# Python Tkinter Treeview VI update records
# Vista de árbol de Python Tkinter

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Treeview VI update records')
root.iconbitmap('Python Tkinter Treeview VI update records/Icons/cocoa.ico')
root.geometry("500x600") 

# Add some style
style = ttk.Style()

# Pick a theme
style.theme_use("default")

# Configure our treeview colors
style.configure("Treeview",
    background="silver",
    foreground = "black",
    rowheight=25,
    fieldbackground="silver"
    )

# CHange selected color
style.map('Treeview', 
    background=[('selected', 'blue')])

# Create TreeView Frame
tree_frame = Frame(root)
tree_frame.pack(pady=20)

# TreeView Scroll
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create TreeView
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the scrollbar
tree_scroll.config(command=my_tree.yview)



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
    ["Bob", 5, "Orion"],
    ["Steve", 6, "Peppers"],
    ["Tina", 7, "Cheese"],
    ["Mark", 8, "Supreme"],
    ["Ruth", 9, "Vegan"],
    ["Tim", 3, "Mushroom"],
    ["Erin", 4, "Ham"],
    ["Bob", 5, "Orion"],
    ["Steve", 6, "Peppers"],
    ["Tina", 7, "Cheese"],
    ["Mark", 8, "Supreme"],
    ["Ruth", 9, "Vegan"],
    ["Tim", 3, "Mushroom"],
    ["Erin", 4, "Ham"],
    ["Bob", 5, "Orion"],
    ["Steve", 6, "Peppers"],
    ["Tina", 7, "Cheese"],
    ["Mark", 8, "Supreme"],
    ["Ruth", 9, "Vegan"]
]

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0

for record in data:
    if count % 2 == 0:

        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
    else:

        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))

    count +=1

'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("Jhon", 1, "Peperroni"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", "2", "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Tina", "3", "Ham"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Bob", "4", "Supreme"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Erin", "5", "Cheese"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Wes", "6", "Onion"))
'''

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

    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    global count
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()),  tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(name_box.get(), id_box.get(), topping_box.get()),  tags=('oddrow',))

    count +=1

    # Clear the boxes
    name_box.delete(0, END)
    id_box.delete(0, END)
    topping_box.delete(0, END)

# Remove all Recods
def remove_all():

    for record in my_tree.get_children():
        my_tree.delete(record)
        
# Remone One selected
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# Remove many selected
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)




# Buttons
add_rercord = Button(root, text="Add Record",command=add_records)
add_rercord.pack(pady=20)

# Remove All
remove_All = Button(root, text="Remove All",command=remove_all)
remove_All.pack(pady=10)

# Remove One
remove_one = Button(root, text="Remove One Selected", command=remove_one)
remove_one.pack(pady=10)

# Remove many Selected
remove_many = Button(root, text="Remove Many Selected", command=remove_many)
remove_many.pack(pady=10)


root.mainloop()