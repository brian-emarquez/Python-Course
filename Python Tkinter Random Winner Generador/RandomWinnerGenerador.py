# Python Tkinter Random Winner Generador
# Generador de ganador aleatorio de Python Tkinter

from tkinter import *

root = Tk()
root.title('Python Tkinter Random Winner Generador!')
root.iconbitmap('Python Tkinter Random Winner Generador/umbrella.ico')
root.geometry("400x600") 

entries = ['Sanbid Ray ', 'The Refuge Malik', 'Google India', 'DotDotCom', 'jon Label']

def pick():
    return

topLabel = Label(root, text="Win-0-Rama!", font=("Helvetica", 24))
topLabel.pack(pady=28)

winButoon = Button(root, text="PICK OUR WINNER", font=("Helvetica", 24), command=pick)
winButoon.pack(pady=20)

root.mainloop()