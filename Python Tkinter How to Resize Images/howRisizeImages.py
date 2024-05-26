# Python Tkinter How To Riseze Entry Box height
# Python Tkinter Cómo elevar la altura del cuadro de entrada

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python Tkinter How to Resize Images')
root.iconbitmap('Python Tkinter How to Resize Images/pineapple.ico')
root.geometry("800x500") 

# Open Image
my_pic = Image.open("Python Tkinter How to Resize Images/image/moonglow.png")

# Resize Image
resized = my_pic.resize((250, 225), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

# Image size 500x750 /2500
my_label = Label(root, image=new_pic)
my_label.pack(pady=20)

root.mainloop()