
from PyQt5 import QtWidgets,uic
from mainWindow import MainWindow
from PyQt5 import QtWidgets
import sys   

                  

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()