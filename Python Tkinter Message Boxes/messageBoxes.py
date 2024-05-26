# Pyhton Tkinter Message Boxes

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn to Python')
root.iconbitmap('Python Tkinter Message Boxes/icon.ico')

#=====Tabla======#
# showinfo       #
# showwarning    #
# showerror      #
# askquestion    #
# askokcancel    #
# askyesno       #
#================#

def popup():
    response = messagebox.askokcancel("this is my Popup!", "Hello world") #
    Label(root, text=response).pack()

    if response==1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()

Button(root, text="Popup", command=popup).pack()
root.mainloop()
