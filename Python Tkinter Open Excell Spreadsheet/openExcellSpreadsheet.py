# Python Tkinter Open Excell Spreadsheet
# Hoja de cálculo de Python Tkinter Open Excell

# pip install pandas
# pip install xlrd

from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog

root = Tk()
root.title('Python Tkinter Open Excell Spreadsheetx')
root.iconbitmap('Python Tkinter Open Excell Spreadsheet/icons/excel.ico')
root.geometry("800x400")

# Create Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create treeview
my_tree = ttk.Treeview(my_frame)

# File open Function
def file_open():
    filename = filedialog.askopenfilename(

        initialdir="Python Tkinter Open Excell Spreadsheet/documents",
        title = "Open A File", 
        filetype = (("xlsx files", "*.xlsx"), ("All Files", "*.*"))
        )

    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File couldn't Be Opened.. try again!")
        except FileNotFoundError:
            my_label.config(text="File couldn't Be Found.. try again!")
    
    clear_tree()

    # Set up new trereview
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"

    #loop thru column list
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # Put data in trereView
    df_rows = df.to_numpy(). tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)

    # pack the treeview finally
    my_tree.pack()


def clear_tree():
    my_tree.delete(*my_tree.get_children())

# Add a menu
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()
