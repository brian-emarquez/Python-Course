# Python Tkinter Using Frames with Menus
# Python Tkinter usando marcos con menús

from tkinter import *


root = Tk()
root.title('Python Tkinter Using Frames with Menu!')
root.iconbitmap('Python Tkinter Using Frames with Menus/menu.ico')
root.geometry("400x600") 

my_menu = Menu(root)
root.config(menu=my_menu)

# Click Command
def our_comand():
    my_label = Label(root, text="You Clicked A Dropdown Menu!").pack()

# Click new Function
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    my_label = Label(file_new_frame, text="You Clicked the File >> New Menu!").pack()


# Edit Cut
def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    my_label = Label(edit_cut_frame, text="You Clicked the File >> Edit Cut!").pack()


# Hide all frames
def hide_all_frames():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


# Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator() # Separador
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu= Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_comand)

# Create an Options menu item
options_menu= Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Find", command=our_comand)
options_menu.add_command(label="Find Next", command=our_comand)

# Create some frames
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")
root.mainloop()