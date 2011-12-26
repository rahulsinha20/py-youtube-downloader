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
        self.setFlags(PyQt4.QtCore.Qt.ItemIsEditable|self.flags())
        
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