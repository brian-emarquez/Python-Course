# Python Tkinter Create CRM database Tool
# 

from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

root = Tk()
root.title('Python Tkinter Create CRM database Tool')
root.iconbitmap('Python Tkinter Create CRM database Tool/check.ico')
root.geometry("400x200") 

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port = 3308,
  user="briandb",
  password="briandb"
)

print(mydb)

root.mainloop()