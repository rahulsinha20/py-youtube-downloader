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
    