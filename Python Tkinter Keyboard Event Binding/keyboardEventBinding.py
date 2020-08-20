# Python Tkinter Keyboard Event Binding
# Enlace de eventos de teclado Python Tkinter

from tkinter import *

root = Tk()
root.title('Python Tkinter Keyboard Event Binding!')
#root.iconbitmap('Python Tkinter Keyboard Event Binding/classes.ico')
root.geometry("400x400") 

def clicker(event):
    #myLabel = Label(root, text="You clicked a button" + str(event.x) + " " + str(event.y))
    myLabel = Label(root, text="You clicked a button")
    myLabel.pack()

MyButton = Button(root, text="Click Me")
MyButton.bind("<Key>", clicker)
#MyButton.bind("<Leave>", clicker)  # boton sencible a mouse
#MyButton.bind("<Button-3>", clicker) # posicion de boton de mouse y evento de click

MyButton.pack(pady=20)

root.mainloop()