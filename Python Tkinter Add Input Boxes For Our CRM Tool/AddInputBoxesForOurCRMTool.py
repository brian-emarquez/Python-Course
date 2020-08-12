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
    port = 3308,
    user="briandb",
    password="briandb"
    #database = "crm",
)

#Chack to see if connection to MYSQL was created
# print(mydb)

#create a cursor and initialize it
my_cursor = mydb.cursor()

# Create Database
#my_cursor.execute("CREATE DATABASE crm")

#Test to seee if database was created 
#my_cursor.execute("SHOW DATABASES")
#print(my_cursor)
#for db in my_cursor:
#    print(db)

# Create Table
#my_cursor.execute("CREATE TABLE customers (first_name VARCHAR(255), last_name VARCHAR(255), zipcade INT(10), price_paid DECIMAL(10, 2), user_id INT AUTO_INCREMENT PRIMARY KEY)")

my_cursor.execute("SELECT * FROM customers")
print(my_cursor.description)

for thing in my_cursor.description:
    print(thing)

root.mainloop()