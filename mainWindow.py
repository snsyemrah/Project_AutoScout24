
import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow
import psycopg2


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Ui/autoscreen.ui', self)
        self.start.clicked.connect(self.Start)
        self.PlateSearch.clicked.connect(self.search_plate)
        self.quit.clicked.connect(self.Quit)

        self.show()

    def Start(self):
        self.total()
        conn = psycopg2.connect(host= 'localhost',database = 'autoscout24',user = 'postgres',password = '1234')
        cur = conn.cursor()
        

       
        qry = "select model,year,plate from autos"
        cur.execute(qry)
        auto = list(cur.fetchone())
        print(type(auto))
        print(auto)
    
   
        row1 = 0
        for i in auto[0]:
            self.table_autos(row1, 0, QtWidgets.QTableWidgetItem(i[0]))
            row1 = row1+1
        
        row2 = 0
        for i in auto[1]:
            self.table_autos(row2, 1, QtWidgets.QTableWidgetItem(i[1]))
            row2 = row2+1

        row3 = 0
        for i in auto[2]:
            self.table_autos(row3, 2, QtWidgets.QTableWidgetItem(i[2]))
            row3 = row3+1


        conn.commit()

    def total(self):
        conn = psycopg2.connect(host= 'localhost',database = 'autoscout24',user = 'postgres',password = '1234')
        cur = conn.cursor()
        qry = "select id from autos order by id desc"
        cur.execute(qry)
        total = cur.fetchone()
        print(total)




    def Quit(self):
        sys.exit()

    def search_plate(self):
        pass