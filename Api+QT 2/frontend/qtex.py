from modulefinder import IMPORT_NAME
from pickle import NONE
import sys
from tkinter import Y
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QIcon
import requests


SURVEY_LIST_URL="http://127.0.0.1:5555/get-surveys"
SURVEY_QUESTIONS="http://127.0.0.1:5555/surveys"

app=None
window=None


def button(survey_name,parent,go_to_survey_action):
   button1 = QPushButton(parent)
   button1.setText(survey_name)
   button1.setStyleSheet("QPushButton{border-radius:5px;background-color:#C0392B}")
   button1.clicked.connect(lambda : go_to_survey_action(survey_name))
   return button1

def question_panel(question,parent,callback=None):
   panel= QWidget(parent)
   Label=QLabel(question['pytanie'],panel)
   Label.setGeometry(0,0,120,80)
   Label.setStyleSheet("QLabel { background-color : red; color : blue; }")
   C1=QCheckBox(panel)
   C2=QCheckBox(panel)
   C3=QCheckBox(panel)
   return panel



def survey_window(name):
   survey=requests.get(SURVEY_QUESTIONS+"/"+name).json()
   survey_panel=QWidget(window)
   y=0

   survey_panel.setGeometry(0,0,800,400)
   survey_panel.setStyleSheet("QWidget { background-color : grey; color : white; }")

   for question in survey:
      
      panel=question_panel(question,survey_panel)
      panel.setGeometry(300,y,120,300)
      panel.show()
      y+=100
      
   survey_panel.show()

def init_window():
   global app
   global window
   app = QApplication(sys.argv)
   window = QWidget()
   #window.setLayout(QGridLayout())
   
   window.setGeometry(800,200,750,400)
   window.setWindowTitle("Ankiety")
   
   
   surveys_resp=requests.get(SURVEY_LIST_URL)
   surveys_names=surveys_resp.json()
   button_y=50
   for name in surveys_names:
      survey_button=button(name,window,survey_window)
      survey_button.setGeometry(300,button_y,150,80)
      button_y+=100



   window.show()
   sys.exit(app.exec_()) 

   
if __name__ == '__main__':
   init_window()