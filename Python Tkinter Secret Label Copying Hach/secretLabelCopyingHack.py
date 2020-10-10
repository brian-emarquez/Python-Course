# Python Tkinter Secret Label Copying Hack
# Copia de etiqueta secreta de Python Tkinter Hach

from tkinter import *

root = Tk()
root.title('Python Tkinter Secret Label Copying Hach')
root.iconbitmap('Python Tkinter Secret Label Copying Hach/icons/secret.ico')
root.geometry("500x350") 

# Create Label
my_label = Label(root, text="Text 1", font=("Helvetica", 20))
my_label.pack(pady=20)

# Create stringvar
#my_text = StringVar()
#my_text.set("This is Label 2")

# Creaste Entry Box
my_entry = Entry(root,
    font=("Helvetica", 20), 
    bd=0,
    width=10)
   # state="readonly")
    #textvariable=my_text)

my_entry.insert(0, "This is cool label 2")
my_entry.config(state="readonly")

my_entry.pack(pady=20)

root.mainloop()