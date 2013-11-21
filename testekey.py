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
        MainWindow.resize(710, 609)
        MainWindow.setMaximumSize(QtCore.QSize(1443, 921))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(65, 251, 80, 320))
        self.graphicsView.setMinimumSize(QtCore.QSize(80, 320))
        self.graphicsView.setMaximumSize(QtCore.QSize(70, 320))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(149, 251, 80, 320))
        self.graphicsView_2.setMinimumSize(QtCore.QSize(80, 320))
        self.graphicsView_2.setMaximumSize(QtCore.QSize(70, 320))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(233, 251, 80, 320))
        self.graphicsView_3.setMinimumSize(QtCore.QSize(80, 320))
        self.graphicsView_3.setMaximumSize(QtCore.QSize(70, 320))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(317, 251, 80, 320))
        self.graphicsView_4.setMinimumSize(QtCore.QSize(80, 320))
        self.graphicsView_4.setMaximumSize(QtCore.QSize(70, 320))
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.graphicsView_5 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(401, 251, 80, 320))
        self.graphicsView_5.setMinimumSize(QtCore.QSize(80, 320))
        self.graphicsView_5.setMaximumSize(QtCore.QSize(70, 320))
        self.graphicsView_5.setObjectName(_fromUtf8("graphicsView_5"))
        self.graphicsView_6 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_6.setGeometry(QtCore.QRect(485, 251, 80, 320))
        self.graphicsView_6.setMinimumSize(QtCore.QSize(80, 320))
        self.graphicsView_6.setMaximumSize(QtCore.QSize(70, 320))
        self.graphicsView_6.setObjectName(_fromUtf8("graphicsView_6"))
        self.graphicsView_7 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_7.setGeometry(QtCore.QRect(569, 251, 80, 320))
        self.graphicsView_7.setMaximumSize(QtCore.QSize(70, 320))
        self.graphicsView_7.setObjectName(_fromUtf8("graphicsView_7"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 250, 222, 202))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setSpacing(40)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.graphicsView_10 = QtGui.QGraphicsView(self.layoutWidget)
        self.graphicsView_10.setMinimumSize(QtCore.QSize(40, 200))
        self.graphicsView_10.setMaximumSize(QtCore.QSize(40, 200))
        self.graphicsView_10.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.graphicsView_10.setObjectName(_fromUtf8("graphicsView_10"))
        self.horizontalLayout_3.addWidget(self.graphicsView_10)
        self.graphicsView_12 = QtGui.QGraphicsView(self.layoutWidget)
        self.graphicsView_12.setMinimumSize(QtCore.QSize(40, 200))
        self.graphicsView_12.setMaximumSize(QtCore.QSize(40, 200))
        self.graphicsView_12.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.graphicsView_12.setObjectName(_fromUtf8("graphicsView_12"))
        self.horizontalLayout_3.addWidget(self.graphicsView_12)
        self.graphicsView_11 = QtGui.QGraphicsView(self.layoutWidget)
        self.graphicsView_11.setMinimumSize(QtCore.QSize(40, 200))
        self.graphicsView_11.setMaximumSize(QtCore.QSize(40, 200))
        self.graphicsView_11.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.graphicsView_11.setObjectName(_fromUtf8("graphicsView_11"))
        self.horizontalLayout_3.addWidget(self.graphicsView_11)
        self.qwtPlot = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot.setGeometry(QtCore.QRect(280, 20, 361, 191))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 250, 132, 202))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.graphicsView_8 = QtGui.QGraphicsView(self.widget)
        self.graphicsView_8.setMinimumSize(QtCore.QSize(40, 200))
        self.graphicsView_8.setMaximumSize(QtCore.QSize(40, 200))
        self.graphicsView_8.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.graphicsView_8.setObjectName(_fromUtf8("graphicsView_8"))
        self.horizontalLayout_2.addWidget(self.graphicsView_8)
        self.graphicsView_9 = QtGui.QGraphicsView(self.widget)
        self.graphicsView_9.setMinimumSize(QtCore.QSize(40, 200))
        self.graphicsView_9.setMaximumSize(QtCore.QSize(40, 200))
        self.graphicsView_9.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.graphicsView_9.setObjectName(_fromUtf8("graphicsView_9"))
        self.horizontalLayout_2.addWidget(self.graphicsView_9)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(70, 110, 181, 101))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout = QtGui.QGridLayout(self.widget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dial_3 = QtGui.QDial(self.widget1)
        self.dial_3.setObjectName(_fromUtf8("dial_3"))
        self.gridLayout.addWidget(self.dial_3, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.dial = QtGui.QDial(self.widget1)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.gridLayout.addWidget(self.dial, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.dial_2 = QtGui.QDial(self.widget1)
        self.dial_2.setObjectName(_fromUtf8("dial_2"))
        self.gridLayout.addWidget(self.dial_2, 0, 1, 1, 1)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(70, 10, 181, 91))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lcdNumber = QtGui.QLCDNumber(self.widget2)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.verticalLayout.addWidget(self.lcdNumber)
        self.label_4 = QtGui.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sintetizador de Audio", None))
        self.label_2.setText(_translate("MainWindow", "Pitch", None))
        self.label_3.setText(_translate("MainWindow", "Distortion", None))
        self.label.setText(_translate("MainWindow", "Volume", None))
        self.label_4.setText(_translate("MainWindow", "Frequência", None))
        self.actionClose.setText(_translate("MainWindow", "Close", None))

from PyQt4 import Qwt5
import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

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