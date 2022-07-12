import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow
import psycopg2
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PyQt5.QtGui import QImage, QPixmap
import math, json
import datetime
from datetime import datetime



class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Ui/autoscreen.ui', self)
        self.start.clicked.connect(self.Start)
        self.PlateSearch.clicked.connect(self.search_plate)
        self.quit.clicked.connect(self.Quit)
        self.table_autos.setColumnWidth(0,370)
        self.table_autos.clicked.connect(self.Clicked)
        
        self.show()


    def Clicked(self):
        conn = psycopg2.connect(host= 'localhost',database = 'autoscout24',user = 'postgres',password = '1234')
        cur = conn.cursor()


        index=(self.table_autos.selectionModel().currentIndex())
        value=index.row()+1

        cur.execute("select model,kilometer,city,year,price,plate,image from autos where id = %s;",(value,))
        Student = cur.fetchall()
        for r in Student:
            self.model_info.clear()
            self.model_info.insert(r[0])
            self.kilometer_info.clear()
            self.kilometer_info.insert(r[1])
            self.Price_info.clear()
            self.Price_info.insert(r[4] + " €")
            self.Year_info.clear()
            self.Year_info.insert(r[3])
            
            self.City_info.clear()
            self.City_info.insert(r[2])
            
            self.plate.clear()
            self.plate.insert(r[5])
            self.image_label.clear()
            # self.image_label.picture(r[6])
            
            image = QImage()
       
            image.loadFromData(requests.get(r[6]).content)
            self.image_label.setPixmap(QPixmap(image))
            self.image_label.show()

            city_name = self.City_info.text()
            self.city.clear()
            self.city.insert(city_name)
          

        # ===================================////////////////////================================
        city_name = self.city.text()
        # city_name = self.city.clear()
        country_code = "NL"
        api_key = "bbdaa09e0842234cc242fc5186627b70"
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&country_code={country_code}&mode=json&appid={api_key}"
        response = requests.get(url).json()
        
        date_list = []
        temp_max_list = []
        temp_min_list = []
        icon_list = []
        description_list = []

        for i in response['list'][:24:8]:
            temp_max = math.floor(i['main']['temp_max']-273)
            temp_max_list.append(temp_max)
            # print(temp_max)
            temp_min = math.floor(i['main']['temp_min']-273)
            temp_min_list.append(temp_min)
            # print(temp_min)
            d = datetime.strptime(i['dt_txt'],"%Y-%m-%d %H:%M:%S")
            date = f"{d.day}.{d.month}.{d.year}"
            date_list.append(date)
            # print(date_list)
            icon = i['weather'][0]['icon']  
            icon_list.append(icon)    
            
             
            # print(icon_list)
            description = i['weather'][0]['description']
            description_list.append(description)
            # print(description_list)

    # =======================To write the datas to json file==========================

            filename = 'weather.json'          #use the file extension .json
            with open(filename, 'w+') as file_object:  #open the file in write mode
                json.dump(response, file_object)

                    
 
        self.city.setText(city_name)


        

        first_day = str(date_list[0])+"\n"+"Max: "+str(temp_max_list[0])+"°C"+"\n"+"Min: "+str(temp_min_list[0])+"°C"
        new_icon = f"https://openweathermap.org/img/wn/{icon_list[0]}@2x.png"
        self.label_10.setText(first_day)
        image = QImage()
        image.loadFromData(requests.get(new_icon).content)
        self.image_label_2.setPixmap(QPixmap(image))
        self.image_label_2.show()
        # self.label_11.setText(icon_list[0])
        self.label_12.setText(description_list[0])
    

        second_day = str(date_list[1])+"\n"+"Max: "+str(temp_max_list[1])+"°C"+"\n"+"Min: "+str(temp_min_list[1])+"°C"
        new_icon_2 = f"https://openweathermap.org/img/wn/{icon_list[1]}@2x.png"
        self.label_11.setText(second_day)
        image = QImage()
        image.loadFromData(requests.get(new_icon_2).content)
        self.image_label_3.setPixmap(QPixmap(image))
        self.image_label_3.show()
        # self.image_label_3.setText(new_icon_2)
        self.label_13.setText(description_list[1])

        third_day = str(date_list[2])+"\n"+"Max: "+str(temp_max_list[2])+"°C"+"\n"+"Min: "+str(temp_min_list[2])+"°C"
        new_icon_3 = f"https://openweathermap.org/img/wn/{icon_list[2]}@2x.png"
        self.label_14.setText(third_day)
        image = QImage()
        image.loadFromData(requests.get(new_icon_3).content)
        self.image_label_4.setPixmap(QPixmap(image))
        self.image_label_4.show()
        # self.image_label_4.setText(new_icon_3)
        self.label_15.setText(description_list[2])
        conn.commit()
        
