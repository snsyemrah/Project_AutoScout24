
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from mainWindow import MainWindow
import sys   

                  

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()