'''Testing License v0.1'''
'''
Created on Jul 5, 2009

@author: Rahul Sinha
'''
from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(314, 50)
        Dialog.setMaximumSize(QtCore.QSize(314, 50))
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))


class action_select_dialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.o)
        

    def o(self):
        print "close the window"
        self.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = action_select_dialog()
    ui.show()
    sys.exit(app.exec_())
