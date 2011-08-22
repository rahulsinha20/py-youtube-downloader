'''
Created on 11/08/2011
Represents QTreeWidget housing Library Files/Folders
@author: asinha
'''
from PyQt4.QtGui import (QTreeWidget, QTreeWidgetItem, QMenu)
from youtube.gui.util import LibraryItemMenu
class LibraryFileWidgetTree(QTreeWidget):
    '''
    classdocs
    '''


    def __init__(self, controller, parent = None):
        '''
        Constructor - calls parent class constructor
        '''
        QTreeWidget.__init__(self, parent)
        if parent!=None:
            self.parentController = parent
    def contextMenuEvent(self, event): 
        if event.reason() == event.Mouse: 
            pos = event.globalPos() 
            item = self.itemAt(event.pos()) 
        else: 
            pos = None 
            selection = self.selectedItems() 
            if selection: 
                item = selection[0] 
            else: 
                item = self.currentItem() 
                if item is None: 
                    item = self.invisibleRootItem().child(0) 
            if item is not None: 
                parent = item.parent() 
                while parent is not None: 
                    parent.setExpanded(True) 
                    parent = parent.parent() 
                itemrect = self.visualItemRect(item) 
                portrect = self.viewport().rect() 
                if not portrect.contains(itemrect.topLeft()): 
                    self.scrollToItem( 
                        item, QTreeWidget.PositionAtCenter) 
                    itemrect = self.visualItemRect(item) 
                itemrect.setLeft(portrect.left()) 
                itemrect.setWidth(portrect.width()) 
                pos = self.mapToGlobal(itemrect.center()) 
        if pos is not None: 
            menu = LibraryItemMenu.LibraryItemMenu(item,self)             
            menu.popup(pos) 
        event.accept() 
