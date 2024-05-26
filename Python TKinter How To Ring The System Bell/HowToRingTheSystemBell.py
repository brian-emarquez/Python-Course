####################################################################
# Python TKinter How To Ring The System Bell
# Python TKinter Cómo tocar la campana del sistema
####################################################################

from tkinter import *

root = Tk()
root.title('Python TKinter How To Ring The System Bell')
root.iconbitmap('Python TKinter How To Ring The System Bell/icons/bell.ico')
root.geometry("500x500") 

# Define image
bell = PhotoImage(file="Python TKinter How To Ring The System Bell/images/bell.png")

# add image to label
bell_label = Label(root, image=bell)
bell_label.pack(pady=20)

def ring():
    root.bell()

# Create our button
my_button  = Button(root,
    text="Ring the Bell",
    command=ring,
    font=("Helvetica", 24),
    fg="#4d4d4d")

my_button.pack(pady=20)

#root.bell()
root.mainloop()