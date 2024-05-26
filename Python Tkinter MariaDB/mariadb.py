# Python Tkinter MariaDB

from tkinter import *
from PIL import ImageTk, Image
#import mysql.connector
import mysql.connector as mariadb

import sys

root = Tk()
root.title('Python Tkinter MariaDB')
root.iconbitmap('Python Tkinter MariaDB/check.ico')
root.geometry("400x200") 

#mydb = mysql.connector.connect(
conn = mariadb.connect(
    host='127.0.0.1',
    port=3307, 
    user='briandb', 
    password='briandb'
)

print(conn)
conn.close()
root.mainloop()



