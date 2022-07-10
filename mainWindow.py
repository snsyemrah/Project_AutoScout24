
import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow
import psycopg2
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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
            self.Price_info.insert(r[2])
            self.Year_info.clear()
            self.Year_info.insert(r[3])
            self.City_info.clear()
            self.City_info.insert(r[4])
            self.plate.clear()
            self.plate.insert(r[5])
            # self.image_label.insert(r[6])

        conn.commit()
        

       
        

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

        self.total.insert("Total: " + str(total[0]))






    def Quit(self):
        sys.exit()

    def search_plate(self):

        driver=webdriver.Chrome()


        url="https://www.centraalbeheer.nl/verzekeringen/autoverzekering/kentekencheck" 
        driver.get(url)
        time.sleep(3)
        # Database'den buraya veri alinacak.
        kenteken = self.plate.text()

        time.sleep(3)

        # driver.find_element(By.XPATH, "i//*[@id="tekst1"]/div[2]/a[1]")
        # driver.find_element(By.XPATH, '//*[@id="tekst1"]/div[2]/a[1]').click()
        # //*[@id="tekst1"]/div[2]/a[1]
        time.sleep(3)

        kenteken_ = driver.find_element(By.CLASS_NAME, "input-kenteken__input")

        kenteken_.send_keys(kenteken)
        time.sleep(5)
        driver.find_element(By.ID, "kenteken-button").click()