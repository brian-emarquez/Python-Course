# Python Tkinter Read and Write to Text Files
# Python Tkinter leer y escribir en archivos de texto

from tkinter import *
from tkinter import filedialog

root = Tk()

root.title('Python Tkinter Read and Write to Text Files')
root.iconbitmap('Python Tkinter Text-Box/panda.ico')
root.geometry("600x700")

# Read Only r
# read and write r+ (beginning of file)
# Write Only w (over-Written)
# Write and Read w+ (over written)
# Append Only a (end of file)
# Append and Read a+ (end of file)

def open_txt():
    text_file = filedialog.askopenfilename(initialdir="Python Tkinter Read and Write to Text Files/", title ="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, "r")
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

def save_txt():
    text_file = filedialog.askopenfilename(initialdir="Python Tkinter Read and Write to Text Files/", title ="Open Text File", filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, "w")
    text_file.write(my_text.get(1.0, END))


my_text = Text(root, width=60, height=20, font=("Helvetica", 16))
my_text.pack(pady=20)

open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

root.mainloop()
