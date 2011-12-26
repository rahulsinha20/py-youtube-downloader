'''Testing License v0.1'''
'''
Created on Aug 1, 2011

@author: Rahul
'''
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Tooltip(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltip')

        self.setToolTip('This is a <b>QWidget</b> widget')
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))

