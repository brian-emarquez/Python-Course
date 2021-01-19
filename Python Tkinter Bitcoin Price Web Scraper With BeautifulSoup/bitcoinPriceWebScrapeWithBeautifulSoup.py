#############################################################################################
#  Python Tkinter Bitcoin Price Web Scraper With BeautifulSoup                              #
# Raspador web de precios de Bitcoin de Python Tkinter con BeautifulSoup                    #
#############################################################################################

from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib import request
from datetime import datetime

root = Tk()
root.title('Python Tkinter Bitcoin Price Web Scraper With BeautifulSoup')
root.iconbitmap('Python Tkinter Bitcoin Price Web Scraper With BeautifulSoup/icons/bitcoin.ico')
root.geometry("550x210")
root.config(bg="black")

global previous
previous = False 

# Create a Frame
my_frame = Frame(root, bg="black")
my_frame.pack(pady=20)

# Define logo image
logo = PhotoImage(file='Python Tkinter Bitcoin Price Web Scraper With BeautifulSoup/images/bitcoin.png')
logo_label = Label(my_frame, image=logo, bd=0)
logo_label.grid(row=0, column=0, rowspan=2)

# Add bitcoin  price label
bit_label = Label(my_frame, text="TEXT",
    font=("Helvetica", 45),
    bg="black",
    fg="green",
    bd=0)
bit_label.grid(row=0, column=1, padx=20, sticky="s")

# Latest Price up/Down
latest_price = Label(my_frame, text="move test",
    font=("Helvetica", 8),
    bg="black",
    fg="grey")

latest_price.grid(row=1, column=1, sticky="n")

# Grab the bitcoin Price
def Update():

    global previous
    page = urllib.request.urlopen("https://www.coindesk.com/price/bitcoin")

    # Grab bitcoin Prince

    # Set timer to 1 minute
    root.after(30000, Update)

# On program start
Update()
root.mainloop()