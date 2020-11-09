# Python Tkinter Tile Matching Game II Finishing Our Tile Matching Game
# Terminando nuestro juego de combinación de azulejos

from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Python Tkinter Tile Matching Game II')
root.iconbitmap('Python Tkinter Tile Matching Game II/icons/icons.ico')
root.geometry("460x450") 

# Reset the Game
def reset():
    global matches, matches
    winner = 0
    matches = [1,1,2,2,3,3,4,4,5,5,6,6] 
    random.shuffle(matches)

    # reset label
    my_label.config(text="")

    # Reset out tiles
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    # Loop thru buttons and change colors
    for button in button_list:
        button.config(text="", bg="SystemButtonFace", state="normal") 


# Create winner fution
def win():
    my_label.config(text="Congratulations! you win!!")
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    # Loop thru buttons and change colors
    for button in button_list:
        button.config(bg="yellow")

global winner
# set winner counter to 0
winner = 0

#create our matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6] 

# Define some VARIABLES
count = 0
answer_list = []
answer_dict = {}


# Shuffle our matches
random.shuffle(matches)

#print(matches)

#Create button Frame
my_frame = Frame(root)
my_frame.pack(pady=10)


#Function fir cliching buttons
def button_click(b, number):
    global count, answer_list, answer_dict , winner 

    if b["text"] == ' ' and count < 2:
        b["text"] = matches[number]
        #add number to answer list
        answer_list.append(number)
        # add button and number to Answer Dictionary
        answer_dict[b] = matches[number]
        # Increment our Counter
        count += 1
        #print(answer_list)

    # Start too determine correct or not
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text="MATCH!")
            for Key in answer_dict:
                Key["state"] = "disable"
            count = 0
            answer_list = []
            answer_dict = {}
            # Increment our winner counters
            winner += 1
            if winner == 6:
                win()

        else:
            #my_label.config(text="DOH!")
            count = 0
            answer_list = []
            # POP UP BOX
            messagebox.showinfo("Incorrect", "Incorrect")

            # Reset the Buttons
            for Key in answer_dict:
                Key["text"] = " "

            answer_dict = {}

#Define out buttons
b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b0, 0), relief="groove")
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b1, 1), relief="groove")
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b2, 2), relief="groove")
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b3, 3), relief="groove")
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b4, 4), relief="groove")
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b5, 5), relief="groove")
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b6, 6), relief="groove")
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b7, 7), relief="groove")
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b8, 8), relief="groove")
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b9, 9), relief="groove")
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b10, 10), relief="groove")
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda : button_click(b11, 11), relief="groove")

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

my_label = Label(root, text="")
my_label.pack(pady=20)

# Create a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create an Options Dropdown Menu
OptionMenu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=OptionMenu)
OptionMenu.add_command(label="Reset Game", command=reset) 
OptionMenu.add_separator()
OptionMenu.add_command(label="Exit Game", command=root.quit) 




root.mainloop()