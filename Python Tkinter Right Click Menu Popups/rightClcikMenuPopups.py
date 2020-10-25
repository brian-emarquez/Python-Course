# Python Tkinter Right Click Menu Popups!
# ¡Ventanas emergentes del menú contextual de Python Tkinter!

from tkinter import *

root = Tk()
root.title('Python Tkinter Right Click Menu Popups!')
root.iconbitmap('Python Tkinter Right Click Menu Popups/icons/pay.ico')
root.geometry("500x550") 

my_label = Label(root, text="", font=("Helvetica", 20))
my_label.pack(pady=20)

def hello():
    my_label.config(text="Hello Tkinter")

def bye():
     my_label.config(text="Bye Tkinter")

def my_popup(e):
    my_menu.tk_popup(e.x_root, e.y_root)

# Create a Menu
my_menu = Menu(root, tearoff=False)
my_menu.add_command(label="Say Hello", command=hello)
my_menu.add_command(label="Say Goodbye", command=bye)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)

root.bind("<Button-3>", my_popup)

root.mainloop()