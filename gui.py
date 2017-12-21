from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignal
import sys,os
from threshold import globalVariables
# from functions import functionsClass
import subprocess


class Communicate(QtCore.QObject):
    runApp=QtCore.pyqtSignal()
    burger=pyqtSignal()

class popUpWindow(QWidget):

    def __init__(self):
        super(popUpWindow,self).__init__()
        self.initUI()

    def initUI(self):
        lbl=QtGui.QLabel('<b>Useful commands </b>',self)
        lbl.move(15,10)
        controls = QtGui.QLabel('Controls:\nd - Switch to depth view\n'
                                'v - Switch to video view\n'
                                's - Toggle displaing of the skeleton\n'
                                'u - Increase elevation angle\n'
                                'j - Decrease elevation angle',self)
        controls.move(15,30)
        self.setGeometry(500,500,400,150)
        self.setWindowTitle('Help Kinect')
        self.show()

class OutputWindow(QtGui.QPlainTextEdit):
    def __init__(self):
        super(OutputWindow,self).__init__()
        self.setWindowTitle('Kinect Output')
        self.setGeometry(300,500,350,150)


    def write(self, txt):
        self.appendPlainText(txt)


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        #self.glvars = globalVariables()
        self.r=Communicate()

        runAction=QAction("Run",self)
        runAction.setShortcut("Ctrl+R")
        runAction.setStatusTip('Run application')

        helpAction=QAction("About",self)

        self.statusBar()
        self.thresholdObj = globalVariables()

        startbutton=QtGui.QPushButton('Sit',self)
        startbutton.setCheckable(True)
        startbutton.move(100,40)
        startbutton.clicked.connect(self.startButton)

        otherActionButton=QtGui.QPushButton('Other',self)
        otherActionButton.setCheckable(True)
        otherActionButton.move(190,40)
        otherActionButton.clicked.connect(self.otherActionButton)

        plusbutton = QtGui.QPushButton('+', self)
        plusbutton.setCheckable(True)
        plusbutton.setGeometry(40,220,50,30)
        plusbutton.clicked.connect(self.thresholdObj.addsitY)

        ylbl = QtGui.QLabel('Y', self)
        ylbl.move(95, 220)

        minusbutton=QtGui.QPushButton('-',self)
        minusbutton.setCheckable(True)
        minusbutton.setGeometry(110,220,50,30)
        minusbutton.clicked.connect(self.thresholdObj.decSitY)


        plusbutton2=QtGui.QPushButton('+',self)
        plusbutton2.setCheckable(True)
        plusbutton2.setGeometry(40,260,50,30)
        plusbutton2.clicked.connect(self.thresholdObj.addSitZ)

        zlbl=QtGui.QLabel('Z',self)
        zlbl.move(95,260)

        minusbutton2=QtGui.QPushButton('-',self)
        minusbutton2.setCheckable(True)
        minusbutton2.setGeometry(110,260,50,30)
        minusbutton2.clicked.connect(self.thresholdObj.decSitZ)

        menubar = self.menuBar()
        runMenu=menubar.addMenu('&Run')
        runMenu.addAction(runAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(helpAction)
        #trigger events for menu

        helpAction.triggered.connect(self.aboutKinect)

        self.textEdit = QtGui.QTextEdit()
        self.l1=QtGui.QLabel("",self)
        self.l1.move(100,100)

        self.statusBar()
        self.setGeometry(700,400,400,300)
        self.setWindowTitle('PyKinect')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.show()

    def startButton(self):
        subprocess.Popen("testing.py", shell=True)

    def otherActionButton(self):
        subprocess.Popen('otherAction.py',shell=True)


    def aboutKinect(self):
        self.about=popUpWindow()
        self.about.show()

    def setOutput(self,txt):
        self.txt = txt


def main():

    app=QtGui.QApplication(sys.argv)
    ex=Example()
    out = OutputWindow()
    sys.stdout = out
    out.show()
    app.exec_()


if __name__=='__main__':
    main()


