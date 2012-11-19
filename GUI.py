# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'May Sickness.ui'
#
# Created: Sun Nov 18 21:51:30 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(525, 617)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(5, 5, 511, 551))
        self.widget.setAcceptDrops(True)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.listWidget = KengListView(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 491, 471))
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setStyleSheet(_fromUtf8(" QListView {\n"
"     show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
" }\n"
"\n"
" QListView::item:alternate {\n"
"     background: #EEEEEE;\n"
" }\n"
"\n"
" QListView::item:selected {\n"
"     border: 1px solid #6a6ea9;\n"
" }\n"
"\n"
" QListView::item:selected:!active {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
" }\n"
"\n"
" QListView::item:selected:active {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
" }\n"
"\n"
" QListView::item:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
" }"))
        self.listWidget.setViewMode(QtGui.QListView.IconMode)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.btnReaper = QtGui.QPushButton(self.widget)
        self.btnReaper.setGeometry(QtCore.QRect(10, 10, 48, 48))
        self.btnReaper.setAcceptDrops(False)
        self.btnReaper.setObjectName(_fromUtf8("btnReaper"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 23))
        self.menubar.setStyleSheet(_fromUtf8(" QMenuBar {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                       stop:0 lightgray, stop:1 darkgray);\n"
" }\n"
"\n"
" QMenuBar::item {\n"
"     spacing: 3px; /* spacing between menu bar items */\n"
"     padding: 1px 4px;\n"
"     background: transparent;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"     background: #a8a8a8;\n"
" }\n"
"\n"
" QMenuBar::item:pressed {\n"
"     background: #525252;\n"
" }\n"
"\n"
"\n"
"/* action style*/\n"
"QMenu {\n"
"     background-color: white;\n"
"     margin: 2px; /* some spacing around the menu */\n"
" }\n"
"\n"
" QMenu::item {\n"
"     padding: 2px 25px 2px 20px;\n"
"     border: 1px solid transparent; /* reserve space for selection border */\n"
" }\n"
"\n"
" QMenu::item:selected {\n"
"     border-color: darkblue;\n"
"     background: rgba(100, 100, 100, 150);\n"
" }\n"
"\n"
" QMenu::icon:checked { /* appearance of a \'checked\' icon */\n"
"     background: gray;\n"
"     border: 1px inset gray;\n"
"     position: absolute;\n"
"     top: 1px;\n"
"     right: 1px;\n"
"     bottom: 1px;\n"
"     left: 1px;\n"
" }\n"
"\n"
" QMenu::separator {\n"
"     height: 2px;\n"
"     background: lightblue;\n"
"     margin-left: 10px;\n"
"     margin-right: 5px;\n"
" }\n"
"\n"
" QMenu::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */\n"
" QMenu::indicator:non-exclusive:unchecked {\n"
"     image: url(:/images/checkbox_unchecked.png);\n"
" }\n"
"\n"
" QMenu::indicator:non-exclusive:unchecked:selected {\n"
"     image: url(:/images/checkbox_unchecked_hover.png);\n"
" }\n"
"\n"
" QMenu::indicator:non-exclusive:checked {\n"
"     image: url(:/images/checkbox_checked.png);\n"
" }\n"
"\n"
" QMenu::indicator:non-exclusive:checked:selected {\n"
"     image: url(:/images/checkbox_checked_hover.png);\n"
" }\n"
"\n"
" /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
" QMenu::indicator:exclusive:unchecked {\n"
"     image: url(:/images/radiobutton_unchecked.png);\n"
" }\n"
"\n"
" QMenu::indicator:exclusive:unchecked:selected {\n"
"     image: url(:/images/radiobutton_unchecked_hover.png);\n"
" }\n"
"\n"
" QMenu::indicator:exclusive:checked {\n"
"     image: url(:/images/radiobutton_checked.png);\n"
" }\n"
"\n"
" QMenu::indicator:exclusive:checked:selected {\n"
"     image: url(:/images/radiobutton_checked_hover.png);\n"
" }\n"
""))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setStyleSheet(_fromUtf8(""))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewFile = QtGui.QAction(MainWindow)
        self.actionNewFile.setObjectName(_fromUtf8("actionNewFile"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.action_4)
        self.menuEdit.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "五月病", None, QtGui.QApplication.UnicodeUTF8))
        self.btnReaper.setText(QtGui.QApplication.translate("MainWindow", ".rpp", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "文件", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "编辑", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFile.setText(QtGui.QApplication.translate("MainWindow", "新建", None, QtGui.QApplication.UnicodeUTF8))
        self.action_4.setText(QtGui.QApplication.translate("MainWindow", "打开", None, QtGui.QApplication.UnicodeUTF8))

from view.KengListView import KengListView
