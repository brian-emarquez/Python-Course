# Python Tkinter Read and Write to Text Files
# Python Tkinter leer y escribir en archivos de texto

from tkinter import *

root = Tk()

root.title('Python Tkinter Read and Write to Text Files')
root.iconbitmap('Python Tkinter Text-Box/panda.ico')
root.geometry("600x600")

# Read Only r
# read and write r+ (beginning of file)
# Write Only w (over-Written)
# Write and Read w+ (over written)
# Append Only a (end of file)
# Append and Read a+ (end of file)

def open_txt():
    text_file = open("Python Tkinter Read and Write to Text Files/sample.txt", "r")
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

my_text = Text(root, width=60, height=20, font=("Helvetica", 16))
my_text.pack(pady=20)

open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

root.mainloop()
