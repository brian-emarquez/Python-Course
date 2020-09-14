# Pyhton Tkinter Get Height and Width
# Pyhton Tkinter Obtener altura y ancho

from tkinter import *

root = Tk()
root.title('Pyhton Tkinter Get Height and Width')
root.iconbitmap('Pyhton Tkinter Get Height and Width/liam.ico')
root.geometry("600x400+-200+100") 


def suffle():
    my_label = Label(root, text="", font("Helvetica", 48))
    my_label.pack()

states = ['ancash', 'apurimac', 'arequipa', 'ayacucho', 'cajamarca', 'cerro de pasco', 'cuzco', 'huancavelica', 'huanuco', 'ica', 'junin', 'la libertad', 'lambayeque', 'lima', 'madre de dios', 'moquegua', 'piura', 'puno', 'san martin', 'tacna', 'tumbes', 'ucayali', 'amazonas', 'loreto']

root.mainloop()