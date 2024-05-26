# Python Tkinter Using Databases

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learn to Tkinter')
root.iconbitmap('Python Tkinter Using Databases/db.ico')
root.geometry("400x400") 

# Databases
# Create a database or connect to one
conn = sqlite3.connect('Python Tkinter Using Databases/address_book.db')

# create cursor
c = conn.cursor()

# Create Tables
c. execute("""CREATE TABLE adreesses (
            first_name text, 
            last_name text,
            address text,
            city text,
            zipcode integer
            )""")

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()