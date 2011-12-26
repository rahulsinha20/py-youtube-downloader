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
Created on 14/09/2010

@author: asinha
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesktopWallpaperDialog.ui'
#
# Created: Thu Jul 16 09:30:16 2009
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
class Ui_WallpaperChangerDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent, QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("QDialog { background-color: lightblue; }");
        self.setupUi(self)   
    def setImage(self, path, controller):
        self.imagePath = path
        self.controller = controller
         
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(70, 54)
        self.label = WallpaerChangerLabel(Dialog)
#        self.label.setImagePath(self.imagePath)
        self.label_2 = DeleteFileLabel(Dialog)
        #self.label_2.setUIController()
#        self.label_2.setImagePath(self.imagePath,self.controller)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

class WallpaerChangerLabel(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QLabel.__init__(self, parent)
        self.setText(' Download')
        self.setGeometry(QtCore.QRect(0, 5, 161, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.setFont(font)
        self.setObjectName("label")
        self.par = parent
    def setImagePath(self, p):
        self.imagePath = p
    def mouseReleaseEvent(self, event):
        print 'Label clicked!' 
        self.par.close()   
#        print "Image Path:",self.imagePath   
      
      
class DeleteFileLabel(QtGui.QLabel):        
    def __init__(self, parent):
        QtGui.QLabel.__init__(self, parent)
        self.setText(" View")
        self.setGeometry(QtCore.QRect(0, 30, 171, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.setFont(font)
        self.setObjectName("label_2")
        self.par = parent
    def setImagePath(self, p, control):
        self.imagePath = p
        self.controller = control             
    #def setUIController(self,control):
           
    def mouseReleaseEvent(self, event):
        print 'Label clicked!' 
        self.par.close()   
#        print "Image Path:",self.imagePath  
#        os.remove(self.imagePath)
#        self.controller.uploadLibrary()
#        self.controller.ui.clearWidgetsFromLayout()
#        self.controller.ui.addDefaultPic()
