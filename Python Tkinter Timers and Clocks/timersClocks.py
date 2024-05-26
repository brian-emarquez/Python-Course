# Python Tkinter Timers and Clocks
# Temporizadores y relojes de Python Tkinter

from tkinter import *
import time

root = Tk()
root.title('Python Tkinter Timers and Clocks')
root.iconbitmap('Python Tkinter Timers and Clocks/pineapple.ico')
root.geometry("600x400") 

def clock():
    hour= time.strftime("%I")
    minute= time.strftime("%M")
    second= time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")

    my_label.config(text=hour + ":" + minute + ":" + second+ " " + am_pm)
    my_label.after(1000, clock) # segundos

    my_label2.config(text=time_zone + " " + day)


def update():
    my_label.config(text="New Text")

my_label = Label(root, text="", font=("Helvetica", 48), fg="green", bg="black")
my_label.pack(pady=20)

my_label2= Label(root, text="", font=("Helvetica", 14))
my_label2.pack(pady=10)

clock()

root.mainloop()