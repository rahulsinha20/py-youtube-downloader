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
Created on 11/08/2011
Represents Menu for Library Item
@author: asinha
'''
from PyQt4 import QtGui, QtCore
class LibraryItemMenu(QtGui.QMenu):
    '''
    Represents a menu for users to select options for retrieved videos
    '''

    def __init__(self,item, parent = None):
        '''
        Creates an instance of QMenu
        '''
        QtGui.QMenu.__init__(self, parent)
        #Store a reference to clickable label that invoked me
        self.parentWidget = parent
        #Also a reference to the tree widget item
        self.libraryTreeItem = item        
        #check if the event is originating from the tree root
        if item.text(0) == 'Video Library':
            #Check if this 
            self.configureMenuItems(True) #Root folder
        else:
            
            if item.parent().text(0) == 'Video Library' and item.childCount()>0:
                self.configureMenuItems(False, True) #Not a root node but a folder with no media files            
            elif item.parent().text(0) == 'Video Library' and item.childCount()==0:
                self.configureMenuItems(False,True, False)
            else:
                self.configureMenuItems(False, False, True)
    def configureMenuItems(self,isRoot=False, isFolderOnly=False, isVideoItem=False):
        if isRoot:
            #This is the root node, show options for root
#            self.changeLibraryFolderAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&Change Library Folder'))
            self.expandAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&Expand'))
            self.collapseAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&Collapse'))
#            QtCore.QObject.connect(self.changeLibraryFolderAction, QtCore.SIGNAL("triggered()"), self.changeLibraryFolderActionSlot)
            QtCore.QObject.connect(self.expandAction, QtCore.SIGNAL("triggered()"), self.expandActionSlot)
            QtCore.QObject.connect(self.collapseAction, QtCore.SIGNAL("triggered()"), self.collapseActionSlot)
        elif isFolderOnly:
            #If its a folder and number of children = 0, show delete option
            self.renameFolder = self.addAction(QtGui.QIcon(QtCore.QString("./resources/RenameFolder.gif")),self.tr('&Rename Folder'))
            self.deleteFolder = self.addAction(QtGui.QIcon(QtCore.QString("./resources/DeleteFolder.png")),self.tr('&Delete Folder'))
            QtCore.QObject.connect(self.deleteFolder, QtCore.SIGNAL("triggered()"), self.deleteActionSlot)
            QtCore.QObject.connect(self.renameFolder, QtCore.SIGNAL("triggered()"), self.renameActionSlot)
        elif isVideoItem:
            self.playVideoAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/PlayButton.png")),self.tr('&Play'))
            #Check if this item has been already queued
            if self.libraryTreeItem.getQueuedStatus()== True:
                self.playVideoAction.setEnabled(False)
            else:
                self.playVideoAction.setEnabled(True)
            self.renameVideo = self.addAction(QtGui.QIcon(QtCore.QString("./resources/RenameFolder.gif")),self.tr('&Rename'))
            self.deleteVideo = self.addAction(QtGui.QIcon(QtCore.QString("./resources/DeleteFolder.png")),self.tr('&Delete'))
            QtCore.QObject.connect(self.playVideoAction, QtCore.SIGNAL("triggered()"), self.playVideoActionSlot)
#            self.renameFolder = self.addAction(QtGui.QIcon(QtCore.QString("./resources/RenameFolder.gif")),self.tr('&Rename Folder'))
#            self.deleteFolder = self.addAction(QtGui.QIcon(QtCore.QString("./resources/DeleteFolder.png")),self.tr('&Delete Folder'))
            QtCore.QObject.connect(self.deleteVideo, QtCore.SIGNAL("triggered()"), self.deleteActionSlot)
            QtCore.QObject.connect(self.renameVideo, QtCore.SIGNAL("triggered()"), self.renameActionSlot)
#            QtCore.QObject.connect(self.deleteFolder, QtCore.SIGNAL("triggered()"), self.deleteActionSlot)
#        elif !isFolderOnly and isVideoItem:
            
#        self.viewAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&View'))
#        self.downloadAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/download.png")),self.tr('&Download'))
#        QtCore.QObject.connect(self.viewAction, QtCore.SIGNAL("triggered()"), self.viewMenuItemClickedSlot)
        
        #Check if this item is queued for download
#        self.isQueuedForDownload()
    def deleteActionSlot(self):
        '''
        Performs item delete action
        '''
        print 'Delete Action'
        self.parentWidget.parentController.deleteVideoForLibraryItem(self.libraryTreeItem)
    def renameActionSlot(self):
        '''
        Performs item rename
        '''
        self.parentWidget.parentController.renameVideoForLibraryItem(self.libraryTreeItem)
    def playVideoActionSlot(self):
        print 'Play video'
        #Get UI Controller
        self.parentWidget.parentController.playVideoForLibraryItem(self.libraryTreeItem)
    def changeLibraryFolderActionSlot(self):
        return
    def expandActionSlot(self):
        self.parentWidget.expandAll()  
    def collapseActionSlot(self):
        self.parentWidget.collapseAll() 
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