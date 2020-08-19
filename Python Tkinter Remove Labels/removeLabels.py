# Python Tkinter Remove Labels
# Python Tkinter Eliminar etiquetas

from tkinter import *

root = Tk()
root.title('Python Tkinter How To Risize Entry Box height!')
root.iconbitmap('Python Tkinter How To Risize Entry Box height/umbrella.ico')
root.geometry("400x600") 


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)

e = Entry(root, width=50 , font=('Helvetica', 14))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your name", command=myClick)
myButton.pack(pady=10)

root.mainloop()