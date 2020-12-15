##########################################################
# Python Tkinter How To Define Custom Fonts
# Python Tkinter Cómo definir fuentes personalizadas
##########################################################

from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Python Tkinter How To Define Custom Fonts')
root.iconbitmap('Python Tkinter How To Define Custom Fonts/icons/arrow.ico')
root.geometry("500x500")

# Define Out Font
bigFont = Font(
    family = "Tines",
    size=42,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0)

mediumFont = Font(
    family = "Helvetica",
    size=24,
    weight="normal",
    slant="italic",
    underline=1,
    overstrike=0)

#Define A butoon,
my_button1 = Button(root, text="Big Text", font=bigFont)
my_button1.pack(pady=20)


# Label
mylabel = Label (root, text="More Big Text", font=bigFont)
mylabel.pack(pady=20)

root.mainloop()