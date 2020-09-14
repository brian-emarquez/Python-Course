# Pyhton Tkinter Get Height and Width
# Pyhton Tkinter Obtener altura y ancho

from tkinter import *

root = Tk()
root.title('Pyhton Tkinter Get Height and Width')
root.iconbitmap('Pyhton Tkinter Get Height and Width/liam.ico')
root.geometry("800x800+-200+100") 

def info():
    dimension_label = Label(root, text=root.winfo_geometry())
    dimension_label.pack(pady=20)

    height_label = Label(root, text="Height: " + str(root.winfo_height()))
    height_label.pack(pady=20)
    width_label = Label(root, text="Width: " + str(root.winfo_width()))
    width_label.pack(pady=10)

    x_label = Label(root, text="X: " + str(root.winfo_x()))
    x_label.pack(pady=20)
    y_label = Label(root, text="Y " + str(root.winfo_y()))
    y_label.pack(pady=10)

my_button = Button(root, text="ClickMe", command=info)
my_button.pack(pady=20)




root.mainloop()