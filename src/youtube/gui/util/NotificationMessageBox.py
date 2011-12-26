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
        self.stimer.start(15000)
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
    
    