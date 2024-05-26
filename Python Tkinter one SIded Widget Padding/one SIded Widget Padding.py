
# Python Tkinter one SIded Widget Padding
# Relleno de widgets a una cara


from tkinter import *


root = Tk()
root.title('Python Tkinter one SIded Widget Padding')
root.iconbitmap('Python Tkinter one SIded Widget Padding/icons/among_us.ico')
root.geometry("500x550") 
root.config(bg="blue")

# Create Label
my_label = Label(root, text="Hello World!",
    bg="white",
    fg="black",
    font=("Helvetica", 20))

my_label.grid(row=0, column=0, pady=50, padx=(0,50))

# Create a second label
my_label2 = Label(root, text="Hello World 2!",
    bg="white",
    fg="black",
    font=("Helvetica", 20))

my_label2.grid(row=0, column=1)

root.mainloop()
