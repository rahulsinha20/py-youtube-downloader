'''
Created on Feb 18, 2010

@author: Rahul Sinha
'''
from PyQt4 import QtGui

class NumberedCheckBox(QtGui.QCheckBox):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        ''' Is the non default constructor that sets up the main widget'''
        QtGui.QCheckBox.__init__(self, parent)
    def setNumberIndex(self, number):
        self.numberIndex = number
    def getNumberIndex(self):
        return self.numberIndex
