#-----------------------------------------------------------------------------------#
# Python Tkinter Rock Paper Scissors Game
# Python Tkinter Rock Paper Scissors Juego
#-----------------------------------------------------------------------------------#

from tkinter import *
from random import randint

root = Tk()
root.title('Python Tkinter Rock Paper Scissors Game')
root.iconbitmap('Python Tkinter Rock Paper Scissors Game/icons/joystick.ico')
root.geometry("500x600") 

# Change bg color to white
root.config(bg="white")

# Define our images
rock = PhotoImage(file='Python Tkinter Rock Paper Scissors Game/images/rock.png')
#oImage(file='Python Tkinter Rock Paper Scissors Game/images/paper.jpg')
scissors = PhotoImage(file='Python Tkinter Rock Paper Scissors Game/images/scissor.png')

# Add Images to a list
image_list = [root,  scissors]

# Pick random number between 0 and 2
pick_number = randint(0,2)

#throw uo an image when the program starts
image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=20)



root.mainloop()