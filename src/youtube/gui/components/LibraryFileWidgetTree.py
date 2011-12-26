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
