#  Centrado
from tkinter import *

root = Tk()
root.title("Python Tkinter How to Center Windows on the Screen")
root.iconbitmap("Python Tkinter How to Center Windows on the Screen/icons/window.ico")

# Designeate Height and Wifht of our app
app_width = 500
app_height = 500

screen_width = root.winfo_screenwidth() 
screen_height = root.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)


root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

my_label = Label(root, text=f'Width:{screen_width} Height:{screen_height}')
my_label.pack(pady=20)

root.mainloop()