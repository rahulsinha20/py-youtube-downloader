'''Testing License v0.1'''
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
        #Define if this represents a youtube video, all else videos should not have
        #checboxes enabled as we still cannot download them !
        self.canDownload = True
    def setNotDownloadable(self):
        '''
        Sets this checkboxes state so it cannot be selected for a download
        '''
        self.canDownload = False
    def getCanDownloadState(self):
        '''
        Returns if we can download the item represented by this checkbox
        '''        
        return self.canDownload
    def setNumberIndex(self, number):
        self.numberIndex = number
    def getNumberIndex(self):
        return self.numberIndex
