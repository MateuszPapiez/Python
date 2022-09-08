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
from flutter import checked
import requests


SURVEY_LIST_URL="http://127.0.0.1:5555/get-surveys"
SURVEY_QUESTIONS="http://127.0.0.1:5555/surveys"

app=None
window=None

class QuestionPanel (QWidget):

   def __init__(self,question,parent,callback=None):
      super().__init__(parent)
      self.Label=QLabel(question['pytanie'],self)
      self.Label.setGeometry(0,0,120,20)
      self.Label.setStyleSheet("QLabel { color : blue; }")
      self.C1=QCheckBox(self)
      self.C1.stateChanged.connect(lambda : self.uncheck("A"))
      self.C1.setGeometry(0,20,120,20)
      self.C1.setText(question['odpowiedzi'][0]['odpowiedz'])
      

      self.C2=QCheckBox(self)
      self.C2.stateChanged.connect(lambda : self.uncheck("B"))
      self.C2.setGeometry(0,40,120,20)
      self.C2.setText(question['odpowiedzi'][1]['odpowiedz'])
      self.C3=QCheckBox(self)
      self.C3.stateChanged.connect(lambda : self.uncheck("C"))
      self.C3.setGeometry(0,60,120,20)
      self.C3.setText(question['odpowiedzi'][2]['odpowiedz'])
      
   
   uncheck_running=False
   
   def uncheck(self,e):
      if self.uncheck_running:
         return
      self.uncheck_running=True
      if e=="A":
         self.C1.setCheckState(1)
         self.C2.setCheckState(0)
         self.C3.setCheckState(0)
      if e=="B":
         self.C2.setCheckState(1)
         self.C1.setCheckState(0)
         self.C3.setCheckState(0)
      if e=="C":
         self.C3.setCheckState(1)
         self.C1.setCheckState(0)
         self.C2.setCheckState(0)
      self.uncheck_running=False
      

def button(survey_name,parent,go_to_survey_action):
   button1 = QPushButton(parent)
   button1.setText(survey_name)
   button1.setStyleSheet("QPushButton{border-radius:5px;background-color:#C0392B}")
   button1.clicked.connect(lambda : go_to_survey_action(survey_name))
   return button1


   

class Surveywindow (QWidget):

  def __init__(self,name):

   
   survey=requests.get(SURVEY_QUESTIONS+"/"+name).json()
   survey_panel=QWidget(window)
   y=0

   survey_panel.setGeometry(0,0,800,400)
   survey_panel.setStyleSheet("QWidget { background-color : grey; color : white; }")
      
   for question in survey:
         
      panel=QuestionPanel(question,survey_panel)
      panel.setGeometry(300,y,250,300)
      panel.show()
      y+=100
      
      
   survey_panel.show()


def 

def init_window():
   global app
   global window
   app = QApplication(sys.argv)
   window = QWidget()

   
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