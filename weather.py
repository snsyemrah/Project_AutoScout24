from time import strptime
import requests
from tkinter import *
import math
import json
import datetime as dt
from datetime import date
from datetime import datetime
# import mainWindow 


# city_name = mainWindow.Clicked()

city_name = "Amsterdam,NL"
api_key = "bbdaa09e0842234cc242fc5186627b70"

def get_weather(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&mode=json&appid={api_key}"

    response = requests.get(url).json()
    
    
    temp_max_list = []
    temp_min_list = []
    icon_list = []
    description_list = []
    date_list = []

    for i in response['list'][:24:8]:
        # dt = datetime.combine(date.today(), datetime.min.time())
        # print(math.floor(i['main']['temp_max']-273))
        temp_max = math.floor(i['main']['temp_max']-273)
        temp_max_list.append(temp_max)

        # print(math.floor(i['main']['temp_min']-273))
        temp_min = math.floor(i['main']['temp_min']-273)
        temp_min_list.append(temp_min)

        d = datetime.strptime(i['dt_txt'],"%Y-%m-%d %H:%M:%S")
        # print(f"{d.day}.{d.month}.{d.year}")
        date = f"{d.day}.{d.month}.{d.year}"
        date_list.append(date)
        
        
        # print(i['weather'][0]['icon'])
        icon = i['weather'][0]['icon']
        icon_list.append(icon)

        # print(i['weather'][0]['description'])
        description = i['weather'][0]['description']
        description_list.append(description)


        filename = 'weather.json'          #use the file extension .json
        with open(filename, 'w+') as file_object:  #open the file in write mode
            json.dump(response, file_object)
    # print(temp_max_list)
    # print(temp_min_list)
    # print(date_list)
    # print(icon_list)
    # print(description_list)
    #     return {
    #     'temp_max': temp_max,
    #     'temp_min': temp_min,
    #     'date': date,
    #     'icon': icon,
    #     'description' : description

    # }
    
    
get_weather(api_key,city_name)
    
    
    





# Acilir pencere
# root = Tk()
# root.geometry("300x300")
# root.title(f'{city_name[:-3]} Weather')

# def display_city_name(city):
#     city_label = Label(root, text=f"{city_name[:-3]}")
#     city_label.config(font=("Consolas", 28))
#     city_label.pack(side='top')

# def display_stats(weather):
#     temp = Label(root, text=f"Temperature: {weather['temp']} °C")
#     feels_like = Label(root, text=f"Feels Like: {weather['feels_like']} °C")
#     humidity = Label(root, text=f"Humidity: {weather['humidity']} %")

#     temp.config(font=("Consolas", 22))
#     feels_like.config(font=("Consolas", 16))
#     humidity.config(font=("Consolas", 16))

#     temp.pack(side='top')
#     feels_like.pack(side='top')
#     humidity.pack(side='top')


# display_city_name(city_name)
# display_stats(weather)

# mainloop()


