#  Python Tkinter Ballon Text Tools
#  Herramientas de texto de globo de Python Tkinter

from tkinter import *
from tkinter.tix import *

root = Tk()
root.title("Python Tkinter Ballon Text Tools")
root.iconbitmap("Python Tkinter Ballon Text Tools/icons/balloons.ico")
root.geometry('500x350')

# Create Tolltio
tip = Balloon(root)
tip.config(bd=10, bg="blue")

# sub caterories
tip.label.config(bg="red", fg="green", bd=10)
tip.message.config(bg="red", fg="white")

# Button
my_button = Button(root, text="Click me!")
my_button.pack(pady=50)

# Label
my_label = Label(root, text="Some Text", font=("Helvetica", 20))
my_label.pack(pady=20)

# Label
my_label = Label(root)
# Bind tooltip to Button
tip.bind_widget(my_button, balloonmsg="This is my awersome toolstip!")

# Bind tooltip to Button
tip.bind_widget(my_label, balloonmsg="This is my awersome toolstip!")




root.mainloop()