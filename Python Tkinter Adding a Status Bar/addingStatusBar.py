# Python Tkinter Build an Imagen Viewer
# Intercambio de Imagenes
# Python Tkinter Construye un visor de imágenes

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Pyhton Image Viewer') # titulo
root.iconbitmap('Python Tkinter Using Icons, Image/icon.ico')

myimg1 = ImageTk.PhotoImage(Image.open("Python Tkinter Build an Imagen Viewer/1.jpg"))
myimg2 = ImageTk.PhotoImage(Image.open("Python Tkinter Build an Imagen Viewer/2.jpg"))
myimg3 = ImageTk.PhotoImage(Image.open("Python Tkinter Build an Imagen Viewer/3.jpg"))
myimg4 = ImageTk.PhotoImage(Image.open("Python Tkinter Build an Imagen Viewer/4.jpg"))
myimg5 = ImageTk.PhotoImage(Image.open("Python Tkinter Build an Imagen Viewer/5.png"))
myimg6 = ImageTk.PhotoImage(Image.open("Python Tkinter Build an Imagen Viewer/6.png"))

image_list = [myimg1,myimg2, myimg3, myimg4, myimg5, myimg6]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # Mensaje en pantalla - anchor=W-E



my_label = Label(image=myimg1)
my_label.grid(row=0, column=0, columnspan=3)

#-------------------------------------------- FUNCIONES ------------------------------------------------------------

def forward(image_number):
    global my_label
    global Button_forward
    global Button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    Button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    Button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 6:
        Button_forward = Button(root, text=">>", state=DISABLED )


    my_label.grid(row=0, column=0, columnspan=3)
    Button_back.grid(row=1, column=0)
    Button_forward.grid(row=1, column=2)

    status = Label(root, text="Image "+ str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # Mensaje en pantalla - anchor=W-E
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# ---------------------------------------------------------------------------------------------------------------


def back(image_number):
    global my_label
    global Button_forward
    global Button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    Button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    Button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        Button_back = Button(root, text="<<", state=DISABLED) # desabilitar

    my_label.grid(row=0, column=0, columnspan=3)
    Button_back.grid(row=1, column=0)
    Button_forward.grid(row=1, column=2)
    
    #Uodate status bar
    status = Label(root, text="Image "+ str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) # Mensaje en pantalla - anchor=W-E
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# --------------------------------------------------------------------------------------------------------------

Button_back = Button(root, text="<<", command = lambda: back, state=DISABLED) 
Button_exit = Button(root, text="EXIT PROGRAM", command = root.quit)
Button_forward = Button(root, text=">>", command = lambda: forward(2))

Button_back.grid(row=1, column=0)
Button_exit.grid(row=1, column=1)
Button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E) # Linea Horizoantal


root.mainloop()