####################################################################
# Python TKinter Using Entry Boxes On Canvas
# Python TKinter usando cuadros de entrada en lienzo
####################################################################

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python TKinter Using Entry Boxes On Canvas')
root.iconbitmap('Python TKinter Using Entry Boxes On Canvas/icons/canvas.ico')
root.geometry("323x576") 

# Define background Image
bg = ImageTk.PhotoImage(file="Python TKinter Using Entry Boxes On Canvas/images/background.jpg")

# Define canvas
my_canvas = Canvas(root, width=323, height=576, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Put the image on the canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

# Define Entry Boxes
un_entry = Entry(root,font=("Helvetica", 24), width=14, fg="#336d92", bd=0)
pw_entry = Entry(root,font=("Helvetica", 24), width=14, fg="#336d92", bd=0)

# Add the entry boxes to the canvas

un_window = my_canvas.create_window(34, 290, anchor="nw", window=un_entry)
pw_window = my_canvas.create_window(34, 370, anchor="nw", window=pw_entry)

# Define Button
login_bt = Button(root, text="Login", font=("Helvetica", 20), width=15, fg="#336d92")
login




root.mainloop()