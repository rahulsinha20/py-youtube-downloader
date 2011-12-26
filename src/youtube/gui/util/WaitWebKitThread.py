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
Created on Feb 21, 2010

@author: Rahul Sinha
'''
from PyQt4 import QtCore

class WaitWebKitThread(QtCore.QThread):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        QtCore.QThread.__init__(self)
        self.parent = parent
    
    def run(self):
        html = '<html><body>Waiting<img src="http://www.sherv.net/cm/emo/hearts/late.gif" height=80px width=100px></img></body></html>'
        self.parent.webView.setHtml(html)
        self.parent.webView.show()
#        for i in range (0,10000):
#            print 'wait'
        
        
        
        
