# Python TKinter Using config() to update widget

from tkinter import *

root = Tk()
root.title('Python TKinter Using config() to update widget')
root.iconbitmap('Python TKinter Using config() to update widget/api.ico')
root.geometry("400x400")

def something():
    my_label.config(text="This is new text!", font=("Helvetica", 13))
    root.config(bg="blue")
    my_button.config(text="You've benn Configged!", state=DISABLED)

global my_label
my_label = Label(root, text="This is my text", font=("Helvetica", 17))
my_label.pack(pady=10)

global my_button
my_button = Button(root, text="Click me", command=something)
my_button.pack(pady=10)

root.mainloop()


