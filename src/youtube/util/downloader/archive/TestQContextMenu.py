'''
Created on 11/08/2011

@author: asinha
'''
from PyQt4.QtGui import ( 
     QApplication, QTreeWidget, QTreeWidgetItem, QMenu, 
     ) 


class TreeWidget(QTreeWidget): 
     def __init__(self, parent=None): 
         QTreeWidget.__init__(self, parent) 
         self.setWindowTitle('TreeWidget Context Menu') 
         self.header().setHidden(True) 
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