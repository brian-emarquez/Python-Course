# Python Tkinter Create a Data Picker Calendar
# Python Tkinter Crear un calendario de selector de datos

#install : pip install tkcalendar

from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Python Tkinter Create a Data Picker Calendar')
root.iconbitmap('Python Tkinter Create a Data Picker Calendar/api.ico')
root.geometry("600x600")

cal = Calendar(root, selectmode="day", year=2020, moth=5, day=22)
cal.pack(pady=20)

def grab_date():
    my_label.config(text="Today's Date is" + cal.get_date())


my_button = Button(root, text="Get Date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()

