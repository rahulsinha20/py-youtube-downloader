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
Created on Aug 10, 2011

@author: Rahul
'''

from PyQt4.QtGui import ( 
     QApplication, QTreeWidget, QTreeWidgetItem, QMenu, 
     ) 


class TreeWidget(QTreeWidget): 
     def __init__(self, parent=None): 
         QTreeWidget.__init__(self, parent) 
         self.setWindowTitle('TreeWidget Context Menu') 
#         self.header().setHidden(True) 
         self.setGeometry(320, 320, 320, 320) 
         for index in '12345': 
             parent = QTreeWidgetItem(self, ['Parent %s' % index]) 
             for item in 'ABCDE': 
                 QTreeWidgetItem(parent, ['Child %s%s' % (index, item)]) 
             parent.setExpanded(True) 

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
             menu = QMenu(self) 
             menu.addAction(item.text(0)) 
             menu.popup(pos) 
         event.accept() 


if __name__ == "__main__": 

     import sys 
     app = QApplication(sys.argv) 
     tree = TreeWidget() 
     tree.show() 
     sys.exit(app.exec_())