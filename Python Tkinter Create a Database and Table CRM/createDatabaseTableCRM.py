# Python Tkinter Create a Database and Table CRM
# 

from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

root = Tk()
root.title('Python Tkinter Create a Database and Table CRM')
root.iconbitmap('Python Tkinter Create a Database and Table CRM/check.ico')
root.geometry("400x200") 

#Connect to MYSQL
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port = 3308,
    user="briandb",
    password="briandb"
)

#Chack to see if connection to MYSQL was created
# print(mydb)

#create a cursor and initialize it
my_cursor = mydb.cursor()

# Create Database
my_cursor.execute("SHOW DATABASES")

root.mainloop()