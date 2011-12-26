''' Copyright (C) 2010 Abhijat Sinha (Rahul)    
    "This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."
     
    '''

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
