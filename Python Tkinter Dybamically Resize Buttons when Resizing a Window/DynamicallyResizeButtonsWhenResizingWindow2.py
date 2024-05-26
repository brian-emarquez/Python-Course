###############################################################################################
# Python Tkinter Dybamically Resize Buttons when Resizing a Window II
# Python Tkinter redimensiona dinámicamente los botones al redimensionar una ventana
#############################################################################################

from tkinter import *

root = Tk()
root.title('Python Tkinter Dybamically Resize Buttons when Resizing a Window')
root.iconbitmap('Python Tkinter Dybamically Resize Buttons when Resizing a Window/icons/theapplication.ico')
root.geometry("500x500") 


# Config row 2
Grid.columnconfigure(root, 0, weight=1)

# Create two Buttons
button_1 = Button(root, text="Button 1")
button_2 = Button(root, text="Button 2")
button_3 = Button(root, text="Button 3")
button_4 = Button(root, text="Button 4")



# Grid thm to the screen
button_1.grid(row=0, column=0, sticky="nsew")
button_2.grid(row=1, column=0, sticky="nsew")
button_3.grid(row=2, column=0, sticky="nsew")
button_4.grid(row=3, column=0, sticky="nsew")
# Create list of buttons
button_list = [button_1, button_2, button_3, button_4]

# Define row number
row_number = 0

# lopp thru the ist and config each row automatic
for button in button_list:
    Grid.rowconfigure(root, row_number, weight=1)
    # Increments the counter
    row_number +=1





root.mainloop()
