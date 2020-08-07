# Python Tkinter Create CRM database Tool
# 

from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Python Tkinter Create CRM database Tool')
root.iconbitmap('Python Tkinter Create CRM database Tool/check.ico')
root.geometry("400x200") 


def graph():
    house_prices = np.random.normal(200000, 25000, 5000) 
    #plt.pie(house_prices, 200) # tipo de grafico, granularidad
    #plt.pie(house_prices) 
    plt.polar(house_prices) 
    plt.show()

my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()



root.mainloop()