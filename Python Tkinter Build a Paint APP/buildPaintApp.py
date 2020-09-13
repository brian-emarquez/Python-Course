# Python Tkinter Build a Paint APP
# Python Tkinter crea una aplicación de pintura

from tkinter import *
from tkinter.ttk import Scale

class Paint():
    def __init__(self, root):
        self.root = root
        self.root.title("Paint in Python")
        self.root.geometry("800x520")
        self.root.configure(background="white")
        self.root.resizable(0,0)

        # adding widgeths to tkinter window
        self.color_frame = LabelFrame(self.root, text="color", font = ('arial, 13'), bd=5, relief=RIDGE, bg="white")
        self.color_frame.place(x=0, y=0, width=70, height=185)

        colors = ['#ff0000', '#ff4dd2', '#ffff33', '#000000', '#0066ff','#660033','#4dff4d', '#b300b3', '#00ffff', '#00ffff', '#808080', '#99ffcc']
        i = j =0
        for color in colors:
            Button(self.color_frame, bg=color, bd=2, relief=RIDGE, width=3, command=None).grid(row=i, column=j)
            i +=1
            if i==6:
                i=0
                j=1

        self.eraser_button = Button(self.root, text="ERASER", bd=4, bg="white", command=None, width=8, relief=RIDGE)
        self.eraser_button.place(x=0, y=187)

        self.clear_button = Button(self.root, text="Clear", bd=4, bg="white", command=None, width=8, relief=RIDGE)
        self.clear_button.place(x=0, y=217)

        self.save_button = Button(self.root, text="Save", bd=4, bg="white", command=None, width=8, relief=RIDGE)
        self.save_button.place(x=0, y=247)

        self.canvas_color_button = Button(self.root, text="Canvas", bd=4, bg="white", command=None, width=8, relief=RIDGE)
        self.canvas_color_button.place(x=0, y=277)

        # creating a scale for pen and araser size..

        self.pen_size_scale_frame = LabelFrame(self.root, text="size", bd=5, bg="white", font=('arial', 15, 'bold'), relief=RIDGE)
        self.pen_size_scale_frame.place(x=0, y=310, height=200, width=70)

        self.pen_size = Scale(self.pen_size_scale_frame, orient=VERTICAL, from_ = 50,  to = 0, length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column=1, padx=15)

        # creating canvas
        self.canvas = Canvas (self.root, bg='white', bd=5, relief=GROOVE, height=500, width=700)
        self.canvas.place(x=80, y=0)


if __name__=="__main__":
    root = Tk()
    p = Paint(root)
    root.mainloop()







