import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignal,QObject,pyqtSlot
import subprocess
import os


class Communicate(QtCore.QObject):
    runApp=QtCore.pyqtSignal()
    burger=pyqtSignal()

class popUpWindow(QWidget):

    def __init__(self):
        super(popUpWindow,self).__init__()
        self.initUI()

    def initUI(self):
        lbl=QtGui.QLabel('<b>This is my thesis project </b>',self)

        lbl.move(15,10)

        self.setGeometry(500,500,400,150)
        self.setWindowTitle('About Devs')
        self.show()

class PopUpButtons(QWidget):

    def __init__(self):
        super(PopUpButtons,self).__init__()

        self.intUI()

    def intUI(self):

        self.setGeometry(500,500,300,150)
        self.setWindowTitle('Options')
        self.show()

class Example(QtGui.QMainWindow):



    def __init__(self):

        super(Example,self).__init__()
        self.initUI()

    def run(self,path):
        subprocess.call(['pythonw',path])

    def initUI(self):

        self.vars = globalVariables()
        self.r=Communicate()

        runAction=QAction("Run",self)
        runAction.setShortcut("Ctrl+R")
        runAction.setStatusTip('Run application')

        helpAction=QAction("About",self)

        self.statusBar()

        startbutton=QtGui.QPushButton('Sit',self)
        startbutton.setCheckable(True)
        startbutton.move(100,40)
        startbutton.clicked.connect(self.startButton)

        otherActionButton=QtGui.QPushButton('Other',self)
        otherActionButton.setCheckable(True)
        otherActionButton.move(190,40)
        otherActionButton.clicked.connect(self.otherActionButton)

        self.rb=QtGui.QRadioButton('Sit',self)
        self.rb.move(40,80)
        self.rb.setChecked(False)
        self.rb.toggled.connect(lambda:self.sitOn(self.rb))

        self.rb2=QtGui.QRadioButton('Eat',self)
        self.rb2.move(40,100)
        self.rb2.setChecked(True)
        self.rb2.toggled.connect(lambda:self.radiostate(self.rb2))

        sld=QtGui.QSlider(QtCore.Qt.Horizontal,self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30,130,100,30)
        sld.setValue(50)
        sld.valueChanged[int].connect(self.changeValue)

        lcd=QtGui.QLCDNumber(self)
        sld.valueChanged.connect(lcd.display)
        lcd.setGeometry(190,110,100,60)

        sld2=QtGui.QSlider(QtCore.Qt.Horizontal,self)
        sld2.setFocusPolicy(QtCore.Qt.NoFocus)
        sld2.setGeometry(30,180,100,30)
        sld2.setValue(50)

        plusbutton = QtGui.QPushButton('+', self)
        plusbutton.setCheckable(True)
        plusbutton.setGeometry(40,220,50,30)
        plusbutton.clicked.connect(self.addY)

        ylbl = QtGui.QLabel('Y', self)
        ylbl.move(95, 220)

        minusbutton=QtGui.QPushButton('-',self)
        minusbutton.setCheckable(True)
        minusbutton.setGeometry(110,220,50,30)
        minusbutton.clicked.connect(self.addY)

        plusbutton2=QtGui.QPushButton('+',self)
        plusbutton2.setCheckable(True)
        plusbutton2.setGeometry(40,260,50,30)
        plusbutton2.clicked.connect(self.addY)

        zlbl=QtGui.QLabel('Z',self)
        zlbl.move(95,260)

        minusbutton2=QtGui.QPushButton('-',self)
        minusbutton2.setCheckable(True)
        minusbutton2.setGeometry(110,260,50,30)
        minusbutton2.clicked.connect(self.addY)

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

    def addY(self):
        print "HEllo"

    def radiostate(self,rb):
        if rb.text() == "Sit":
            if rb.isChecked() ==True:
                print "Sit is selected"
                sender=self.sender()
        if rb.text() =="Eat":
            if rb.isChecked()==True:
                print "Eat is selected"

    def changeValue(self,value):
        if value==50:
            value=-0.0336414869782
            print 'Value is %1.13f'%value
        elif value < 49 and value >= 45:
            value=-0.0362357378123
            print 'Value is %1.13f'%value
        elif value < 44  and value >= 39:
            value=-0.0403124567346
            print 'Value is %1.13f'%value
        elif value < 38 and value >= 33:
            value=-0.0449852123904
            print 'Value is %1.13f'%value

        elif value < 33 and value >=27:
            value=-0.046
        else:
            print "Above"

    def eatOn(self,state):
        if state==QtCore.Qt.Checked:
            os.system('testing.py')
        else:
            print "Not hello"

    def sitOn(self,state):
        if state==QtCore.Qt.Checked:
            self.setWindowTitle('Skinect Gui')
        else:
            self.setWindowTitle('')

    def startButton(self):
         os.system('testing.py')

    def otherActionButton(self):
        os.system('otherAction.py')

    def aboutKinect(self):
        self.about=popUpWindow()
        self.about.show()


def main():

    app=QtGui.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

