import win32ui
import win32gui
from PyQt4 import QtGui
def ExtractIcon(filename):
    large, small = win32gui.ExtractIconEx(filename, 0)
    # win32gui.DestroyIcon(small[0])
    h=bitmapFromHIcon(large[0])
    print h
    pixmap = QtGui.QPixmap.fromWinHBITMAP(h, 2)
    pixmap.save("large.ico","ico")
    pass
def bitmapFromHIcon(hIcon):
    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, 40, 40)
    hdc = hdc.CreateCompatibleDC()
    hdc.SelectObject(hbmp)
    hdc.DrawIcon((0, 0), hIcon)
    hdc.DeleteDC()
    return hbmp.GetHandle()
    
if __name__ == "__main__":
    app = QtGui.QApplication([])
    filename='E:/Program Files (x86)/REAPER 4.30/REAPER.exe'
    f=fuckIcon(filename)
    app.exec_()