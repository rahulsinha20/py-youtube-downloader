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
