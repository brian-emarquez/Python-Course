#  Python Tkinter Dates and 2020 Countdown App
#  Python Tkinter Dates y la aplicación Countdown 2020

from tkinter import *
from datetime import date

root = Tk()
root.title("Python Tkinter Dates and 2020 Countdown App")
root.iconbitmap("Python Tkinter Dates and 2020 Countdown App/icons/h.ico")
root.geometry('500x350')

panic = Label(root, text="Don't Panic", font=("Helvetica", 42), bg="black", fg="green")
panic.pack(pady=20, ipadx=10, ipady=10)

# Get Date
today= date.today()

# Format Date
f_today = today.strftime("%A - %B %d, %Y")

# Output date
today_label = Label(root, text=f'Today is{f_today}')
today_label.pack(pady=20)

# Count Down
dats_is_year = 365
todays_day_number = int (today.strftime("%j"))

# Calculate days left in year
days_left = dats_is_year - todays_day_number

# output days left 
countdown_label = Label(root, text=f'There are only{days_left} days \n left in 2020!', font=("Helvetica", 20))
countdown_label.pack(pady=20)

root.mainloop()