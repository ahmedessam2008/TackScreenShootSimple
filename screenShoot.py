import sys
import os
import re
from os import path

# import PyQt5 modules
from PyQt5.QtGui import *
# from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from PyQt5.QtCore import *
# from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QBoxLayout, QTextEdit, QCompleter
from PyQt5.uic import loadUiType

# For load on save Gui
FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"screenShot.ui"))

# Intiate Ui File
class MainApp(QMainWindow , FORM_CLASS):
  def __init__(self, parent=None):
    # pafy.set_api_key("AIzaSyBVMRM6hTFiSJL5K5yCSpovgn82g2W55FU")
    super().__init__(parent)
    QMainWindow.__init__(self)
    self.setupUi(self)
    self.Handle_Ui()
    self.Handle_Buttons()
    
  def Handle_Ui(self):
    self.setWindowTitle("PyDownloader")
    self.setFixedSize(800, 411)
    
  def Handle_Buttons(self):
    # For Tack Screen
    self.pushButton.clicked.connect(self.Download)
    
    
    
    
  # main method to call our app
if __name__ == '__main__':
 
  # create app
  App = QApplication(sys.argv)

  # create the instance of our window
  window = MainApp()

  window.show()
  
  # start the app
  sys.exit(App.exec())