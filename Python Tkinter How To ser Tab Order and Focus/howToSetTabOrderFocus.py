# Python Tkinter How To ser Tab Order and Focus
# Python Tkinter Cómo ser el orden de tabulación y el enfoque

from tkinter import *

root = Tk()
root.title('Python Tkinter How To ser Tab Order and Focus!')
root.iconbitmap('Python Tkinter How To ser Tab Order and Focus/icons/black.ico')
root.geometry("500x550") 


# Create Some entry boxes

red = Entry(root, bg="red", font=("Helvetica", 20))
white = Entry(root, bg="white", font=("Helvetica", 20))
blue = Entry(root, bg="blue", font=("Helvetica", 20))

# Pack item
red.pack(pady=20)
white.pack(pady=20)
blue.pack(pady=20)

# Pick focus
white.focus() # posicion donde se empiesa a escribir

# Change Tab Order
def tab_order():
    blue.focus()
    widgets = [blue, white, red]
    for w in widgets:
        w.lift()


my_button =  Button(root, text= "Change Tab Order", command=tab_order)
my_button.pack(pady=20)

tab_order()


root.mainloop()