import sys, os
if os.system('pyuic4 -o GUI.py "May Sickness.ui"')==0:
	print 'build GUI.py ok!'
	os.system('python "May Sickness.py"')
else:
	print 'build GUI.py 0r2...'
 	pass 
