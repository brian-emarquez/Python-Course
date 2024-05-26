# Python Tkinter Unicode Character & Special Characters
# Caracteres especiales y caracteres Unicode de Python Tkinter

from tkinter import *

root = Tk()
root.title('Python Tkinter Unicode Character & Special Characters!')
root.iconbitmap('Python Tkinter Unicode Character & Special Characters/avatar.ico')
root.geometry("400x400")

my_label = Label(root, text='41' + u'\u00b0', font=("Helvetica", 32)).pack(pady=10)
my_button = Button(root, text=u'\u00AB', font=("Helvetica", 32)).pack(pady=10)
my_button1 = Button(root, text=u'\u00BB', font=("Helvetica", 32)).pack(pady=10)


root.mainloop()