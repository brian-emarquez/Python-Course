# Python Tkinter Build A text Editor III - Saves Files
# Python Tkinter Build A editor de texto

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Python Tkinter Build A text Editor III')
root.iconbitmap('Python Tkinter Build A text Editor III/icons/document.ico')
root.geometry("1000x660")

# Set Variable for opne file name
global open_status_name
open_status_name = False

# Create New File Function
def new_file():
    # Delete previos text
    my_text.delete("1.0", END)
    # Update status bars
    root.title("New File - TextPad!")
    status_bar.config(text="New File        ")

    global open_status_name
    open_status_name = False

# Open Files
def open_file():
    # Delete Precios Text
    my_text.delete("1.0", END)

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir="Python Tkinter Build A text Editor III/documents/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    
    # Check to see if there is a file name
    if text_file:
        # Make filename global so we can access it later
        global open_status_name
        open_status_name = text_file

    # Updaet status bars
    name = text_file
    status_bar.config(text=f'{name}         ')
    name = name.replace("C:/Users/brian/Documents/Python-Course/Python Tkinter Build A text Editor III/documents/", "")
    root.title(f'{name} - TextPad!')

    # Open the File
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    # Close the opened file
    text_file.close()

    # Add File textbox
    my_text.insert(END, stuff)

#Save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/brian/Documents/Python-Course/Python Tkinter Build A text Editor III/documents/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Updates Status Bars
        name = text_file
        status_bar.config(text=f'{name}         ')
        name = name.replace("C:/Users/brian/Documents/Python-Course/Python Tkinter Build A text Editor III/documents/", "")
        root.title(f'{name} - TextPad!')
        
        # Save File
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        #close the file
        text_file.close()

# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # Save File
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0, END))
        #close the file
        text_file.close()
        # put status
        status_bar.config(text=f'{open_status_name}         ')
    else:
        save_as_file()


# Creare Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="#4FDECD", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our Scroolbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#A Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar To Botton of App
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
