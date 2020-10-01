# Python Tkinter Tic Tac Toe Game

from tkinter import *
from tkinter import messagebox


root = Tk()

root.title('Python Tkinter Tic Tac Toe Game')
root.iconbitmap('Python Tkinter Tic Tac Toe Game/Icons/tic-tac-toe.ico')
#root.geometry("500x400")

def  b_cick(b):
    pass


# Build our Buttons
b1 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b1))
b2 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b2))
b3 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b3))

b4 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b4))
b5 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b5))
b6 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b6))

b7 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b7))
b8 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b8))
b9 = Button(root, text="", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_cick(b9))

# Grid our buttons to the screen
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)











root.mainloop()
