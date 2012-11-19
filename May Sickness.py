from PyQt4 import QtGui, QtCore, uic
import sys,os,sip
from GUI import Ui_MainWindow
from utils.IconExtractor import ExtractIcon
# from mskwidget import MSKWidget

class MainWin(QtGui.QMainWindow,Ui_MainWindow):
    """docstring for MainWin"""
    intit=False
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # app.setStyle("cleanlooks")
    # app.setStyle("plastique")
    ExtractIcon('E:/Program Files (x86)/REAPER 4.30/REAPER.exe')
    mainWin=MainWin()
    mainWin.show()

    print 'app start up...'
    print mainWin.intit
    sys.exit(app.exec_())