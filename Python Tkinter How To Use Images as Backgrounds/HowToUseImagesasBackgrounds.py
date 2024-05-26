#####################################################################
# Python Tkinter How To Use Images as Backgrounds
# Python Tkinter Cómo usar imágenes como fondos
#####################################################################

from tkinter import *

root = Tk()
root.title('Python Tkinter How To Use Images as Backgrounds')
root.iconbitmap('Python Tkinter How To Use Images as Backgrounds/icons/pikachu.ico')
root.geometry("900x600")

# Define image
bg = PhotoImage(file="Python Tkinter How To Use Images as Backgrounds/images/mario.png")

# Create a Label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


# Add something to the of our image
my_text = Label(root, text="Welcome!", font=("Helvetica", 50), fg="white", bg='#6b88fe')
my_text.pack(pady=50)

# create frame
my_frame = Frame(root, bg='#6b88fe')
my_frame.pack(pady=20)

# add some buttons
my_button1  = Button(my_frame, text="Exit")
my_button1.grid(row=0, column=0, padx=20)

my_button2  = Button(my_frame, text="Start")
my_button2.grid(row=0, column=1, padx=20)

my_button3  = Button(my_frame, text="Reset")
my_button3.grid(row=0, column=2, padx=20)

root.mainloop()


