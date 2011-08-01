'''
Created on 01/08/2011

@author: asinha
'''
from PyQt4 import QtGui, QtCore
class NotificationMessageBox(QtGui.QMessageBox):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QMessageBox.__init__(self,parent)
        self.setText("Notification")
        self.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel);
        self.stimer = QtCore.QTimer()
        QtCore.QObject.connect(self.stimer, QtCore.SIGNAL("timeout()"), self.constantUpdate)
        self.stimer.start(1000)
    def constantUpdate(self):
        """
        Slot for singleShot timer timeout
        """
        print 'done'
        self.stimer.stop()
        self.setVisible(False)
        self.destroy()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    obj = NotificationMessageBox()
    obj.exec_()
    
    