#######################################################################
# Python Tkinter Color Changing Number Guessing Game
# Python Tkinter Juego de adivinanzas de números que cambian de color
########################################################################

from tkinter import *
from random import randint

root = Tk()
root.title('Python Tkinter Color Changing Number Guessing Game')
root.iconbitmap('Python Tkinter Color Changing Number Guessing Game/icons/hipopotamo.png')
root.geometry("500x500")

num_label = Label(root, text="Pick A Number\nBetwen 1 and 10!", font=("Bush Script MT", 32))
num_label.pack(pady=20)

def guesser():
    pass

def rando():
    pass


guess_box = Entry(root, font=("Helvetica", 100), width=2)
guess_box.pack(pady=20)

guess_button = Button(root, text="Submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text="New Number", command=rando)
rand_button.pack(pady=20)

root.mainloop()