'''Testing License v0.1'''
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
