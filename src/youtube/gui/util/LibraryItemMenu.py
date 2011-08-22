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


    def __init__(self,text, childCount, parent = None):
        '''
        Creates an instance of QMenu
        '''
        QtGui.QMenu.__init__(self, parent)
        #Store a reference to clickable label that invoked me
        self.parentWidget = parent
        #check if the event is originating from the tree root
        if text == 'Video Library':
            self.configureMenuItems(True, False)
        elif childCount==0:
            self.configureMenuItems(False, True)
        else:
            self.configureMenuItems(False, False)
    def configureMenuItems(self,isRoot=False, isFolder=False):
        if isRoot:
            #This is the root node, show options for root
            self.changeLibraryFolderAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&Change Library Folder'))
            self.expandAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&Expand'))
            self.collapseAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&Collapse'))
            QtCore.QObject.connect(self.changeLibraryFolderAction, QtCore.SIGNAL("triggered()"), self.changeLibraryFolderActionSlot)
            QtCore.QObject.connect(self.expandAction, QtCore.SIGNAL("triggered()"), self.expandActionSlot)
            QtCore.QObject.connect(self.collapseAction, QtCore.SIGNAL("triggered()"), self.collapseActionSlot)
        elif isFolder:
            self.renameFolder = self.addAction(QtGui.QIcon(QtCore.QString("./resources/RenameFolder.gif")),self.tr('&Rename Folder'))
#        self.viewAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/view.gif")),self.tr('&View'))
#        self.downloadAction = self.addAction(QtGui.QIcon(QtCore.QString("./resources/download.png")),self.tr('&Download'))
#        QtCore.QObject.connect(self.viewAction, QtCore.SIGNAL("triggered()"), self.viewMenuItemClickedSlot)
        
        #Check if this item is queued for download
#        self.isQueuedForDownload()
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