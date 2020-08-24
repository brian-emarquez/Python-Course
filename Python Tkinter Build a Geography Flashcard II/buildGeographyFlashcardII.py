# Python Tkinter Build a Geography Flashcard II
# Python Tkinter Construye una tarjeta de geografía

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Python Tkinter Build a Geography Flashcard II')
root.iconbitmap('Python Tkinter Build a Geography Flashcard II/avatar.ico')
root.geometry("500x500")

# Create state flascard Function
def states():
    # Hide previous frames
    hice_all_frames() # borra el frame anterior
    state_frame.pack(fill="both", expand=1)
    my_label = Label(state_frame, text="States").pack()

# Create State Capital Flashcard Function

def state_capitals():
    # Hide previous frames
    hice_all_frames() # borra el frame anterior
    state_capitals_frame.pack(fill="both", expand=1)
    my_label = Label(state_capitals_frame, text="States Capitals").pack()

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