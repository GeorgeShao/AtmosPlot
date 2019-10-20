# from geolocator import geolocator
from latlong import returnlatlong
import ftp_functions as FTP
import parse_data
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

DATA = list()
gas_year_month = [] 
list_of_gases = ["C2H2","C2H6","CCl2F2","CCl3F","CCl4","CF4","CH3Cl","CH4","CHF2Cl","ClONO2","CO","COF2","H2CO","H2O2","H2O","HCl","HCN","HCOOH","HF","HNO3","HO2NO2","N2","N2O5","N2O","NO2","O3","OCS","P","SF6"]

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('SCISAT Data Interpreter')
        self.textfield1 = QLabel()
        self.dropdown1 = QComboBox()
        self.textfield2 = QLabel()
        self.dropdown2 = QComboBox()
        self.textfield3 = QLabel()
        self.dropdown3 = QComboBox()
        self.textfield4 = QLabel()
        self.dropdown4 = QComboBox()
        self.button = QPushButton()

        for each_gas in list_of_gases:
            self.dropdown1.addItem(each_gas)
            self.dropdown2.addItem(each_gas)
        
        for each_year in range(2004,2011):
            self.dropdown3.addItem(str(each_year))
        
        for each_month in range(1,10):
            self.dropdown4.addItem('0' + str(each_month))
        
        for each_month in range(10,13):
            self.dropdown4.addItem(str(each_month))
        
        self.textfield1.setText('Graph in purple/pink (left y-axis)')
        self.textfield2.setText('Graph in yellow/green (right y-axis)')
        self.textfield3.setText("Year")
        self.textfield4.setText("Month")
        self.button.setText("Graph")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textfield1)
        self.layout.addWidget(self.dropdown1)
        self.layout.addWidget(self.textfield2)
        self.layout.addWidget(self.dropdown2)
        self.layout.addWidget(self.textfield3)
        self.layout.addWidget(self.dropdown3)
        self.layout.addWidget(self.textfield4)
        self.layout.addWidget(self.dropdown4)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        global DATA, gas_year_month
        
        year_month = str(self.dropdown3.currentText()) + "-" + str(self.dropdown4.currentText())
        array = FTP.ls(year_month)
        gas_year_month = [str(self.dropdown1.currentText()), str(self.dropdown2.currentText()), year_month]
        for i in array:
            print("Fetching data: " + i)
            latlong = returnlatlong(year_month, i)
            ozone_data, acid_data = parse_data.parse_csv(year_month, i, str(self.dropdown1.currentText()), str(self.dropdown2.currentText()))
            DATA.append(ozone_data)
            DATA.append(acid_data)
            DATA.append(latlong)
        
        app.quit()


print(DATA)

app = QApplication(sys.argv)

widget = MyWidget()
widget.resize(400, 200)
widget.show()

app.exec_()