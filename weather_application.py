#----------------------------------------WEATHER APPLICATION----------------------------------------

import tkinter as tk
import requests
from tkinter import font

#--------------------------------------FUNCTION FOR DISPLAYING THE WEATHER CONDITIONS------------------------


def get_result(weather):
    try:
        a = weather['name']
        b = weather['weather'][0]['description']
        c = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']

        final_str = 'City = ' + str(a) + '\nConditions = ' + str(b) + '\nTemperature = ' + str(c) + '°C' + '\nFeels like = ' + str(feels_like) + '°C' + '\nTemperature min = ' + str(temp_min) + '°C' + '\nTemperature max = ' + str(temp_max) + '°C' + '\npressure = ' + str(pressure) + '\nHumidity = ' + str(humidity) + '%'
    except:
        final_str = 'There was a problem in retrieving the information'
    return final_str


#------------------------------------FUNCTION FOR GETTING THE REQUIRED INFORMATION---------------------------------


def get_weather(enter):
    weather_key = '2140004b122066c33d4c3361cd2ef42bFEW4252423'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    pam = {'appid': weather_key, 'q': enter, 'units': 'Metric'}
    response = requests.get(url, params=pam)
    weather = response.json()
    print(weather)

    label['text'] = get_result(weather)


#----------------------------------------------CODE FOR THE USER INTERFACE------------------------------------


rex = tk.Tk()

rex.title('Weather')

canvas = tk.Canvas(rex, height=500, width=700)
canvas.pack()

background_image = tk.PhotoImage(file='po.png')
background_place = tk.Label(rex, image=background_image)
background_place.place(relwidth=1, relheight=1)

frame = tk.Frame(rex, bg='#C0C3CC', bd=4)
frame.place(relx=0.12, rely=0.12, relheight=0.1, relwidth=0.75)

entry = tk.Entry(frame, font=('Bahnschrift', 12))
entry.place(relx=0, rely=0, relheight=1, relwidth=0.65)

button = tk.Button(frame, text='Get Weather', font=('Bahnschrift', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.68, rely=0, relheight=1, relwidth=0.3)

down_frame = tk.Frame(rex, bg='#6BC1FF', bd=5, relief='groove')
down_frame.place(relx=0.12, rely=0.3, relheight=0.6, relwidth=0.75)

label = tk.Label(down_frame, font=('Courier', 12))
label.place(relx=0, rely=0, relheight=1, relwidth=1)

rex.mainloop()