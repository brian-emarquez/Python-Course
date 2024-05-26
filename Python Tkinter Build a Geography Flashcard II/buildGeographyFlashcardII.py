# Python Tkinter Build a Geography Flashcard II
# Python Tkinter Construye una tarjeta de geografía

from tkinter import *
from PIL import ImageTk, Image
from random import randint


root = Tk()
root.title('Python Tkinter Build a Geography Flashcard II')
root.iconbitmap('Python Tkinter Build a Geography Flashcard II/avatar.ico')
root.geometry("500x500")

# Create state flascard Function
def states():
    # Hide previous frames
    hice_all_frames() # borra el frame anterior
    state_frame.pack(fill="both", expand=1)
    #my_label = Label(state_frame, text="States").pack()

    # Create list of state names
    our_states = ['califonia', 'florida', 'illinois', 'kentucky','nebraska', 'newyork', 'oregon', 'texas']

    # Generate a random number
    rando = randint(0, len(our_states)-1)
    state = "Python Tkinter Build a Geography Flashcard II/states/" + our_states[rando] + ".png"

    # Create our State Images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state = Label(state_frame, image=state_image)
    show_state.pack(pady=15)

    # Create Button randomize state Images
    randon_button = Button(state_frame, text="New State", command=states)
    randon_button.pack(pady=10)

# Create State Capital Flashcard Function
def state_capitals():
    # Hide previous frames
    hice_all_frames() # borra el frame anterior
    state_capitals_frame.pack(fill="both", expand=1)
    #my_label = Label(state_capitals_frame, text="States Capitals").pack()

# Create our Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Hide all previous frames
def hice_all_frames():
    for Widget in state_frame.winfo_children():
        Widget.destroy()

    for Widget in state_capitals_frame.winfo_children():
        Widget.destroy()

    state_frame.pack_forget()
    state_capitals_frame.pack_forget()



# Create Geography Menu Items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="State Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

# Create our Frames
state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)



root.mainloop()