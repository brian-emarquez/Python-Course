# Python Tkinter Using Icons, Images And Exit Buttons
# pillow


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code at Code') # titulo
root.iconbitmap('Python Tkinter Using Icons, Image/icon.ico')


my_img = ImageTk.PhotoImage(Image.open("Python Tkinter Using Icons, Image/django.gif"))
my_label = Label(image=my_img)
my_label.pack()


#close 
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()