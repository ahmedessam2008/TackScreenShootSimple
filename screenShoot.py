import sys
from time import sleep, strftime
from os import path , system
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

# For Convert to exe file 
from screenDesign import Ui_MainWindow

# For load on save Gui
# FORM_CLASS,_= loadUiType(path.join(path.dirname(__file__),"screenDesign.ui"))

# Intiate Ui File
class MainApp(QMainWindow , Ui_MainWindow):
  def __init__(self, parent=None):
    # pafy.set_api_key("AIzaSyBVMRM6hTFiSJL5K5yCSpovgn82g2W55FU")
    super().__init__(parent)
    QMainWindow.__init__(self)
    self.setupUi(self)
    self.Handle_Ui()
    self.Handle_Buttons()
    
  def Handle_Ui(self):
    # self.setWindowTitle("Take")
    self.setFixedSize(430, 120)
    
  def Handle_Buttons(self):
    # For Tack Screen
    self.pushButton.clicked.connect(self.Take)
  
  def Take(self):
    self.hide()
    sleep(.5)
    image = PIL.ImageGrab.grab()
    self.show()
    save_location = r"C:\Users\brave\Desktop\{}.jpg".format(strftime("%d%b%Y%H%M%S"))
    image.save(save_location)
    system(save_location)
    
   
    
  # main method to call our app
if __name__ == '__main__':
 
  # create app
  App = QApplication(sys.argv)

  # create the instance of our window
  window = MainApp()

  window.show()
  
  # start the app
  sys.exit(App.exec())