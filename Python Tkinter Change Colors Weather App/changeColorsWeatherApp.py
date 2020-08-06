# Python Tkinter Change Colors Weather App
#


from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Python Tkinter Build a Weather App')
root.iconbitmap('Python Tkinter Build a Weather App/weather.ico')
root.geometry("450x50") 

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=D3E1D2B8-09F8-4FB3-AB63-6A2B716BEF52

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=D3E1D2B8-09F8-4FB3-AB63-6A2B716BEF52")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    qualty = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "unhelthy for sensitive groups":
        weather_color = "#ff9900"
    elif category == "Unhealthy":
        weather_color = "#FF0000"
    elif category == "Very unhelthy":
        weather_color = "#990066"
    elif category == "Hazardous":
        weather_color = "#660000"


    root.configure(background = weather_color)


    myLabel = Label(root, text=city + " Air Quality " + str(qualty) + " " + category, font = ("Helvetica", 20), background=weather_color)
    myLabel.pack()

except Exception as e:
    api = "Error..."



root.mainloop()