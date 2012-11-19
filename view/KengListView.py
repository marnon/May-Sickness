from PyQt4 import QtGui,QtCore
class KengListView(QtGui.QListWidget):
	"""docstring for KengListView"""
	def __init__(self, parent=None):
		super(KengListView, self).__init__(parent)
		pass
	def dragEnterEvent(self, event):
		event.acceptProposedAction()
		print self,'dragEnterEvent'
	def dragMoveEvent(self, event):
		event.acceptProposedAction()
	def dropEvent(self, event):
		mimeData = event.mimeData()
		if mimeData.hasImage():
			self.setPixmap(QtGui.QPixmap(mimeData.imageData()))
		# elif mimeData.hasText():
		# 	self.setText(mimeData.text())
		# 	self.setTextFormat(QtCore.Qt.PlainText)
		elif mimeData.hasUrls():
			url=mimeData.urls()
			print url[0].path()

			print QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(url[0].path()))
			print QtGui.QListWidgetItem(url[0].path(),self)
		else:
			self.setText("Cannot display data")
		event.acceptProposedAction()
