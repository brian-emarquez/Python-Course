#####################################################################
# Python Tkinter How To Use Images as Backgrounds 2
# Python Tkinter Cómo usar imágenes como fondos
#####################################################################

from tkinter import *

root = Tk()
root.title('Python Tkinter How To Use Images as Backgrounds')
root.iconbitmap('Python Tkinter How To Use Images as Backgrounds/icons/pikachu.ico')
root.geometry("900x600")

# Define image
bg = PhotoImage(file="Python Tkinter How To Use Images as Backgrounds/images/mario.png")

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

root.mainloop()


