# Python Tkinter Random Winner Generador
# Generador de ganador aleatorio de Python Tkinter

from tkinter import *
from random import randint

root = Tk()
root.title('Python Tkinter Random Winner Generador!')
root.iconbitmap('Python Tkinter Random Winner Generador/umbrella.ico')
root.geometry("400x600") 

def pick():

    # 6 Entries
    entries = ['Sanbid Ray chowdhurry ', 'The Refuge Malik', 'Google India', 'DotDotCom', 'jon Label', 'Brian Marquez']
    
    # Convert to a set
    entries_set = set(entries)
    # Convert back to list
    unique_entries = list(entries_set)

    #create our list size variable
    our_number = len(unique_entries) -1

    # create a random number between 0 and 5
    rando = randint(0, our_number)

    winnerLabel = Label(root, text=(unique_entries[rando]), font=("Helvetica", 18))
    winnerLabel.pack(pady=50)


topLabel = Label(root, text="Win-0-Rama!", font=("Helvetica", 24))
topLabel.pack(pady=28)

winButoon = Button(root, text="PICK OUR WINNER", font=("Helvetica", 24), command=pick)
winButoon.pack(pady=20)

root.mainloop()