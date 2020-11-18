###############################################################################################
# Python Tkinter Dybamically Resize Buttons when Resizing a Window
# Python Tkinter redimensiona dinámicamente los botones al redimensionar una ventana
#############################################################################################

from tkinter import *

root = Tk()
root.title('Python Tkinter Dybamically Resize Buttons when Resizing a Window')
root.iconbitmap('Python Tkinter Dybamically Resize Buttons when Resizing a Window/icons/theapplication.ico')
root.geometry("500x500") 

# Config our column rows and cols
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

# Config row 2
Grid.rowconfigure(root, 1, weight=1)


# Create two Buttons
button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")

# Grid thm to the screen
button_1.grid(row=0, column=0, sticky="nsew")
button_2.grid(row=1, column=0, sticky="nsew")




root.mainloop()
