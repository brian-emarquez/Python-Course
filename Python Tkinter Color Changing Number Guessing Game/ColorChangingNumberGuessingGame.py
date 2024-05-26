#######################################################################
# Python Tkinter Color Changing Number Guessing Game
# Python Tkinter Juego de adivinanzas de números que cambian de color
########################################################################

from tkinter import *
from random import randint

root = Tk()
root.title('Python Tkinter Color Changing Number Guessing Game')
root.iconbitmap('Python Tkinter Color Changing Number Guessing Game/icons/color.ico')
root.geometry("500x500")

num_label = Label(root, text="Pick A Number\nBetwen 1 and 10!", font=("Brush Script MT", 32))
num_label.pack(pady=20)

def guesser():
    if guess_box.get().isdigit():
        # Reset our label
        num_label.config(text="Pick A Number\nBetwen 1 and 10!")
        # find
        #ABS devuelve el valor apsoluto
        dif = abs(num - int(guess_box.get()))

        # check to see if correct

        if int (guess_box.get()) == num:
            bc = "SystemButtonFace"
            num_label.config(text="Correct")
        elif dif == 5:
            # set background color to white
            bc = "white"
        elif dif < 5:
            bc = f'#ff{dif}{dif}{dif}{dif}'
        else:
            bc = f'#{dif}{dif}{dif}{dif}ff'

        # Change the cackground
        root.config(bg=bc)

        #change bg label
        num_label.config(bg=bc)

    else:
        # Delete entry and throw wror message
        guess_box.delete(0, END)
        num_label.config(text="Hey! Thet's Not A number")

def rando():
    global num
    num = randint(1, 10)
    #clear the guess box
    guess_box.delete(0, END)
    # Change the colors back to normal
    num_label.config(bg=" ")
    root.config(bg="SystemButtonFace")




guess_box = Entry(root, font=("Helvetica", 100), width=2)
guess_box.pack(pady=20)

guess_button = Button(root, text="Submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text="New Number", command=rando)
rand_button.pack(pady=20)

# Genrate a random numer on state
rando()
root.mainloop()