# Python Tkinter Adding Full Screen ScrollBar
# Python Tkinter agregando barra de desplazamiento de pantalla completa

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Learn To Code at Python Tkinter Adding Full Screen ScrollBar')
root.iconbitmap('Python Tkinter Adding Full Screen ScrollBar/panda.ico')
root.geometry("500x400")

# Create a Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add A Scrollbar To the canvas
my_scrollbar = ttk.ScrollBar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.apck(side=RIGHT, fill=Y)

#  Configure The canvas
my_canvas.configure(yscrollcommand=my_canvas.yview)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(Scrollbarregion = my_canvas.bbox("all")))

# Create ANOTHER frame INISE th canvas
second_frame = Frame(my_canvas)

# add that New frame to a window In Th Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


for thing in range(100):
    Button(root, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)



root.mainloop()
