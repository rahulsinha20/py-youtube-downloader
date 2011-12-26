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
Created on 27/11/2010

@author: Rahul
'''
from PyQt4 import QtGui

class CustomizedDirectDownloadButton(QtGui.QPushButton):
    '''
    This allows QPushButton having toggle state - Add, Remove
    '''

    def __init__(self, counter, parent=None):
        ''' Is the non default constructor that sets up the main widget'''
        QtGui.QPushButton.__init__(self, parent)
        self.addState = True
        self.buttonCounter = counter
    def setButtonCounter(self, value):
        self.buttonCounter = value
    def getButtonCounter(self):
        '''
        Returns button number/index
        '''
        return self.buttonCounter
    def setAddState(self, state):
        '''
        Sets Add State
        '''
        self.addState = state
        
    def getAddState(self):
        '''
        Returns Add State for the button
        '''
        return self.addState
