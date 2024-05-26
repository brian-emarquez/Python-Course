# Python Tkinter Dont Packon the same Line
# Python Tkinter no empaqueta en la misma línea


from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Python Tkinter Dont Packon the same Line')
root.iconbitmap('Python Tkinter Dont Packon the same Line/api.ico')
root.geometry("600x600")

def grab():
    my_label.config(text=my_box.get())


my_box = Entry(root, font=("Helvetica", 28))
my_box.pack(pady=20)

my_button = Button(root, text="Grab Text From Box", command=grab).pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()

