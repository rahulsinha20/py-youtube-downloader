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
        
        
