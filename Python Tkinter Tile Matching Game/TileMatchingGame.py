# Python Tkinter Tile Matching Game
# Juego de combinación de mosaicos Python Tkinter

from tkinter import *
import random

root = Tk()
root.title('Python Tkinter Tile Matching Game')
root.iconbitmap('Python Tkinter Tile Matching Game/icons/icons.ico')
root.geometry("500x550") 

#create our matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6] 

# Shuffle our matches
random.shuffle(matches)

print(matches)

root.mainloop()