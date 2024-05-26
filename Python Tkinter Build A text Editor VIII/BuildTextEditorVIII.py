# Python Tkinter Build A text Editor VIII - Print A File - Build A Text Editor
# Python Tkinter Build A editor de texto

from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api


root = Tk()
root.title('Python Tkinter Build A text Editor VIII')
root.iconbitmap('Python Tkinter Build A text Editor VIII/icons/document.ico')
root.geometry("1000x700")

# Set Variable for opne file name
global open_status_name
open_status_name = False

global selected
selected = False

#-------------------------------------------------------------------------------------------------------#
# Create New File Function
def new_file():
    # Delete previos text
    my_text.delete("1.0", END)
    # Update status bars
    root.title("New File - TextPad!")
    status_bar.config(text="New File        ")

    global open_status_name
    open_status_name = False

#-------------------------------------------------------------------------------------------------------#
# Open Files
def open_file():
    # Delete Precios Text
    my_text.delete("1.0", END)

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir="Python Tkinter Build A text Editor VIII/documents/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    
    # Check to see if there is a file name
    if text_file:
        # Make filename global so we can access it later
        global open_status_name
        open_status_name = text_file

    # Updaet status bars
    name = text_file
    status_bar.config(text=f'{name}         ')
    name = name.replace("C:/Users/brian/Documents/Python-Course/Python Tkinter Build A text Editor VIII/documents/", "")
    root.title(f'{name} - TextPad!')

    # Open the File
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    # Close the opened file
    text_file.close()

    # Add File textbox
    my_text.insert(END, stuff)

#-------------------------------------------------------------------------------------------------------#
#Save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/brian/Documents/Python-Course/Python Tkinter Build A text Editor VIII/documents/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Updates Status Bars
        name = text_file
        status_bar.config(text=f'{name}         ')
        name = name.replace("C:/Users/brian/Documents/Python-Course/Python Tkinter Build A text Editor VIII/documents/", "")
        root.title(f'{name} - TextPad!')
        
        # Save File
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        #close the file
        text_file.close()

#-------------------------------------------------------------------------------------------------------#
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

#-------------------------------------------------------------------------------------------------------#
# cut Text
def cut_text(e):
    global selected
    
    if e:
        selected = root.clipboard_get()

    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            # Delected selected text from box
            my_text.delete("sel.first", "sel.last")
            #clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)

#-------------------------------------------------------------------------------------------------------#
# copy Text
def copy_text(e):
    global selected
    #CHECK TO SEE IF WE USED KEYBOARD SHORTCUTS
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        # Grab selected text from text box
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

#-------------------------------------------------------------------------------------------------------#
# paste Text
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

#-------------------------------------------------------------------------------------------------------#
# Bold Text
def bold_it():
    # Create our font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # Configure a Tag
    my_text.tag_configure("bold", font=bold_font)

    # define Current tag
    current_tags = my_text.tag_names("sel.first")

    # If stament to see if tag has been set
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")

    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

#-------------------------------------------------------------------------------------------------------#
# Italics Text
def italics_it():
    # Create our font
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    # Configure a Tag
    my_text.tag_configure("italic", font=italic_font)

    # define Current tag
    current_tags = my_text.tag_names("sel.first")

    # If stament to see if tag has been set
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")

    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

#-------------------------------------------------------------------------------------------------------#
# Change Selected text Color
def text_color():

    # Pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:

        status_bar.config(text=my_color)

        # Create our font
        color_font = font.Font(my_text, my_text.cget("font"))

        # Configure a Tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)

        # define Current tag
        current_tags = my_text.tag_names("sel.first")

        # If stament to see if tag has been set
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")

        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

#-------------------------------------------------------------------------------------------------------#
# Change bg color
def bg_colors():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

#-------------------------------------------------------------------------------------------------------#
# Change All text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

#-------------------------------------------------------------------------------------------------------#
# Print File Fuction
def print_file():
    #printer_name = win32print.GetDefaultPrinter()
    #status_bar.config(text=printer_name) # detencio de nombre de impresora

    file_to_print = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/brian/Documents/Python-Course/Python Tkinter Build A text Editor VIII/documents/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


#-------------------------------------------------------------------------------------------------------#
# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

#-------------------------------------------------------------------------------------------------------#
# Creare Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal Scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

# Create Text Box
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="#4FDECD", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none",  xscrollcommand=hor_scroll.set)
my_text.pack()

# Configure our Scroolbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

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
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")

# Add color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_colors)


# Add Status Bar To Botton of App
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

#fee = "Brian Marquez"
#my_label = Label(root, text=fee[:-1]).pack()

# Create Button

# Bold Button
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)

# Italics Button
italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5)

# Undo/Redo Buttons
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

# Tet Color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)

root.mainloop()
