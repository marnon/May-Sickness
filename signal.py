from PyQt4 import QtCore

 class MyQObject(QtCore.QObject):
   # 定義一個無參數的signal
   signal1 = QtCore.pyqtSignal()
   # 定義一個有一個整數參數的signal，並且name為qtSignal2。
   signal2 = QtCore.pyqtSignal(int, name='qtSignal2')
   def connectSigSlot(self):
       # 利用pySignal物件本身提供的connect，我們可以輕易的將pySignal物件與對應的slot相連。
       # 將signal1與myReceiver1連接起來。
       signal1.connect(self.myReceiver1)
       # 將signal2與myReceiver2連接起來。
       signal2.connect(self.myReceiver2)
   def myEmitter(self, arg):
       # 利用pyqtSignal物件所提供的emit function，我們就可以輕易的發出signal。
       signal1.emit()
       signal2.emit(10)
   def myReceiver1(self):
       print 'myReceiver1 called'
   def myReceiver2(self, arg):
       print 'myReceiver2 called with argument value %d' % arg
