# Python Tkinter Open Files Dialog Box
# ventana para cargar imagenes

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learn to Python')
root.iconbitmap('Python Tkinter Open Files Dialog Box/icon.ico')


def open():
    global my_iamge

    root.filename = filedialog.askopenfilename(initialdir="/Python Tkinter Open Files Dialog Box/images", title="Select A File", filetype=(("jpg files","*.jpg"), ("all file", "*.*")))
    my_Label = Label(root, text=root.filename).pack()
    my_iamge = ImageTk.PhotoImage(Image.open(root.filename))
    my_iamge_label = Label(image=my_iamge).pack()

my_btn = Button(root, text="Open File", command=open).pack()


root.mainloop()
