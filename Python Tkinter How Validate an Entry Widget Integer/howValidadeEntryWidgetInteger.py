# Python Tkinter How Validate an Entry Widget Integer
# Python Tkinter Cómo validar un entero de widget de entrada

from tkinter import *

root = Tk()
root.title('Python Tkinter How Validate an Entry Widget Integer')
root.iconbitmap('Python Tkinter How Validate an Entry Widget Integer/api.ico')
root.geometry("400x400")

def number():
    try:
        int(my_box.get())
        answer.config(text="That is a number! Congrats!")
        
    except ValueError:
        answer.config(text="That is NOT number! Congrats!")


my_label = Label(root, text="Enter a Number")
my_label.pack(pady=20)

my_box = Entry(root)
my_box.pack(pady=10)

my_button = Button(root, text="Entre a Number", command=number)
my_button.pack(pady=5)

answer = Label(root, text="")
answer.pack(pady=5)


root.mainloop()


