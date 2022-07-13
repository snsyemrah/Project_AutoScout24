import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class About(QMainWindow):
    def __init__(self):
        super(About, self).__init__()
        uic.loadUi('Ui/about.ui', self)
        self.pushButton_4.clicked.connect(self.emrah)
        self.pushButton_5.clicked.connect(self.burhan)
        self.pushButton_2.clicked.connect(self.aliosman)
        self.pushButton_3.clicked.connect(self.serkan)
        
        self.show()

    def emrah(self):
        driver=webdriver.Chrome()
        url="https://github.com/snsyemrah" 
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        driver.close()

    def burhan(self):
        driver=webdriver.Chrome()
        url="https://github.com/brhnstr" 
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        driver.close()

    def aliosman(self):
        driver=webdriver.Chrome()
        url="https://github.com/alosoz" 
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        driver.close()
    
    def serkan(self):
        driver=webdriver.Chrome()
        url="https://github.com/SerkanKaluc" 
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        driver.close()
