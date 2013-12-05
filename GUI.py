

import sys
from PyQt4 import QtGui, QtCore


    
#------------------------------------GUI--------------------------------------

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class GUI(QtGui.QMainWindow):
    
    def __init__(self):
        super(GUI, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        MainWindow = QtGui.QWidget(self)
        self.setCentralWidget(MainWindow)
            
        
        
        
        hud = QtGui.QWidget(MainWindow)
        hud.setGeometry(QtCore.QRect(0, 0, 530, 150))         
        hudlayout = QtGui.QGridLayout()
        
                
        
        #Teclas Inferiores
        tecla1 = QtGui.QPushButton("", self)       
        tecla1.setGeometry(10,200,80,300)
        tecla1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        tecla2 = QtGui.QPushButton("", self)    
        tecla2.setGeometry(90,200,80,300)
        tecla2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        tecla3 = QtGui.QPushButton("", self)        
        tecla3.setGeometry(170,200,80,300)
        tecla3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        tecla4 = QtGui.QPushButton("", self)        
        tecla4.setGeometry(250,200,80,300)
        tecla4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        tecla5 = QtGui.QPushButton("", self)        
        tecla5.setGeometry(330,200,80,300)
        tecla5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        tecla6 = QtGui.QPushButton("", self)        
        tecla6.setGeometry(410,200,80,300)
        tecla6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        tecla7 = QtGui.QPushButton("", self)        
        tecla7.setGeometry(490,200,80,300)
        tecla7.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))                    
        
        #Teclas Superiores
        tecla8 = QtGui.QPushButton("", self)        
        tecla8.setGeometry(70,200,40,175)
        tecla8.setStyleSheet(_fromUtf8("background-color: rgb(10, 10, 10);"))
        tecla9 = QtGui.QPushButton("", self)        
        tecla9.setGeometry(150,200,40,175)
        tecla9.setStyleSheet(_fromUtf8("background-color: rgb(10, 10, 10);"))
        tecla10 = QtGui.QPushButton("", self)        
        tecla10.setGeometry(310,200,40,175)
        tecla10.setStyleSheet(_fromUtf8("background-color: rgb(10, 10, 10);"))
        tecla11 = QtGui.QPushButton("", self)        
        tecla11.setGeometry(390,200,40,175)
        tecla11.setStyleSheet(_fromUtf8("background-color: rgb(10, 10, 10);"))
        tecla12 = QtGui.QPushButton("", self)        
        tecla12.setGeometry(470,200,40,175)
        tecla12.setStyleSheet(_fromUtf8("background-color: rgb(10, 10, 10);"))
        
        #Slider de Volume
        slider = QtGui.QSlider(self)
        slider.setOrientation(QtCore.Qt.Horizontal)  
        slider.setMinimumSize(100,100)
        slider.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        slider.setSliderPosition(50)
        
        volume = QtGui.QLabel(self)
        volume.setText("Volume")
        volume.setAlignment(QtCore.Qt.AlignCenter)
                              
                      
        #LCD
        lcd = QtGui.QLCDNumber(self)
        lcd.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        lcd.setMinimumSize(300,100)
        lcdf = QtGui.QLabel(self)
        lcdf.setText("Frequencia")
        lcdf.setAlignment(QtCore.Qt.AlignCenter)
         
        
        #Sizers              
        hudlayout.setSpacing(30)
        hudlayout.addWidget(slider, 0,0,1,1, alignment=QtCore.Qt.AlignCenter)
        hudlayout.addWidget(volume, 1,0,1,1, alignment=QtCore.Qt.AlignCenter)
        hudlayout.addWidget(lcd, 0,1,1,1, alignment=QtCore.Qt.AlignCenter)
        hudlayout.addWidget(lcdf, 1,1,1,1, alignment=QtCore.Qt.AlignCenter)                     
        hud.setLayout(hudlayout)        
        
    
        
        #bindings
        tecla1.clicked.connect(self.buttonClicked)            
        tecla2.clicked.connect(self.buttonClicked)
        
        
        #MainWindow
        self.statusBar()        
        self.setFixedSize(580,530)
        self.setWindowTitle('Sintetizador de Audio')
        self.show()
  
       
        
    def buttonClicked(self):           
                
        sender = self.sender()                                  
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
def main():    

    app = QtGui.QApplication(sys.argv)
    ex = GUI()       
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
