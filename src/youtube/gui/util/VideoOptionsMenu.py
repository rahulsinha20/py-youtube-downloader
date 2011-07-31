'''
Created on Jul 31, 2011
Represents a Menu when the user right clicks on a video
@author: Rahul
'''
from PyQt4 import QtGui, QtCore
class VideoOptionsMenu(QtGui.QMenu):
    '''
    Represents a menu for users to select options for retrieved videos
    '''


    def __init__(self, parent = None):
        '''
        Creates an instance of QMenu
        '''
        QtGui.QMenu.__init__(self, parent)
        #Store a reference to clickable label that invoked me
        self.parentWidget = parent
        #Add actions
        self.viewAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&View'))
#        self.downloadAction = self.addAction(self.tr('&Download'))
        QtCore.QObject.connect(self.viewAction, QtCore.SIGNAL("triggered()"), self.viewMenuItemClickedSlot)
#        QtCore.QObject.connect(self.downloadAction, QtCore.SIGNAL("triggered()"), self.downloadMenuItemClickedSlot)

    def viewMenuItemClickedSlot(self):
        '''
        Slot when view menu item is selected
        '''       
        self.parentWidget.emit(QtCore.SIGNAL('clicked(PyQt_PyObject)'), self.parentWidget)
    
#    def downloadMenuItemClickedSlot(self):
#        '''
#        Slot when download menu item is selected
#        '''
#        
#        self.parentWidget.emit(QtCore.SIGNAL('clicked(PyQt_PyObject2)'), self.parentWidget)
#        