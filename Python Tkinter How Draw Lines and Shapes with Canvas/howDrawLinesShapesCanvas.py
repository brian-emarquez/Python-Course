# Python Tkinter How Draw Lines and Shapes with Canvas
# Python Tkinter How Draw Lines and Shapes with Canvas

from tkinter import *

root = Tk()
root.title('Python Tkinter How Draw Lines and Shapes with Canvas')
root.iconbitmap('Python Tkinter How Draw Lines and Shapes with Canvas/api.ico')
root.geometry("500x500")


my_canvas = Canvas(root, width=300, height=200, bg="white")
my_canvas.pack(pady=20)

# create Rectangle
# x1, y1, x2, y2, fill"color"
my_canvas.create_rectangle(50, 150, 250, 50, fill="pink") 

# create Line
# x1, y1, x2, y2, fill"color"
my_canvas.create_line(0, 100, 300, 100 ,fill="red") # Linea Horizontal Rojas
my_canvas.create_line(150, 0, 150, 200 ,fill="red") # Linea Horizontal Rojas

# Create Oval
my_canvas.create_oval(50, 150, 250, 50, fill="cyan")

root.mainloop()


