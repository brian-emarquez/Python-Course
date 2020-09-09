# Python Tkinter Drag and Drop Images With the Mouse
# Python Tkinter Arrastra y suelta imágenes con el mouse

from tkinter import *

root = Tk()
root.title('Python Tkinter Drag and Drop Images With the Mouse')
root.iconbitmap('Python Tkinter Drag and Drop Images With the Mouse/api.ico')
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=10)

# my_circle = my_canvas.create_oval(x, y, x+10, y+10)
# Add image to Canvas
img = PhotoImage(file="Python Tkinter Drag and Drop Images With the Mouse/eddy.png")
my_image = my_canvas.create_image(260,125, anchor=NW, image=img)

def move(e):

    global img
    img = PhotoImage(file="Python Tkinter Drag and Drop Images With the Mouse/eddy.png")
    my_image = my_canvas.create_image(e.x, e.y, image=img)
    my_label.config(text="Coordinates x: " + str(e.x) + " y: " + str(e.y)) # Movimiento
    


#root.bind("<Left>", left)
#root.bind("<Right>", right)
#root.bind("<Up>", up)
#root.bind("<Down>", down)
my_label = Label(root, text="")
my_label.pack(pady=50)

my_canvas.bind('<B1-Motion>', move)



root.mainloop()

