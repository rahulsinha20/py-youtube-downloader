'''
Created on Dec 26, 2011

@author: Rahul
'''

from PyQt4 import QtGui
import os

class ConfirmDialog(QtGui.QWidget):
    
    def __init__(self, controller = None):
        super(ConfirmDialog, self).__init__()
        self.controller = controller
#        self.__init__()
#        self.initUI()
        
    def initUI(self):      

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Confirm dialog')
        self.show()
        
    def showDialog(self, path):
        
        currentFileNameExtension = os.path.splitext(str(path))[1]
        currentFileName = path;
        print 'Current File Name:'+currentFileName
        index = str(path).rfind("/")
       
        text, ok = QtGui.QInputDialog.getText(self, 'Rename:', 
            'Enter new name:')
        
        if ok:
            newFileName = path[:index+1]+str(text)
            print 'New File Name:'+newFileName
            os.rename(currentFileName, newFileName+currentFileNameExtension)
            self.controller.updateVideoLibrary()
