# Python Tkinter Text Box
# Caja de texto

from tkinter import *

root = Tk()

root.title('Learn To Code at Python Tkinter Text Box')
root.iconbitmap('Python Tkinter Text-Box/panda.ico')
root.geometry("600x600")

# Create Clear Function
def clear():
    my_text.delete(1.0, END)
    
# Grab the text from the text box    
def get_text():
    my_label.configure(text=my_text.get(1.0, END))
    

my_text = Text(root, width=60, height=20, font=("Helvetica", 16))
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear Screen", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="Get Text", command=get_text)
get_text_button.grid(row=0, column=1, padx=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
