import sys
import PyQt5
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Toolbox")

window.move(500,200)
window.setStyleSheet(
    "background-color: #202020;"
)
grid = QGridLayout()

#############################################
groupBoxButtons = QGroupBox("Buttons AND Options")
pushButton = QPushButton("QPushButton")
toolButton = QToolButton()
radioButton = QRadioButton("RadioButton")
checkBox = QCheckBox("CheckBox")
comboBox = QComboBox()
comboBox.addItem("ComboBox")
comboBox.addItem("Item2")
comboBox.addItem("Item3")
fontComboBox = QFontComboBox()

groupButtons = QVBoxLayout()
groupButtons.addWidget(pushButton)
groupButtons.addWidget(toolButton)
groupButtons.addWidget(radioButton)
groupButtons.addWidget(checkBox)
groupButtons.addWidget(comboBox)
groupButtons.addWidget(fontComboBox)

groupBoxButtons.setLayout(groupButtons)

###############################################
groupBoxDate = QGroupBox("Date Time")
dateEdit = QDateEdit()
dateTimeEdit = QDateTimeEdit()
timeEdit = QTimeEdit()
calendarWidget = QCalendarWidget()

groupDate =  QVBoxLayout()
groupDate.addWidget(dateEdit)
groupDate.addWidget(dateTimeEdit)
groupDate.addWidget(timeEdit)
groupDate.addWidget(calendarWidget)
groupBoxDate.setLayout(groupDate)

#################################################

table = QTableWidget()
table.setRowCount(3)
table.setColumnCount(3)
################################################
tabs = QTabWidget()
tab1 = QWidget()
layoutTab1 = QVBoxLayout()
tab1Label = QLabel("You are on first page")
layoutTab1.addWidget(tab1Label)
tab1.setLayout(layoutTab1)

tab2 = QWidget()
layoutTab2 = QVBoxLayout()
tab2Label = QLabel("Welcome on second")
layoutTab2.addWidget(tab2Label)
tab2.setLayout(layoutTab2)
tabs.addTab(tab1, "First")
tabs.addTab(tab2, "Second")
#################################################
groupBoxText = QGroupBox("Text and Labels")
label = QLabel("This is a label")
textEdit = QTextEdit("This is TextEdit")
LCDNumber = QLCDNumber()
LCDNumber.display("420")
lineEdit = QLineEdit()
lineEdit.setPlaceholderText("This is lineEdit")

groupText = QVBoxLayout()
groupText.addWidget(label)
groupText.addWidget(textEdit)
groupText.addWidget(LCDNumber)
groupText.addWidget(lineEdit)
groupBoxText.setLayout(groupText)
###############################################

groupRangeBox = QGroupBox("Range AND Progress")
slider = QSlider(Qt.Horizontal)
spinBox = QSpinBox()
progresBar = QProgressBar()
dial = QDial()
doubleSpinBox = QDoubleSpinBox()

groupRange = QVBoxLayout()
groupRange.addWidget(slider)
groupRange.addWidget(spinBox)
groupRange.addWidget(progresBar)
groupRange.addWidget(doubleSpinBox)
groupRange.addWidget(dial)
groupRangeBox.setLayout(groupRange)

################################################


grid.addWidget(groupBoxButtons,1,0)
grid.addWidget(groupBoxDate,1,1)
grid.addWidget(groupBoxText,2,0)
grid.addWidget(groupRangeBox,2,1)
grid.addWidget(table,3,0)
grid.addWidget(tabs,3,1)



window.show()
window.setLayout(grid)
sys.exit(app.exec())
