from tkinter import *
from tkhtmlview import HTMLLabel

root = Tk()
root.title("Python Tkinter How To Use HTML In Your Tkinter App")
root.geometry("500x600")


my_label = HTMLLabel(root, html="\
    <h1>\
    <a href='https://www.python.org/'>Download Python</a>\
    </h1>\
    <ul>\
    <li>One </li>\
    <li>Two </li>\
    <li>three </li>\
    </ul>\
    <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTr9vl91PpaNrX7_EiOaWpTyftYzOFEiQixBA&usqp=CAU'> ")

my_label.pack(pady=20,
    padx=20,
    fill = "both",
    expand=True)



root.mainloop()