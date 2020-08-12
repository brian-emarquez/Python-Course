# Python Tkinter MariaDB

from tkinter import *
from PIL import ImageTk, Image
#import mysql.connector
import mariadb
import sys

root = Tk()
root.title('Python Tkinter MariaDB')
root.iconbitmap('Python Tkinter MariaDB/check.ico')
root.geometry("400x200") 

mariadb_conexion = mariadb.connect(
    host='127.0.0.1',
    port=3307, 
    user='briandb', 
    password='briandb'
    #tabase='test2'
)

print(mariadb_conexion)
root.mainloop()



