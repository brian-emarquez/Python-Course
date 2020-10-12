# Python Tkinter How To Position Label Text
# Python Tkinter Cómo colocar el texto de la etiqueta

from tkinter import *

root = Tk()
root.title('Python Tkinter How To Position Label Text')
root.iconbitmap('Python Tkinter How To Position Label Text/icons/label.ico')
root.geometry("500x500") 

my_label1 = Label(root,
    text="Brian\nBrian Brian\nBrian Brian Brian",
    font=("Comic Sans", 18),
    bd=1, relief="sunken")
my_label1.pack(pady=20, ipady=10, ipadx=10)

my_label2 = Label(root,
    text="Brian\nBrian Brian\nBrian Brian Brian",
    font=("Comic Sans", 18),
    bd=1, relief="sunken",
    justify="left")
my_label2.pack(pady=20, ipady=10, ipadx=10)

my_label3 = Label(root,
    text="Brian\nBrian Brian\nBrian Brian Brian",
    font=("Comic Sans", 18),
    bd=1, relief="sunken",
    justify="right")
my_label3.pack(pady=20, ipady=10, ipadx=10)


root.mainloop()


