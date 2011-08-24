'''
Created on Feb 21, 2010
Represents an item in the library tree widget
@author: Rahul Sinha
'''
from PyQt4 import QtGui
import PyQt4
class LibraryFileWidgetItem(QtGui.QTreeWidgetItem):
    '''
    This class represents a file in the library. It has a text indicating
    its name and a boolean indicating if its being queued/playing
    '''
    
    def __init__(self, stringList):
        '''
        Constructor - calls parent class constructor
        Note-we invoke parent class constructor that takes QStringlist as an arg
        '''
        QtGui.QTreeWidgetItem.__init__(self, stringList)
        #Assign this as not queued/playing
        self.setQueuedStatus(False)
        self.setFlags(PyQt4.QtCore.Qt.ItemIsEditable|PyQt4.QtCore.Qt.ItemIsEnabled|PyQt4.QtCore.Qt.ItemIsSelectable)
        
    def setQueuedStatus(self, queued):
        '''
        Sets the state for this file
        '''
        self.queuedStatus = queued
        
    def getQueuedStatus(self):
        '''
        Returns queued status for the file
        '''
        return self.queuedStatus
    def mousePressEvent(self, mouseEvent):
        print 'mouse clicked'
        print self