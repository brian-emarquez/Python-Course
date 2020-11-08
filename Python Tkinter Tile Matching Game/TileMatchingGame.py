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

#print(matches)

#Create button Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Functions 
def something():
    pass

#Define out buttons
b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=something)

#Grid out Buttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)






root.mainloop()