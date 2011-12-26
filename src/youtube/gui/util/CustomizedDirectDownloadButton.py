'''Testing License v0.1'''
'''
Created on 27/11/2010

@author: Rahul
'''
from PyQt4 import QtGui

class CustomizedDirectDownloadButton(QtGui.QPushButton):
    '''
    This allows QPushButton having toggle state - Add, Remove
    '''

    def __init__(self, counter, parent=None):
        ''' Is the non default constructor that sets up the main widget'''
        QtGui.QPushButton.__init__(self, parent)
        self.addState = True
        self.buttonCounter = counter
    def setButtonCounter(self, value):
        self.buttonCounter = value
    def getButtonCounter(self):
        '''
        Returns button number/index
        '''
        return self.buttonCounter
    def setAddState(self, state):
        '''
        Sets Add State
        '''
        self.addState = state
        
    def getAddState(self):
        '''
        Returns Add State for the button
        '''
        return self.addState
