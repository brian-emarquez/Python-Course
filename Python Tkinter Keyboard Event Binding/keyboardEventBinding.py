# Python Tkinter Keyboard Event Binding

from tkinter import *

root = Tk()
root.title('Python Tkinter Keyboard Event Binding!')
root.iconbitmap('Python Tkinter Keyboard Event Binding/classes.ico')
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