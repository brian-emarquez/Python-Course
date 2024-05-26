##############################################################
# How To Use The Message Widget For Blocks of Text
#############################################################

from tkinter import *

root = Tk()
root.title("Python Tkinter How To Use The Message Widget For Blocks of Text")
root.iconbitmap("Python Tkinter How To Use The Message Widget For Blocks of Text/icons/hulk.ico")
root.geometry("500x800")

def change():
    my_message.config(text="And now something complety defferent!")

# First One
frame1 = LabelFrame(root, text="Left Justified")
frame1.pack(pady=20)

my_message = Message(frame1, text="This is some \n long text i am typing so that we can lok at it, isn look ",
    font=("Helvetica", 18),
    aspect=150,
    justify=LEFT)
my_message.pack(pady=10, padx=10)

# Seconds One
frame2 = LabelFrame(root, text="Right Justified")
frame2.pack(pady=20)

my_message2 = Message(frame2, text="This is some \n long text i am typing so that we can lok at it, isn look ",
    font=("Helvetica", 18),
    aspect=150,
    justify=RIGHT)
my_message2.pack(pady=10, padx=10)

# Thrird One
frame3 = LabelFrame(root, text="Center Justified")
frame3.pack(pady=20)

my_message3 = Message(frame3, text="This is some \n long text i am typing so that we can lok at it, isn look ",
    font=("Helvetica", 18),
    aspect=150,
    justify=CENTER)
my_message3.pack(pady=10, padx=10)

# Button
my_button = Button(root, text="Change Text", command=change)
my_button.pack(pady=20)


root.mainloop()