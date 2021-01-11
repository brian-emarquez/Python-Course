######################################################################
# Python TKinter Button Bitmaps
###################################################################### 

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python TKinter Button Bitmaps')
root.iconbitmap('Python TKinter Button Bitmaps/icons/elvis.ico')
root.geometry("300x900")

'''
error
gray75
gray50
gray12
hourglass
info
questhead
question
warning
'''
# Un solo bitmap
#my_button = Button(root, bitmap="error", width=50, height=50)
#my_button.pack(pady=50)

list = ["error",
"gray75",
"gray50",
"gray12",
"hourglass",
"info",
"questhead",
"question",
"warning"]


for map in list:
    Button(root, bitmap=map, width=50, height=50, fg="darkblue").pack(pady=20)





root.mainloop()