# ======================Start-Button========================

    def Start(self):
        conn = psycopg2.connect(host= 'localhost',database = 'autoscout24',user = 'postgres',password = '1234')
        cur = conn.cursor()
  
        qry = "select model,year,plate from autos"
        cur.execute(qry)
        auto = cur.fetchall()
    
        self.table_autos.setRowCount(len(auto))
        row = 0
        for i in auto:
            self.table_autos.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))
            self.table_autos.setItem(row, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.table_autos.setItem(row, 2, QtWidgets.QTableWidgetItem(i[2]))
            row = row+1

        conn.commit()

    
        qry = "select id from autos order by id desc;"
        cur.execute(qry)
        total = cur.fetchone()

        self.total.insert(str(total[0]))

# ======================OpenWeather&API========================
        city_name = "Amsterdam"
        country_code = "NL"
        api_key = "bbdaa09e0842234cc242fc5186627b70"
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&country_code={country_code}&mode=json&appid={api_key}"
        response = requests.get(url).json()
        
        date_list = []
        temp_max_list = []
        temp_min_list = []
        icon_list = []
        description_list = []

        for i in response['list'][:24:8]:
            temp_max = math.floor(i['main']['temp_max']-273)
            temp_max_list.append(temp_max)
            # print(temp_max)
            temp_min = math.floor(i['main']['temp_min']-273)
            temp_min_list.append(temp_min)
            # print(temp_min)
            d = datetime.strptime(i['dt_txt'],"%Y-%m-%d %H:%M:%S")
            date = f"{d.day}.{d.month}.{d.year}"
            date_list.append(date)
            # print(date_list)
            icon = i['weather'][0]['icon']  
            icon_list.append(icon)    
            
             
            # print(icon_list)
            description = i['weather'][0]['description']
            description_list.append(description)
            # print(description_list)

    # =======================To write the datas to json file==========================

            filename = 'weather.json'          #use the file extension .json
            with open(filename, 'w+') as file_object:  #open the file in write mode
                json.dump(response, file_object)

                    
 
        self.city.setText(city_name)


        

        first_day = str(date_list[0])+"\n"+"Max: "+str(temp_max_list[0])+"°C"+"\n"+"Min: "+str(temp_min_list[0])+"°C"
        new_icon = f"https://openweathermap.org/img/wn/{icon_list[0]}@2x.png"
        self.label_10.setText(first_day)
        image = QImage()
        image.loadFromData(requests.get(new_icon).content)
        self.image_label_2.setPixmap(QPixmap(image))
        self.image_label_2.show()
        # self.label_11.setText(icon_list[0])
        self.label_12.setText(description_list[0])
    

        second_day = str(date_list[1])+"\n"+"Max: "+str(temp_max_list[1])+"°C"+"\n"+"Min: "+str(temp_min_list[1])+"°C"
        new_icon_2 = f"https://openweathermap.org/img/wn/{icon_list[1]}@2x.png"
        self.label_11.setText(second_day)
        image = QImage()
        image.loadFromData(requests.get(new_icon_2).content)
        self.image_label_3.setPixmap(QPixmap(image))
        self.image_label_3.show()
        # self.image_label_3.setText(new_icon_2)
        self.label_13.setText(description_list[1])

        third_day = str(date_list[2])+"\n"+"Max: "+str(temp_max_list[2])+"°C"+"\n"+"Min: "+str(temp_min_list[2])+"°C"
        new_icon_3 = f"https://openweathermap.org/img/wn/{icon_list[2]}@2x.png"
        self.label_14.setText(third_day)
        image = QImage()
        image.loadFromData(requests.get(new_icon_3).content)
        self.image_label_4.setPixmap(QPixmap(image))
        self.image_label_4.show()
        # self.image_label_4.setText(new_icon_3)
        self.label_15.setText(description_list[2])

    

    def search_plate(self):
        driver=webdriver.Chrome()
        url="https://www.centraalbeheer.nl/verzekeringen/autoverzekering/kentekencheck" 
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        kenteken = self.plate.text()
        time.sleep(3)
        adres=driver.find_element(By.ID, 'kenteken-input')
        driver.execute_script("arguments[0].scrollIntoView();",adres)
        time.sleep(3)
        kenteken_ = driver.find_element(By.CLASS_NAME, "input-kenteken__input")
        
        kenteken_.send_keys(kenteken)
        time.sleep(3)
        driver.find_element(By.ID, "kenteken-button").click()
        time.sleep(45)

    def Quit(self):
        sys.exit()