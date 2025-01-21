from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QPushButton, QGridLayout
import random

# major settings and objects 
App = QApplication([])
Main_Window = QWidget()
Main_Window.setWindowTitle('Calculator App prototype')
Main_Window.resize(400, 600)

# creating all the neccerary objects & widgets
wordBox = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',          
'0', '.', '+', '='           
]
row = 0
coloumn = 0
grid = QGridLayout()
text_box = QLineEdit()
clear = QPushButton('C')
delete = QPushButton('✂')

def CalcFunc():
    button = App.sender() # This is to seperate events 
    txt = button.text()   
    if txt == 'C':
      x = text_box.clear()
      text_box.setText(x)
    elif txt == '✂' :
        cut = text_box.text()
        text_box.setText(cut[:-1])
    elif txt == '=' :
        try:
         res = text_box.text()
         text_box.setText(str(eval(res)))
        except Exception as e:
            text_box.setText('Error!')
    else:    
        tx = text_box.text()
        text_box.setText(tx + txt)
        
for button_text in wordBox:
    button = QPushButton(button_text)
    button.clicked.connect(CalcFunc)
    grid.addWidget(button, row, coloumn)
    coloumn += 1
    if coloumn > 3:
        coloumn = 0
        row += 1 

def eraser():
    text_box.clear()
def backspace():
    pen = text_box.text()
    text_box.setText(pen[:-1])







clear.clicked.connect(eraser)
delete.clicked.connect(backspace)

# design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()       
button_row.addWidget(clear)
button_row.addWidget(delete)
    
master_layout.addLayout(button_row)       
Main_Window.setLayout(master_layout) 

# to run and show the app
Main_Window.show()
App.exec_()