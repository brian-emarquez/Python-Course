# Python Tkinter building Out


# Python Tkinter Using Databases

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learn to Tkinter')
root.iconbitmap('Python Tkinter Building Out/db.ico')
root.geometry("400x400") 

# Databases
# Create a database or connect to one
conn = sqlite3.connect('Python Tkinter Building Out/address_book.db')

# create cursor
c = conn.cursor()

# Create Tables
'''c. execute("""CREATE TABLE adreesses (
            first_name text, 
            last_name text,
            address text,
            city text,
            zipcode integer
            )""")
'''
# Create submit Function For database
def submit():

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Tsext Box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create text box labels

f_name_label = Label(root, text="First Nane")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)


#Create submit button
submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()