# Python Tkinter How to Open External Programns
# Python Tkinter Cómo abrir programas externos

from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title('Python Tkinter How to Open External Programns')
root.iconbitmap('Python Tkinter How to Open External Programns/pineapple.ico')
root.geometry("600x600") 

def open_programa():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    # Open the program
    os.system('"%s"' % my_program)

def open_notepad():
    notepad = 'c:/Windows/system32/notepad.exe'
    os.system('"%s"' % notepad) # Open Notepad

my_button = Button(root, text="Open Program", command=open_programa)
my_button.pack(pady=20)

my_button2 = Button(root, text="Open Notepadd", command=open_notepad)
my_button2.pack(pady=25)


my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()