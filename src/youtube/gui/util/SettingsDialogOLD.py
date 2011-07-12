# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialog.ui'
#
# Created: Tue Feb 16 14:00:47 2010
#      by: PyQt4 UI code generator 4.7-snapshot-20091223
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import youtube.util.xml.PropertiesAccessor
class Ui_Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        ''' Is the non default constructor that sets up the main widget'''
        '''This is not generated with QT Designer'''
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parentApp = parent
        
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 119)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 80, 281, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 20, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 50, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 50, 31, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
#        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.okButton)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #Populate Values from XML
        self.readValuesFromXml()

        #SLots
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.browseForLibLocation)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.browseForVlcLocation)
#        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("triggered()"), self.okButton)
    def retranslateUi(self, Dialog):
        #WIndow Icon
        Dialog.setWindowIcon(QtGui.QIcon(QtCore.QString("./resources/app.ico")))
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Video Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Library Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "VLC Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
    def okButton(self):
        '''
        This is where we write the configs in an xml
        '''
        properties = youtube.util.xml.PropertiesAccessor.PropertiesAccessor()
        properties.write(str(self.lineEdit.text()), str(self.lineEdit_2.text()))
        #Cal the parent APp- which is AudioDownloaderApp as referenced by MainWIndow in the View
        #It then calls a mutator to change the library path and then reloads the library
        
        self.parentApp.setLibraryPath(str(self.lineEdit.text()))
        self.parentApp.setVlcPath(str(self.lineEdit_2.text()))
        self.parentApp.updateVideoLibrary()
        
        self.accept()
    def readValuesFromXml(self):
        '''
        This reads values from config file
        '''
        properties = youtube.util.xml.PropertiesAccessor.PropertiesAccessor()
        properties.readProperties()
        
        self.lineEdit.setText(properties.getLibraryPath())
        self.lineEdit_2.setText(properties.getVlcPath())

    def browseForLibLocation(self):
        location = self.browseForFiles("Select Library Location", True)
        self.lineEdit.setText(location)
        
    def browseForVlcLocation(self):
        vlcLocation = self.browseForFiles("Select VLC Executable Location", False)
        self.lineEdit_2.setText(vlcLocation)
        
    def browseForFiles(self, dialogText, browseForDirectory):
        if browseForDirectory is True:
            browseDialog = QtGui.QFileDialog(self, dialogText, self.lineEdit.text())    
            browseDialog.setFileMode(QtGui.QFileDialog.Directory)
        else:
            browseDialog = QtGui.QFileDialog(self, dialogText, self.lineEdit_2.text())
        browseDialog.setOption(QtGui.QFileDialog.ShowDirsOnly)       
        browseDialog.setViewMode(QtGui.QFileDialog.Detail)
        path = ''
        if (browseDialog.exec_()):
            folderNames = browseDialog.selectedFiles()
            #Get the first QString from QSTringList
            path = str(folderNames.takeAt(0))
            print 'Library Location:', path
        return path
