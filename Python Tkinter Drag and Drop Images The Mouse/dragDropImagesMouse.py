# Python Tkinter Drag and Drop Images The Mouse
# Python Tkinter Arrastrar y soltar imágenes con el mouse

from tkinter import *

root = Tk()
root.title('Python Tkinter Drag and Drop Images The Mouse')
root.iconbitmap('Python Tkinter Drag and Drop Images The Mouse/icons/fun.ico')
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=10)

# my_circle = my_canvas.create_oval(x, y, x+10, y+10)
# Add image to Canvas
img = PhotoImage(file="Python Tkinter Drag and Drop Images The Mouse/images/eddy.png")
my_image = my_canvas.create_image(260,125, anchor=NW, image=img)

def left(event):
    x = -10
    y= 0
    my_canvas.move(my_image, x, y)

def right(event):
    x = 10
    y= 0
    my_canvas.move(my_image , x, y)

def up(event):
    x =0
    y= -10
    my_canvas.move(my_image , x, y)

def down(event):
    x =0
    y= 10
    my_canvas.move(my_image , x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()

