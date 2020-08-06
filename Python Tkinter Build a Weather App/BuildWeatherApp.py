# Python Tkinter Update a Record II
# API
# Extraccion y manejo de datos

from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Python Tkinter Build a Weather App')
root.iconbitmap('Python Tkinter Build a Weather App/weather.ico')
root.geometry("400x50") 
root.configure(background = "green")

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=D3E1D2B8-09F8-4FB3-AB63-6A2B716BEF52

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=D3E1D2B8-09F8-4FB3-AB63-6A2B716BEF52")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    qualty = api[0]['AQI']
    Category = api[0]['Category']['Name']

except Exception as e:
    api = "Error..."

myLabel = Label(root, text=city + " Air Quality " + str(qualty) + " " + Category, font = ("Helvetica", 20), background="green")
myLabel.pack()


root.mainloop()