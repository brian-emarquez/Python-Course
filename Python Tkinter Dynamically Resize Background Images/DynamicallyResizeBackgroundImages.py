#####################################################################
# Dynamically Resize Background Images
# Cambiar el tamaño de las imágenes de fondo de forma dinámica
#####################################################################

from tkinter import *
from PIL import ImageTk, Image

#pip install pillow

root = Tk()
root.title('Python Tkinter Dynamically Resize Background Images')
root.iconbitmap('Python Tkinter Dynamically Resize Background Images/icons/pikachu.ico')
root.geometry("750x450")

# Define image
bg = ImageTk.PhotoImage(file="Python Tkinter Dynamically Resize Background Images/images/mario.png")

# Create a canvas
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas 
my_canvas.create_image(0,0, image=bg, anchor="nw")

# add label
my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50), fill="white")

# add some buttons
button1 = Button(root, text="Start")
button2 = Button(root, text="Reset Score")
button3 = Button(root, text="Exit")

button1_window = my_canvas.create_window(10, 10, anchor="nw", window=button1)
button2_window = my_canvas.create_window(50, 10, anchor="nw", window=button2)
button3_window = my_canvas.create_window(130, 10, anchor="nw", window=button3)

def resizer(e):
    global bg1, resize_bg, new_bg

    bg1 = Image.open("Python Tkinter Dynamically Resize Background Images/images/mario.png")
    # Resize the image
    resize_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    # DEFINE OUR IMAGE AGAIN
    new_bg = ImageTk.PhotoImage(resize_bg)
    #  add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    # READ THE TEXT
    my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50), fill="white")


root.bind('<Configure>', resizer)
root.mainloop()


