'''Testing License v0.1'''
'''
Created on Aug 1, 2011

@author: Rahul
'''

class ActiveDownloadItem(object):
    '''
    classdocs
    '''


    def __init__(self, label, progressBar, button):
        '''
        Constructor
        '''
        self.activeDownloadLabel = label
        self.activeDownloadProgressBar = progressBar
        self.activeDownloadButton = button
    def getActiveDownloadLabel(self):
        return self.activeDownloadLabel
    def getActiveDownloadProgressBar(self):
        return self.activeDownloadProgressBar
    def getActiveDownloadButton(self):
        return self.activeDownloadButton
    