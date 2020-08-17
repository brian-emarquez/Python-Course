# Python Tkinter Delete A Records our Database
# Python Tkinter Delete A Records nuestra base de datos

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Python Tkinter Delete a Record')
root.iconbitmap('Python Tkinter Delete a Record/db.ico')
root.geometry("380x550") 

# Databases
# Create a database or connect to one
conn = sqlite3.connect('Python Tkinter Delete a Record/address_book.db')

# create cursor
c = conn.cursor()

# Create Tables
'''c. execute("""CREATE TABLE adreesses (
            f_name text, 
            l_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")
'''
# Create Function to delete a Record
def delete():
    # create a database or conect to one
    conn = sqlite3.connect('Python Tkinter Delete a Record/address_book.db')
    c = conn.cursor()

    #query the database
    c.execute("DELETE from adreesses WHERE oid = " + delete_box.get())
    
    delete_box.delete(0, END)

    conn.commit()
    conn.close()

# Create submit Function For database
def submit():

    conn = sqlite3.connect('Python Tkinter Delete a Record/address_book.db')
    
    c = conn.cursor()
    
    c.execute("INSERT INTO adreesses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",

        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })
    
    conn.commit()
    conn.close()

    # clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Create Query Function

def query():
    conn = sqlite3.connect('Python Tkinter Delete a Record/address_book.db')
    c = conn.cursor()

    #query the databaseç
    c.execute("SELECT * , oid FROM adreesses ")
    records = c.fetchall()  # fetchone, fetchmany(45)
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box labels
f_name_label = Label(root, text="First Nane")
f_name_label.grid(row=0, column=0, pady=(10, 0))

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

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0, pady=5)


#Create submit button
submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create A Delete Button

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Commit changes
conn.commit()

# Close connection
conn.close()
root.mainloop()