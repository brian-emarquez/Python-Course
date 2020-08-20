# Python Tkinter Remove Labels
# Borrar el texto

from tkinter import *

root = Tk()
root.title('Python Tkinter Remove Labels!')
root.iconbitmap('Python Tkinter Remove Labels/pc.ico')
root.geometry("400x600") 


def myDelete():
    if myLabel.winfo_exists() ==1:
        myLabel.destroy()
    else:
        myLabel.destroy()

    #myLabel.pack_forget()
    myLabel.destroy()
    myButton['state'] = NORMAL # habilitar button
    print(myButton.winfo_exists())

def myClick():

    global myLabel
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)
    myButton['state'] = DISABLED # Desabilitar Button

e = Entry(root, width=50 , font=('Helvetica', 14))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your name", command=myClick)
myButton.pack(pady=10)

DeleteButton = Button(root, text='Delete Text', command=myDelete)
DeleteButton.pack(pady=10)

root.mainloop()