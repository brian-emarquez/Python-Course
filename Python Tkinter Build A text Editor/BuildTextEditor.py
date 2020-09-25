# Python Tkinter Build A text Editor
# Python Tkinter Build A editor de texto

from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Python Tkinter Build A text Editor')
root.iconbitmap('Python Tkinter Build A text Editor/icons/document.ico')
root.geometry("1200x660")

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


root.mainloop()
