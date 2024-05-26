# Python Tkinter Create Tabs in Your GUI Interface Using Notebook
# Python Tkinter Cree pestañas en su interfaz GUI usando Notebook

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Create Tab in Your GUI')
root.iconbitmap('Python Tkinter Create Tab in Your GUI/api.ico')
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

def hide():
    my_notebook.hide(1) #  Muestra el primner tab

def show():
    my_notebook.add(my_frame2, text="Red tab")

def select():
    my_notebook.select(1)


my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Blue Tab")
my_notebook.add(my_frame2, text="Red Tab")

# Hide a tab
my_button1 = Button(my_frame1, text="Hide Tab 2", command=hide).pack(pady=15)

# show a tab
my_button2 = Button(my_frame1, text="Show Tab 2", command=show).pack(pady=15)

# Navidate to a tab
my_button3 = Button(my_frame1, text="Navigate", command=select).pack(pady=10)


root.mainloop()


