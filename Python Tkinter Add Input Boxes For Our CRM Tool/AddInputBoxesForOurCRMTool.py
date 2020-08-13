# Python Tkinter Add Input Boxes For Our CRM Tool

from tkinter import *
from PIL import ImageTk, Image
#import mysql.connector
import mysql.connector as mariadb

root = Tk()
root.title('Python Tkinter Add Input Boxes For Our CRM Tool')
root.iconbitmap('Python Tkinter Add Input Boxes For Our CRM Tool/check.ico')
root.geometry("400x200") 

mydb = mariadb.connect(
#mydb = mysql.connector.connect(
    host="127.0.0.1",
    port = 3307,
    user="briandb",
    password="briandb",
    database = "cmd"
)

#Check to see if connection to MYSQL was created
print(mydb)

#create a cursor and initialize it
my_cursor = mydb.cursor()

# Create Database
#my_cursor.execute("CREATE DATABASE cmd")

#Test to seee if database was created 
#my_cursor.execute("SHOW DATABASES")
#print(my_cursor)
#for db in my_cursor:
#    print(db)

#Drop Table
#my_cursor.execute("DROP TABLE customers")

# Create Table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255),\
    last_name VARCHAR(255), \
    zipcade INT(10), \
    price_paid DECIMAL(10, 2),\
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

# Alter Table
#my_cursor.execute("ALTER TABLE customers ADD (\
#    email VARCHAR(255),\
#    address_1 VARCHAR(255), \
#    address_2  VARCHAR(255), \
#    city VARCHAR(50),\
#    state VARCHAR(50),\
#    country VARCHAR(255),\
#    phone VARCHAR(255),\
#    payment_method VARCHAR(255),\
#    dicount_code VARCHAR(255))")

# Show table
#my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)

#for thing in my_cursor.description:
#    print(thing)

#create label
title_label = Label (root, text="MariaDb customer database", font=("helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady="10")

# create Main to Enter customer Data



root.mainloop()
