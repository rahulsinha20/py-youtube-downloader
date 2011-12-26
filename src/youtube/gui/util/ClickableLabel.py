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
Created on Feb 17, 2010

@author: Rahul Sinha
'''

from PyQt4 import QtGui, QtCore
import VideoOptionsMenu
from youtube.gui.core.DownloadDialog import Ui_WallpaperChangerDialog
class ClickableLabel(QtGui.QLabel):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        ''' Is the non default constructor that sets up the main widget'''
        QtGui.QLabel.__init__(self, parent)
        self.ref = self
        #Assign a reference to controller
        self.controller = parent
        self.index = 0;
    def getIndex(self):
        '''
        Returns video index
        '''
        return int(self.index)
    def setIndex(self, value):
        '''
        Every video item can be accessed via its unique index
        '''
        self.index = value
    def setWebLink(self, link):
        self.webUrl = link
    def mouseMoveEvent(self, mouseEvent):
        print 'Mouse Hovered over a label'
    def mousePressEvent(self, mouseEvent):
        print 'mouse clicked'
        print self
        # Check if the user pressed a left or right click
        button = mouseEvent.button()
        if button == 1:
            self.emit(QtCore.SIGNAL('clicked(PyQt_PyObject)'), self)
        elif button == 2:
            print "Right click pressed", self.ref
            test = VideoOptionsMenu.VideoOptionsMenu(self)
            test.exec_(self.mapToGlobal(QtCore.QPoint(0,0)))
        else:    
            mouseEvent.ignore()
    def getWebLink(self):
        return self.webUrl
        
        
