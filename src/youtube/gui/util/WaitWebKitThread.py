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
        
        
        
        
