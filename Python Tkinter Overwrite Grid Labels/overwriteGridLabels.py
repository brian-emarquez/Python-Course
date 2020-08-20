# Python Tkinter Overwrite Grid Labels
# Python Tkinter sobrescribe etiquetas de cuadrícula

from tkinter import *

root = Tk()
root.title('Python Tkinter Overwrite Grid Labels!')
root.iconbitmap('Python Tkinter Overwrite Grid Labels/pc.ico')
root.geometry("400x400") 

myLabel = Label(root)

'''def myDelete():
    
    myLabel.grid_forget()
    #myLabel.destroy()
    myButton['state'] = NORMAL # habilitar button
    #print(myButton.winfo_exists())
'''

def myClick():

    global myLabel
    myLabel.destroy()

    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    #myButton['state'] = DISABLED # Desabilitar Button

e = Entry(root, width=17 , font=('Helvetica', 30))
e.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root, text="Enter Your name", command=myClick)
myButton.grid(row=1, column=0, pady=10)

#DeleteButton = Button(root, text="Delete Text", command=myDelete)
#DeleteButton.grid(row=2, column=0, pady=10)

root.mainloop()