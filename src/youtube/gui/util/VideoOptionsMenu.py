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
        #Check if this item is queued for download
        self.isQueuedForDownload()
        
    def isQueuedForDownload(self):
        '''
        Disables Download menu item if this item has already been queued
        '''
        if self.parentWidget.controller.getCheckBoxState(self.parentWidget.getIndex()-1) == True:
            #Already Queued, disable menu items
            self.clear()
            #Add New actions
            self.viewAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&View'))
            #Check if the video represented by the checkbox is available for a download
            if self.parentWidget.controller.getCanDownloadCheckBoxState(self.parentWidget.getIndex()-1)== False:
                self.notAvailableForDownload = self.addAction(QtGui.QIcon(QtCore.QString("./resources/exclaimation.png")),self.tr('&Download Unavailable'))
            else:
                self.cancelDownloadAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/cancelDownload.png")),self.tr('&Cancel Download'))
                QtCore.QObject.connect(self.cancelDownloadAction, QtCore.SIGNAL("triggered()"), self.cancelDownloadItemClickedSlot)
            QtCore.QObject.connect(self.viewAction, QtCore.SIGNAL("triggered()"), self.viewMenuItemClickedSlot)
            
        else:
            self.clear()
            #Add actions
            self.viewAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&View'))
            #Check if the video represented by the checkbox is available for a download
            if self.parentWidget.controller.getCanDownloadCheckBoxState(self.parentWidget.getIndex()-1)== False:
                self.notAvailableForDownload = self.addAction(QtGui.QIcon(QtCore.QString("./resources/exclaimation.png")),self.tr('&Download Unavailable'))
            else:
                self.downloadAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/download.png")),self.tr('&Download'))
                QtCore.QObject.connect(self.downloadAction, QtCore.SIGNAL("triggered()"), self.downloadMenuItemClickedSlot)
            QtCore.QObject.connect(self.viewAction, QtCore.SIGNAL("triggered()"), self.viewMenuItemClickedSlot)
            
                
    def cancelDownloadItemClickedSlot(self):
        '''
        Removes this item from queued list of downloads
        '''       
        self.parentWidget.controller.setCheckBoxState(self.parentWidget.getIndex()-1, False)
    
    def viewMenuItemClickedSlot(self):
        '''
        Slot when view menu item is selected
        '''       
        self.parentWidget.emit(QtCore.SIGNAL('clicked(PyQt_PyObject)'), self.parentWidget)
    
    def downloadMenuItemClickedSlot(self):
        '''
        Slot when download menu item is selected
        The checkbox corresponding to this label starts from index 0, therefore we subtract 1 from getIndex()
        CheckBoxes and Labels follow indices: {1,2...} but to retrieve from their
        corresponding list we map 1 --> index 0
        '''
        #Select the checkbox, this will also emit a signal which is handled in the controller
        self.parentWidget.controller.setCheckBoxState(self.parentWidget.getIndex()-1, True)
#        checkBoxInstance.setChecked(True)
#        checkBoxInstance.repaint()