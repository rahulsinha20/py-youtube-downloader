'''Testing License v0.1'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\dev\SettingsDialog.ui'
#
# Created: Tue Jul 12 15:03:14 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import youtube.util.xml.PropertiesAccessor
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        ''' Is the non default constructor that sets up the main widget'''
        '''This is not generated with QT Designer'''
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.parentApp = parent
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(536, 274)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/icon.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(160, 240, 171, 32))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.imageLabel = QtGui.QLabel(Dialog)
        self.imageLabel.setGeometry(QtCore.QRect(10, 10, 141, 121))
        self.imageLabel.setFrameShape(QtGui.QFrame.NoFrame)
        self.imageLabel.setFrameShadow(QtGui.QFrame.Raised)
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/ResourceImages/configuration-settings-icon.png")))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 120, 521, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 150, 291, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 150, 75, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ResourceImages/Browse 1 Icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ResourceImages/Browse 1 Icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ResourceImages/Browse 1 Icon.jpg")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/ResourceImages/Browse 1 Icon.jpg")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 351, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 220, 291, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 220, 75, 23))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(200, 10, 211, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(30, 196, 441, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.checkBox.setFont(font)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        #Populate Values from XML
        self.readValuesFromXml()
        #Slots
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.okButton)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        self.retranslateUi(Dialog)
        #SLots
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.browseForLibLocation)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.browseForVlcLocation)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL("stateChanged(int)"), self.checkBoxSlot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00aa00;\">It looks this is the first time you are using the application. Please select media locations for your files which will be imported to the library and a default player.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">Library Path: </span><span style=\" font-size:10pt; color:#ff0000;\">Please select a folder that the application will use to download your videos.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#00aa7f;\">Current path:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#0000ff;\">Media Player: </span><span style=\" font-size:10pt; color:#ff0000;\">Please select your default video player.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#00aa7f;\">Current path:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Configuration Editor</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "No thanks, I will manage them myself", None, QtGui.QApplication.UnicodeUTF8))

    def checkBoxSlot(self, state):
        '''
        Slot for checkbox - once selected it disables media player availability to the app
        '''
        if state == 2:
            self.lineEdit_2.setEnabled(False)
            self.pushButton_2.setEnabled(False)
        else:
            self.lineEdit_2.setEnabled(True)
            self.pushButton_2.setEnabled(True)
    def okButton(self):
        '''
        This is where we write the configs in an xml
        '''
        properties = youtube.util.xml.PropertiesAccessor.PropertiesAccessor()
        #get state for medi player enabled
        if self.checkBox.checkState()==2:
            self.mediaPlayerEnabled = 'false'
        else:
            self.mediaPlayerEnabled = 'true';
        properties.write(str(self.lineEdit.text()), str(self.lineEdit_2.text()), self.mediaPlayerEnabled)
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
        #Check settings for media player
        if properties.getMediaPlayerEnabled() == 'true':
            self.checkBox.setChecked(False)
            self.pushButton_2.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
        else:
            self.checkBox.setChecked(True)
            self.pushButton_2.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
    def browseForLibLocation(self):
        location = self.browseForFiles("Select Library Location", True)
        self.lineEdit.setText(location)
        
    def browseForVlcLocation(self):
        vlcLocation = self.browseForFiles("Select Media Player Executable Location", False)
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
import SettingsResources_rc