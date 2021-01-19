#############################################################
#  Python Tkinter Basic Search and Autofill
#############################################################

from tkinter import *


root = Tk()
root.title("Python Tkinter Basic Search and Autofill")
root.iconbitmap("Python Tkinter Basic Search and Autofill/icons/fire.ico")
root.geometry('500x300')

# Update
def update(data):
    #clear tje listbox
    my_list.delete(0, END)

    # ADD TOPPING TO LISTBOX
    for item in data:
        my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
    # DELETE WHATEVER IS IN THE ENTRY BOX
    my_entry.delete(0, END)

    #add clicked list item to entry box
    my_entry.insert(0, my_list.get(ACTIVE))

# create function to check entry vs listbox
def check(e):
    #grab what was typed
    typed = my_entry.get()

    if typed =='':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)

    # update our listbox with selected items
    update(data)


# Create Label
my_label = Label(root, text="Start Typing...",
    font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza topping
toppings = ["Peperoni", "Peppers", "Mushrooms", "Chesse", "Onions", "Ham", "Taco"]

# Add the topping to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

#CREATE A BINDING ON THE ENTRY BOX
my_entry.bind("<KeyRelease>", check)





root.mainloop()