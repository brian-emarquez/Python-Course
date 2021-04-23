## Build A Currency Converter App

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Python Tkinter Build A Currency Converter App')
root.iconbitmap('Python Tkinter Build A Currency Converter App/icons/currency.ico')
root.geometry("500x500")

# Create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create two Frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

#add our tabs
my_notebook.add(currency_frame, text="Currencies")
my_notebook.add(conversion_frame, text="Currencies")

##################################################
# CURRENCY STUFF
##################################################
def lock():
    pass

def unlock():
    pass

home = LabelFrame(currency_frame, text="Your home currency")
home.pack(pady=20)

# Home currency entry box
home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

# Conversion currency frame
conversion = LabelFrame(currency_frame, text="Conversion Currency ")
conversion.pack(pady=20)

# Covnert to label
conversion_label = Label(conversion, text="Currencuy to Convert to...")
conversion_label.pack(pady=10)

# Convert to Entry
conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10, padx=10) 

#
# rate label
rate_label = Label(conversion, text="Currencuy conversion Rate...")
rate_label.pack(pady=10)

# Convert to Entry
rate_entry = Entry(conversion, font=("Helvetica", 24))
rate_entry.pack(pady=10, padx=10) 

# Button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# create buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button .grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command=unlock)
unlock_button .grid(row=0, column=1, padx=10)

##################################################
# CONVERSION STUFF
##################################################

def convert():
    pass

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)


amount_label = LabelFrame(conversion_frame, text="Amount To Conver")
amount_label.pack(pady=20)

# Entry Box for amount
amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

# Convert Button
convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# Equals
converted_label = LabelFrame(conversion_frame, text="Convert Currency")
converted_label.pack(pady=20)

# Converted Entry
converted_entry = Entry(converted_label, font=("Helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

# Clear button
clear_buttton = Button(conversion_frame, text="Clear", command=clear)
clear_buttton.pack(pady=20)

# Face label for spacing
spacer = Label(conversion_frame, text="", width=68)

root.mainloop()
