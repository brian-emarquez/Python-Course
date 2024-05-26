# HowToResizeYourAppWithTheSizegrip Widget
# Cómo cambiar el tamaño de su aplicación con el widget de agarre de tamaño

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('HowToResizeYourAppWithTheSizegripWidget')
root.iconbitmap('Python Tkinter How To Resize Your App With The Sizegrip Widget/icons/document.ico')
root.geometry("400x300")

# Make the app resizeable
root.resizable(True, True)

my_frame2 = Frame(root, highlightbackground="gray",  highlightthickness=1)
my_frame2.pack(pady=20)

my_label = Label(my_frame2, text="Hello World!",
    font=("Helvetica", 32))
my_label.pack(pady=20, padx=20)

# Reconfigure our rows and olumns for grid
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

# Create a frame
my_frame = Frame(root, highlightbackground="gray",  highlightthickness=1)
my_frame.pack(side="bottom", fill=X)

# Create sizegrip
my_sizegrip = ttk.Sizegrip(root)
my_sizegrip.pack(side="right", anchor=SE)

#my_sizegrip.grid(row=1, sticky=SE)


root.mainloop()
