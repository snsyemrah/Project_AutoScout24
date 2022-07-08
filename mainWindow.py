
import sys
from PyQt5 import QtWidgets,uic


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Ui/autoscreen.ui', self)
        self.start.clicked.connect(self.Start)
        self.PlateSearch.clicked.connect(self.search_plate)
        self.quit.clicked.connect(self.Quit)

        self.show()

    def Start(self):
        pass

    def Quit(self):
        sys.exit()

    def search_plate(self):
        pass