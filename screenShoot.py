import sys
import os
import time
from os import path
import PIL.ImageGrab
import pyautogui

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
    # self.setWindowTitle("Take")
    self.setFixedSize(123, 140)
    
  def Handle_Buttons(self):
    # For Tack Screen
    self.pushButton.clicked.connect(self.Take)
  
  def Area(self):
    rectang = pyautogui.position()
  
  def Take(self):
    self.hide()
    time.sleep(.5)
    image = PIL.ImageGrab.grab()
    self.show()
    image.show()
    
    # self.close()
   
   
   
    
  # main method to call our app
if __name__ == '__main__':
 
  # create app
  App = QApplication(sys.argv)

  # create the instance of our window
  window = MainApp()

  window.show()
  
  # start the app
  sys.exit(App.exec())