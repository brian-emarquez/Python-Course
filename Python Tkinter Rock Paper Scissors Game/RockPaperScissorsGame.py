#-----------------------------------------------------------------------------------#
# Python Tkinter Rock Paper Scissors Game
# Python Tkinter Rock Paper Scissors Juego
#-----------------------------------------------------------------------------------#

from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title('Python Tkinter Rock Paper Scissors Game')
root.iconbitmap('Python Tkinter Rock Paper Scissors Game/icons/joystick.ico')
root.geometry("500x600") 

# Change bg color to white
root.config(bg="white")

# Define our images
rock = PhotoImage(file='Python Tkinter Rock Paper Scissors Game/images/rock.png')
paper = PhotoImage(file='Python Tkinter Rock Paper Scissors Game/images/paper.png')
scissors = PhotoImage(file='Python Tkinter Rock Paper Scissors Game/images/scissor.png')

# Add Images to a list
image_list = [rock, paper, scissors]

# Pick random number between 0 and 2
pick_number = randint(0,2)

#throw uo an image when the program starts
image_label = Label(root, image=image_list[pick_number], bd=0 )
image_label.pack(pady=20)

# Create Spin Function
def spin():
    # Pick random number
    pick_number = randint(0,2)
    #show image
    image_label.config(image=image_list[pick_number])

    # 0 = rock
    # 1 = Papper
    # 2 = scissors
    # convert dropdown choice to a number

    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    # Determine if we won or lost
    if user_choice_value ==0: #Rock
        if pick_number ==0: 
            win_lose_label.config(text="Is's A Tie! Spin Again...")
        elif pick_number ==1: # Paper
            win_lose_label.config(text="Paper Cover Rock! you lose...")
        elif pick_number ==2: # scissors
            win_lose_label.config(text="Rock Smashes Scissors! you Win")

    # if user pick paper
    if user_choice_value ==1: #paper
        if pick_number ==1: 
            win_lose_label.config(text="Is's A Tie! Spin Again...")
        elif pick_number ==0: # rock
            win_lose_label.config(text="Paper Cover Rock! you win...")
        elif pick_number ==2: # scissors
            win_lose_label.config(text="Scissors Cuts Paper! you lose...")

    # If user Pick scissors
    if user_choice_value ==2: # scissors
        if pick_number ==2: 
            win_lose_label.config(text="Is's A Tie! Spin Again...")
        elif pick_number ==0: # rock
            win_lose_label.config(text="Rock smashes scissors! You Lose...")
        elif pick_number ==1: # peper
            win_lose_label.config(text="Scisssor Cuts Paper! You Win...")

# Make  our choice
user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

# create spin button
spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)

# Label for showing
win_lose_label = Label(root, text="", font=("Helvetica", 18), bg="white")
win_lose_label.pack(pady=50)


root.mainloop()