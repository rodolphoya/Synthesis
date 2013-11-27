# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:01:35 2013

@author: WIN7
"""
from audiolazy import *
import pygame
from pygame.locals import * 
import pygame.midi
from pygame.locals import *

nota = 0 
anterior = 0
freq = 0
rate = 44100
s,Hz=sHz(rate)
ms = 1e-3*s
player = AudioIO()

pygame.init()
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
i = pygame.midi.Input( input_id )

#dicionario que relaciona as o numero das teclas do teclado MIDI com
#a frequencia correspondente de sua nota musical
DFreq = {36 : 32.703,     
37 : 34.648,
38 : 36.708,
39 : 38.891,
40 : 41.204,
41 : 43.655,
42 : 46.250,
43 : 49.000,
44 : 51.915,
45 : 55.000,
46 : 58.270,
47 : 61.735,
48 : 65.406,
49 : 69.296,
50 : 73.416,
51 : 77.782,
52 : 82.407,
53 : 87.31,
54 : 92.50,
55 : 98.00,
56 : 103.83,
57 : 110.00,
58 : 116.54,
59 : 123.47,
60 : 131.00,
61 : 138.59,
62 : 146.83,
63 : 155.56,
64 : 164.81,
65 : 174.61,
66 : 185.00,
67 : 196.00,
68 : 207.55,
69 : 220.00,
70 : 233.08,
71 : 246.94,
72 : 261.63,
73 : 277.18,
74 : 293.67,
75 : 311.13,
76 : 329.63,
77 : 349.23,
78 : 369.99,
79 : 392.00,
80 : 415.30,
81 : 440.00,
82 : 466.16, 
83 : 493.88,
84 : 523.25,
85 : 554.37,
86 : 587.33,
87 : 622.25,
88 : 659.26,
89 : 698.46,
90 : 739.99,
91 : 783.99,
92 : 830.61,
93 : 880.00,
94 : 932.33,
95 : 987.77,
96 : 1046.50,
    }

#GUI

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(608, 595)
        MainWindow.setMaximumSize(QtCore.QSize(1443, 921))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graficoplot = Qwt5.QwtPlot(self.centralwidget)
        self.graficoplot.setGeometry(QtCore.QRect(143, 21, 441, 231))
        self.graficoplot.setProperty("propertiesDocument", _fromUtf8(""))
        self.graficoplot.setObjectName(_fromUtf8("graficoplot"))
        self.tecla1 = QtGui.QPushButton(self.centralwidget)
        self.tecla1.setGeometry(QtCore.QRect(22, 279, 80, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla1.sizePolicy().hasHeightForWidth())
        self.tecla1.setSizePolicy(sizePolicy)
        self.tecla1.setMinimumSize(QtCore.QSize(80, 300))
        self.tecla1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        self.tecla1.setText(_fromUtf8(""))
        self.tecla1.setCheckable(False)
        self.tecla1.setAutoDefault(False)
        self.tecla1.setDefault(False)
        self.tecla1.setFlat(False)
        self.tecla1.setObjectName(_fromUtf8("tecla1"))
        self.tecla2 = QtGui.QPushButton(self.centralwidget)
        self.tecla2.setGeometry(QtCore.QRect(103, 279, 80, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla2.sizePolicy().hasHeightForWidth())
        self.tecla2.setSizePolicy(sizePolicy)
        self.tecla2.setMinimumSize(QtCore.QSize(80, 300))
        self.tecla2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        self.tecla2.setText(_fromUtf8(""))
        self.tecla2.setCheckable(False)
        self.tecla2.setAutoDefault(False)
        self.tecla2.setDefault(False)
        self.tecla2.setFlat(False)
        self.tecla2.setObjectName(_fromUtf8("tecla2"))
        self.tecla3 = QtGui.QPushButton(self.centralwidget)
        self.tecla3.setGeometry(QtCore.QRect(184, 279, 80, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla3.sizePolicy().hasHeightForWidth())
        self.tecla3.setSizePolicy(sizePolicy)
        self.tecla3.setMinimumSize(QtCore.QSize(80, 300))
        self.tecla3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        self.tecla3.setText(_fromUtf8(""))
        self.tecla3.setCheckable(False)
        self.tecla3.setAutoDefault(False)
        self.tecla3.setDefault(False)
        self.tecla3.setFlat(False)
        self.tecla3.setObjectName(_fromUtf8("tecla3"))
        self.tecla6 = QtGui.QPushButton(self.centralwidget)
        self.tecla6.setGeometry(QtCore.QRect(427, 279, 80, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla6.sizePolicy().hasHeightForWidth())
        self.tecla6.setSizePolicy(sizePolicy)
        self.tecla6.setMinimumSize(QtCore.QSize(80, 300))
        self.tecla6.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        self.tecla6.setText(_fromUtf8(""))
        self.tecla6.setCheckable(False)
        self.tecla6.setAutoDefault(False)
        self.tecla6.setDefault(False)
        self.tecla6.setFlat(False)
        self.tecla6.setObjectName(_fromUtf8("tecla6"))
        self.tecla4 = QtGui.QPushButton(self.centralwidget)
        self.tecla4.setGeometry(QtCore.QRect(265, 279, 80, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla4.sizePolicy().hasHeightForWidth())
        self.tecla4.setSizePolicy(sizePolicy)
        self.tecla4.setMinimumSize(QtCore.QSize(80, 300))
        self.tecla4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        self.tecla4.setText(_fromUtf8(""))
        self.tecla4.setCheckable(False)
        self.tecla4.setAutoDefault(False)
        self.tecla4.setDefault(False)
        self.tecla4.setFlat(False)
        self.tecla4.setObjectName(_fromUtf8("tecla4"))
        self.tecla7 = QtGui.QPushButton(self.centralwidget)
        self.tecla7.setGeometry(QtCore.QRect(508, 279, 80, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla7.sizePolicy().hasHeightForWidth())
        self.tecla7.setSizePolicy(sizePolicy)
        self.tecla7.setMinimumSize(QtCore.QSize(80, 300))
        self.tecla7.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        self.tecla7.setText(_fromUtf8(""))
        self.tecla7.setCheckable(False)
        self.tecla7.setAutoDefault(False)
        self.tecla7.setDefault(False)
        self.tecla7.setFlat(False)
        self.tecla7.setObjectName(_fromUtf8("tecla7"))
        self.tecla5 = QtGui.QPushButton(self.centralwidget)
        self.tecla5.setGeometry(QtCore.QRect(346, 279, 80, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla5.sizePolicy().hasHeightForWidth())
        self.tecla5.setSizePolicy(sizePolicy)
        self.tecla5.setMinimumSize(QtCore.QSize(80, 300))
        self.tecla5.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 245);"))
        self.tecla5.setText(_fromUtf8(""))
        self.tecla5.setCheckable(False)
        self.tecla5.setAutoDefault(False)
        self.tecla5.setDefault(False)
        self.tecla5.setFlat(False)
        self.tecla5.setObjectName(_fromUtf8("tecla5"))
        self.tecla8 = QtGui.QPushButton(self.centralwidget)
        self.tecla8.setGeometry(QtCore.QRect(80, 270, 40, 170))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla8.sizePolicy().hasHeightForWidth())
        self.tecla8.setSizePolicy(sizePolicy)
        self.tecla8.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.tecla8.setText(_fromUtf8(""))
        self.tecla8.setAutoDefault(False)
        self.tecla8.setFlat(False)
        self.tecla8.setObjectName(_fromUtf8("tecla8"))
        self.tecla9 = QtGui.QPushButton(self.centralwidget)
        self.tecla9.setGeometry(QtCore.QRect(160, 270, 40, 170))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla9.sizePolicy().hasHeightForWidth())
        self.tecla9.setSizePolicy(sizePolicy)
        self.tecla9.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.tecla9.setText(_fromUtf8(""))
        self.tecla9.setAutoDefault(False)
        self.tecla9.setFlat(False)
        self.tecla9.setObjectName(_fromUtf8("tecla9"))
        self.tecla10 = QtGui.QPushButton(self.centralwidget)
        self.tecla10.setGeometry(QtCore.QRect(330, 270, 40, 170))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla10.sizePolicy().hasHeightForWidth())
        self.tecla10.setSizePolicy(sizePolicy)
        self.tecla10.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.tecla10.setText(_fromUtf8(""))
        self.tecla10.setAutoDefault(False)
        self.tecla10.setFlat(False)
        self.tecla10.setObjectName(_fromUtf8("tecla10"))
        self.tecla11 = QtGui.QPushButton(self.centralwidget)
        self.tecla11.setGeometry(QtCore.QRect(410, 270, 40, 170))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla11.sizePolicy().hasHeightForWidth())
        self.tecla11.setSizePolicy(sizePolicy)
        self.tecla11.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.tecla11.setText(_fromUtf8(""))
        self.tecla11.setAutoDefault(False)
        self.tecla11.setFlat(False)
        self.tecla11.setObjectName(_fromUtf8("tecla11"))
        self.tecla12 = QtGui.QPushButton(self.centralwidget)
        self.tecla12.setGeometry(QtCore.QRect(490, 270, 40, 170))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tecla12.sizePolicy().hasHeightForWidth())
        self.tecla12.setSizePolicy(sizePolicy)
        self.tecla12.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
""))
        self.tecla12.setText(_fromUtf8(""))
        self.tecla12.setAutoDefault(False)
        self.tecla12.setFlat(False)
        self.tecla12.setObjectName(_fromUtf8("tecla12"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 21, 111, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcdFrequencia = QtGui.QLCDNumber(self.layoutWidget)
        self.lcdFrequencia.setObjectName(_fromUtf8("lcdFrequencia"))
        self.verticalLayout.addWidget(self.lcdFrequencia)
        self.frequencia = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.frequencia.setFont(font)
        self.frequencia.setAlignment(QtCore.Qt.AlignCenter)
        self.frequencia.setObjectName(_fromUtf8("frequencia"))
        self.verticalLayout.addWidget(self.frequencia)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(21, 131, 111, 121))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dial = QtGui.QDial(self.layoutWidget1)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.gridLayout.addWidget(self.dial, 0, 0, 1, 1)
        self.volume = QtGui.QLabel(self.layoutWidget1)
        self.volume.setAlignment(QtCore.Qt.AlignCenter)
        self.volume.setObjectName(_fromUtf8("volume"))
        self.gridLayout.addWidget(self.volume, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sintetizador de Áudio", None))
        self.frequencia.setText(_translate("MainWindow", "Frequência", None))
        self.volume.setText(_translate("MainWindow", "Volume", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))

from PyQt4 import Qwt5


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#/GUI

print "Iniciado, toque o teclado!"
    
def main():
    global nota
    global freq 
       
    pygame.init()
    
    while 1:

        events = event_get()
        if i.poll():
            midi_events = i.read(10)
            pos = midi_events[0][0][2] #Entrada MIDI valor2, que é usado para
                                       #saber se a nota foi pressionada (DOWN)
                                       #ou solta (UP).
            
            note = midi_events[0][0][1] #Entada MIDI valor1, que é usado para
                                        #saber qual tecla foi pressionada

            #Verifica se a tecla apertada é válida, pos != 0 => a nota foi
            #pressionada e não solta; note !=0 => uma nota foi pressionada/
            #solta, na ausência de nota pressionada, o teclado manda continua-
            #mente a nota 0.            
            if pos and note:
                
                #Pega o valor da frequencia baseado no dicionario acima                
                freq = DFreq[note]
                #A função freq_to_lag converte a frequencia para numero de 
                #amostras 
                N = freq_to_lag(freq * Hz)
                #Preparação do Stream (container definido pelo Audiolazy) no 
                #qual será aplicado o filtro que aproximará o som ao de um 
                #violão. O método empregado é semelhante ao do filtro comb
                smix = Streamix()
                #Cria uma stream de ruído branco baseada no numero de amostras
                smix.add(0, white_noise(N))
                smix.add(N, 0.99 * smix.copy())
                #Limita o tamanho da Stream. Por meio de testes, determinamos 
                #que 1 segundo é tempo suficiente para se ouvir o som, consi-
                #derando o decaimento e ajuda em aliviar a quantidade de dados
                #que serão processados.
                smix.limit(1 * s)
                
                #Filtro simplificado que 'cria' um som próximo ao do violão.
                filt = 0.01/(1 - 1.46146 * z**-1 + 0.875285 * z**-2 - 0.990911
                * z**-3 + 0.600283 * z**-4 - 0.021322 * z**-5)
            
#                Filtro obtido por meio da análise lpc de uma gravação do
#                som de um violão no formato wav.
#            Linear predictive coding - 
#                filt = 0.01/(1 - 1.24148 * z**-1 + 0.056845 * z**-2 + 
#                0.0437731 * z**-3 + 0.0337219 * z**-4 + 0.0259962 * z**-5 + 
#                0.0200621 * z**-6 + 0.0155093 * z**-7 + 0.0120234 * z**-8 + 
#                0.00936348 * z**-9 + 0.0073461 * z**-10 + 0.00583213 * z**-
#                11 + 0.00471728 * z**-12 + 0.00392492 * z**-13 + 0.00340072 
#                * z**-14 + 0.00310888 * z**-15 - 0.00275325 * z** -16)
#                
                player.play(filt(smix),rate = rate)
                                           
if __name__ == "__main__":
    main()
