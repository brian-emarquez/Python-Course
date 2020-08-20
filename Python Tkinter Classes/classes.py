# Python Tkinter Classes

from tkinter import *

root = Tk()
root.title('Python Tkinter Classes!')
root.iconbitmap('Python Tkinter Classes/classes.ico')
root.geometry("400x400") 



class Brian:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Loook at you.. you clicked a button!")

e = Brian(root)



root.mainloop()